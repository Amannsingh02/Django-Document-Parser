<template>
  <div class="home-container">
    <h1>Welcome</h1>
    <img src="http://100dayscss.com/codepen/upload.svg" class="upload-icon" />
    <input class="input" type="file" ref="fileInput" />
    
    <button class="btn1" @click="uploadFile">Upload</button>
    <button class="btn2" @click="logoutUser">Logout</button>
    <DocumentList />
  </div>
</template>

<script>
import axios from 'axios';
import DocumentList from '../components/DocumentList.vue'
export default {
  components: {
    DocumentList, // Register the DocumentList component
  },
  computed: {
    token() {
      // Retrieve the token from the Vuex store
      return this.$store.state.user ;
    },
  },
  methods: {
    async logoutUser() {
      try {
        // Use nextTick to wait for the component to re-render after state update
        await this.$nextTick();

        // Check if the user is logged in (token is available)
        if (!this.token) {
          console.error('Token not available. User may not be logged in.');
          return;
        }

        // Include the token in the headers for the logout request
        const config = {
          headers: {
            Authorization: `Token ${this.token}`,
          },
        };

        // Make the logout API call with the token in the headers
        await axios.post('http://127.0.0.1:8000/api/logout/', null, config);

        // Clear the user from Vuex store after successful logout
        this.$store.commit('SET_USER', null);

        // Redirect the user back to the login page
        this.$router.push('/login');
      } catch (error) {
        console.error('Logout failed:', error.response.data);
      }
    },
    async uploadFile() {
      // Get the selected file from the input element
      const fileInput = this.$refs.fileInput;
      const file = fileInput.files[0];
      if (!file) {
        console.error('No file selected.');
        return;
      }
      // Create a FormData object to send the file
      const formData = new FormData();
      formData.append('file', file, file.name);
      console.log("mam",formData);
      console.log(formData.get('file'));


      // Include the token in the headers for the upload request
      const config = {
        headers: {
          Authorization: `Token ${this.token}`,
          'Content-Type': 'multipart/form-data',
          
        },
      };

      // Make the file upload API call with the token in the headers
      axios.post('http://127.0.0.1:8000/api/upload/', formData, config)
        .then(response => {
          console.log('File uploaded successfully:', response.data);
        })
        .catch(error => {
          console.error('File upload failed:', error.response.data);
        });
    },
  },
};
</script>

<style>
.btn1 {
	display: block;
	width: 120px;
	height: 30px;
	background: rgb(36, 9, 155);
	color: #fff;
	border-radius: 3px;
	border: 0;
	box-shadow: 0 3px 0 0 rgb(77, 88, 241);
	transition: all 0.3s ease-in-out;
	font-size: 14px;
}

.btn1:hover {
	background: rebeccapurple;
	box-shadow: 0 3px 0 0 deeppink;
}

.btn2 {
	display: block;
	width: 120px;
	height: 30px;
  margin-top: 10px;
	background: rgb(194, 11, 11);
	color: #fff;
	border-radius: 3px;
	border: 0;
	box-shadow: 0 3px 0 0 rgb(240, 121, 88);
	transition: all 0.3s ease-in-out;
	font-size: 14px;
}

.btn2:hover {
	background: rebeccapurple;
	box-shadow: 0 3px 0 0 deeppink;
}

.input {
	top: -62px;
	left: 0;
	width: 100%;
	height: 100%;
  margin-left: 485px;
}
.upload-icon {
	margin-left: -200px;
  margin-top: 10px;
  width: 100px;
  height: 100px;
}
</style>
