import { createRouter, createWebHashHistory } from 'vue-router';
import Dashboard from '../views/DashboardView.vue';
import Login from '../views/LoginView.vue';
import Signup from '../views/SignupView.vue';
import axios from 'axios';

const routes = [
    { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },  // Protect this route
    { path: '/login', component: Login },
    { path: '/signup', component: Signup },
    { path: '/', redirect: '/dashboard' },
];

const router = createRouter({
    history: createWebHashHistory(),  // Use hash mode for Vue Router
    routes,
});

// Add a navigation guard to check authentication
router.beforeEach(async (to, from, next) => {
    // Check if the route requires authentication
    if (to.meta.requiresAuth) {
        try {
            // Call the API to check if the user is authenticated
            const response = await axios.get('/dashboard/check-login-status/');
            const isAuthenticated = response.data.isAuthenticated;

            if (isAuthenticated) {
                next();  // Allow access to the route
            } else {
                next('/login');  // Redirect to login if not authenticated
            }
        } catch (error) {
            console.error('Error checking authentication:', error);
            next('/login');  // Redirect to login on error
        }
    } else {
        // For non-authenticated routes like login or signup
        next();  // Proceed as usual
    }
});

export default router;
