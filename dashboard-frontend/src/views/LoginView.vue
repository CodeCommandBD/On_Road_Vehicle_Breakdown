<template>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="card shadow p-4" style="width: 100%; max-width: 400px;">
      <h3 class="card-title text-center mb-4">Login</h3>
      <form @submit.prevent="login">
        <div class="form-group mb-3">
          <label for="username" class="form-label">Username</label>
          <input
              v-model="username"
              type="text"
              class="form-control"
              id="username"
              placeholder="Enter username"
              required>
        </div>
        <div class="form-group mb-3">
          <label for="password" class="form-label">Password</label>
          <input
              v-model="password"
              type="password"
              class="form-control"
              id="password"
              placeholder="Enter password"
              required>
        </div>
        <div class="d-grid gap-2">
          <button type="submit" class="btn btn-primary btn-block">Login</button>
        </div>
        <div class="text-center mt-3">
          <small>
            Don't have an account?
            <router-link to="/signup">Sign up here</router-link>
          </small>
        </div>
      </form>
    </div>
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
    async login() {
      const formData = new URLSearchParams();
      formData.append('username', this.username);
      formData.append('password', this.password);

      try {
        const response = await axios.post('/login/', formData);
        if (response.status === 200) {
          this.$router.push('/dashboard');  // Redirect to the dashboard on successful login
        }
      } catch (error) {
        console.error('Login failed:', error);
      }
    },
  },
};
</script>

<!-- Add Bootstrap styles in your main.js or index.html file -->
<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f8f9fa;
}

.card {
  border-radius: 0.5rem;
}

.form-control {
  border-radius: 0.25rem;
}

.btn-primary {
  border-radius: 0.25rem;
}
</style>
