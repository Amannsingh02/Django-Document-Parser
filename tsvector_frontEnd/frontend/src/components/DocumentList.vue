<template>
    <div class="document-list">
      <h2>My Documents</h2>
      <input class="macx" v-model="searchQuery" placeholder="Search...">
      <button class="btnx" @click="search">Search</button>
      <table class="file-table">
      <thead>
        <tr>
          <th>Filename</th>
          <th>Created At</th>
          <th>Download</th>
        </tr>
      </thead>
      <tbody v-if="searchResults.length>0">
        <tr v-for="file in searchResults" :key="file.id">
          <td>{{ file.filename }}</td>
          <td>{{ file.created_at }}</td>
          <td><a :href="getDownloadLink(file.id)" download>Download</a></td>
        </tr>
      </tbody>
      <tbody v-else>
        <tr v-for="file in files" :key="file.id">
          <td>{{ file.filename }}</td>
          <td>{{ file.created_at }}</td>
          <td><a :href="getDownloadLink(file.id)" download>Download</a></td>
        </tr>
      </tbody>
    </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        files: [],
        searchQuery: '',
        searchResults: [],
      };
    },
    mounted() {
      this.fetchFiles();
      // this.search();
    },
    
    methods: {
      async fetchFiles() {
        try {
          // Make the GET request to fetch documents for the authenticated user
          const response = await axios.get('http://127.0.0.1:8000/documents/', {
            headers: {
              Authorization: `Token ${this.$store.state.user}`,
            },
          });
  
          this.files = response.data;
          console.log("ahlfavbjadbvjadbvj",response.data)
        } catch (error) {
          console.error('Error fetching documents:', error);
        }
      },
      getDownloadLink(fileId) {
      return `http://127.0.0.1:8000/api/textfiles/${fileId}/download/`;
      },
      async search() {
      try {
      const apiUrl = `http://localhost:8000`;
      const response = await axios.get(`${apiUrl}/search/?q=${this.searchQuery}`,{ 
        headers:{
          Authorization: `Token ${this.$store.state.user}`,
       }, 
    });
      this.searchResults =response.data;
      //this.files = [];
      console.log("data",response.data);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  }
  },
  };
  </script>
  
<style>
.macx{
  width: 40%;
  padding: 12px 20px;
  margin: 5px 0;
  box-sizing: border-box;
}
.btnx{
  background-color: #204ad3; 
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  width: 15%;
  height: 40px;
  margin-left: 10px;
  border-radius: 5px;
}
.file-table {
  border-collapse: collapse;
  width: 100%;
}

.file-table th, .file-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.file-table th {
  background-color: #f2f2f2;
}
  </style>
  