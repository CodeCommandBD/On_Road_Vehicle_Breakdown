import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import axios from 'axios';
import {getCsrfToken} from './utils/csrf';


// Set default headers for axios
axios.defaults.headers.common['X-CSRFToken'] = getCsrfToken();

createApp(App).use(router).mount('#app')
