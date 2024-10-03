import {createApp} from 'vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import {BootstrapVueNext} from 'bootstrap-vue-next';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';
import { Swiper, Navigation, Pagination } from 'swiper';


Swiper.use([Navigation, Pagination]);
import mitt from 'mitt';
import HelloProject from './components/HelloProject.vue'
import SignUp from "@/templates/assets/js/components/SignUp";
import UserLogin from "@/templates/assets/js/components/UserLogin";
import HeroArea from "@/templates/assets/js/components/HeroArea";
import RepairService from "@/templates/assets/js/components/RepairService";
import TwentyfourHour from "@/templates/assets/js/components/TwentyfourHour";
import TopGarage from "@/templates/assets/js/components/TopGarage";
import ServiceBook from "@/templates/assets/js/components/ServiceBook";
import ServicePackage from "@/templates/assets/js/components/ServicePackage";
import CustomerTestimonial from "@/templates/assets/js/components/CustomerTestimonial";
import FaqOnline from "@/templates/assets/js/components/FaqOnline";
import ServiceCounter from "@/templates/assets/js/components/ServiceCounter";
import ServiceModel from "@/templates/assets/js/components/ServiceModel";
import RoadNav from "@/templates/assets/js/components/RoadNav";
import RoadFooter from "@/templates/assets/js/components/RoadFooter";
const emitter = mitt();
const app = createApp({})
app.component('hello-project', HelloProject)
app.component('sign-up', SignUp)
app.component('user-login', UserLogin)
app.component('hero-area',HeroArea)
app.component('repair-service', RepairService)
app.component('twenty-hour', TwentyfourHour)
app.component('top-garage', TopGarage)
app.component('service-book', ServiceBook)
app.component('service-package', ServicePackage)
app.component('customer-testimonial', CustomerTestimonial)
app.component('faq-online', FaqOnline)
app.component('service-counter', ServiceCounter)
app.component('service-model', ServiceModel)
app.component('road-nav', RoadNav)
app.component('road-footer', RoadFooter)
app.use(BootstrapVueNext);
app.config.globalProperties.emitter = emitter;

app.mount('body')