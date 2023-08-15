<!-- UserRegistrationForm.vue -->
<template>
  <div id="register">
    <h1>User Registration</h1>
    <form @submit.prevent="registerUser" class="registration-form">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>

      <button type="submit">Register</button>
      <h5>Already Have An Account?<a href="http://localhost:8080/login">Login</a></h5>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    registerUser() {
      const userData = {
        username: this.username,
        email: this.email,
        password: this.password,
      };

      axios.post('http://127.0.0.1:8000/api/register/', userData)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error.response.data);
        });
    }
  }
}
</script>


<style lang="scss">
#register {
  max-width: 400px;
  margin: 0 auto;
}

.registration-form {
  padding: 20px;
  border: 1px solid #260b9d;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 15px;
  margin-right: 20px;
}

label {
  font-weight: bold;
  display: block;
  padding-top: 20px;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  margin-right: 100px;
  padding: 10px;
  border: 1px solid #2c2387;
  border-radius: 5px;
}

button[type="submit"] {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  margin-top: 20px;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}
</style>
