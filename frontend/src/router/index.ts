import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import IdeaList from '../components/IdeaList.vue'
import AdminLogin from '../components/AdminLogin.vue'
import AdminDashboard from '../components/AdminDashboard.vue'

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/ideas', name: 'ideas', component: IdeaList },
  { path: '/admin', name: 'admin-dashboard', component: AdminDashboard },
  { path: '/admin/login', name: 'admin-login', component: AdminLogin },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
