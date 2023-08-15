<!-- Login.vue -->
<template>
    <div class="login-container">
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
  
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
  
        <button type="submit">Login</button>
        <h5>Not Registered?<a href="http://localhost:8080/">Register</a></h5>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      loginUser() {
        const userData = {
          username: this.username,
          password: this.password,
        };
  
        axios.post('http://127.0.0.1:8000/api/login/', userData)
          .then(response => {
            // Save the logged-in user in Vuex store
            this.$store.commit('SET_USER', response.data.token);
            console.log(response.data);

            // Redirect to home page after successful login
            this.$router.push('/home');
          })
          .catch(error => {

            console.error(error.response.data);
          });
      }
    }
  }
  </script>
  
  <style>
  .login-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    font-weight: bold;
    display: block;
  }
  
  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  button[type="submit"] {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button[type="submit"]:hover {
    background-color: #0056b3;
  }
  </style>
  