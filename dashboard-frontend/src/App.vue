<template>
  <div id="app" class="d-flex">
    <!-- Conditional Sidebar -->
    <nav id="sidebar" v-if="showSidebar" class="bg-dark vh-100">
      <ul class="list-unstyled">
        <li>
          <router-link to="/dashboard" class="text-white nav-link">Dashboard</router-link>
        </li>
        <li>
          <router-link to="/profile" class="text-white nav-link">Profile</router-link>
        </li>
        <li>
          <router-link to="/settings" class="text-white nav-link">Settings</router-link>
        </li>
        <li><a href="/logout" class="text-white nav-link">Logout</a></li>
      </ul>
    </nav>

    <!-- Main content area -->
    <div class="flex-grow-1">
      <!-- Conditional Top Navbar -->
      <nav v-if="showNavbar" class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <span class="navbar-brand mb-0 h1">My Dashboard</span>
        </div>
      </nav>

      <!-- Main content -->
      <div class="container-fluid p-3">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';  // Use Axios for API calls

export default {
  name: 'App',
  computed: {
    showSidebar() {
      return this.$route.path !== '/login' && this.$route.path !== '/signup';
    },
    showNavbar() {
      return this.$route.path !== '/login' && this.$route.path !== '/signup';
    }
  },
  methods: {

  }
}
</script>

<style>
#sidebar {
  width: 250px;
}
</style>
