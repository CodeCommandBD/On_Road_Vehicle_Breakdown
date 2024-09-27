import {createApp} from 'vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import {BootstrapVueNext} from 'bootstrap-vue-next';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';
import mitt from 'mitt';
import HelloProject from './components/HelloProject.vue'
import SignUp from "@/templates/assets/js/components/SignUp";
import UserLogin from "@/templates/assets/js/components/UserLogin";
const emitter = mitt();
const app = createApp({})
app.component('hello-project', HelloProject)
app.component('sign-up', SignUp)
app.component('user-login', UserLogin)

app.use(BootstrapVueNext);
app.config.globalProperties.emitter = emitter;

app.mount('body')