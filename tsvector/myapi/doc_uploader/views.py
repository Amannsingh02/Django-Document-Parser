from typing import Self
from django.shortcuts import render
from rest_framework import viewsets
from .models import TextFile
from .serializers import TextFileSerializer

class TextFileViewSet(viewsets.ModelViewSet):
    queryset = TextFile.objects.all()
    serializer_class = TextFileSerializer

import chardet
from django.contrib.postgres.search import SearchVector

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TextFile
from .serializers import TextFileSerializer

from django.db import IntegrityError
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
class FileUploadView(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]


    def post(self, request, *args, **kwargs):
        try:
            file_obj = request.FILES['file']
            print("file_obj:",(file_obj))

            # Detect the encoding of the file content
            #raw_data = file_obj.read()
            #detected_encoding = chardet.detect(raw_data)['encoding']

            # Decode the file content using the detected encoding
            #content = raw_data.decode(detected_encoding)

            # Save the content to the database
            text_file = TextFile(content=file_obj.read(),filename=file_obj.name, user=request.user)
            text_file.save()
            TextFile.objects.filter(id=text_file.id).update(tsvector_content=SearchVector('content'))
            updated_text_file = TextFile.objects.get(id=text_file.id)
            print("tsvector_content after updating:", updated_text_file.tsvector_content)

            # Serialize the data and return the response
            serializer = TextFileSerializer(text_file)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            print("Database save error:", e)




from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        
        
        
        
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TextFile
from .serializers import TextFileSerializer

class TextFileSearchView(APIView):
    def get(self, request):
        # Get the search query from the request parameters
        query = request.query_params.get('q')

        # Perform the search using the SearchVector and SearchQuery
        search_vector = SearchVector('tsvector_content', config='english')
        search_query = SearchQuery(query, config='english')
        results = TextFile.objects.annotate(rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.01).order_by('-rank')

        # Create a simplified dictionary for each search result
        search_result_data = []
        for result in results:
            search_result = {
                'filename': result.filename,
                'created_at': result.created_at,
                # Add any other details you want to include
            }
            search_result_data.append(search_result)

        return Response(search_result_data)


#for listing all the files
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TextFile
from .serializers import TextFileSerializer

class TextFileListView(generics.ListAPIView):
    serializer_class = TextFileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TextFile.objects.filter(user=user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for item in queryset:
            file_info = {
                'id': item.id,
                'filename': item.filename,  # Assuming content is a FileField
                'created_at': item.created_at,
            }
            data.append(file_info)
        
        return Response(data)



#for downloading the file
from django.http import HttpResponse
from .models import TextFile

def download_text_file(request, file_id):
    try:
        text_file = TextFile.objects.get(id=file_id)
        response = HttpResponse(text_file.content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{text_file.filename}"'
        return response
    except TextFile.DoesNotExist:
        # Handle case when the file does not exist
        return HttpResponse('File not found', status=404)
