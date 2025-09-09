import { createRouter, createWebHistory, type RouteLocationNormalized, type NavigationGuardNext } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import SubmitIdea from '../views/SubmitIdea.vue'

import IdeaList from '../components/IdeaList.vue'
import AdminLogin from '../components/AdminLogin.vue'
import AdminDashboard from '../components/AdminDashboard.vue'

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/submit', name: 'submit', component: SubmitIdea },
  { path: '/ideas', name: 'ideas', component: IdeaList },
  { 
    path: '/admin', 
    name: 'admin-login', 
    component: AdminLogin,
    beforeEnter: (to: RouteLocationNormalized, from: RouteLocationNormalized, next: NavigationGuardNext) => {
      const adminUser = localStorage.getItem('admin_user')
      const adminPass = localStorage.getItem('admin_pass')
      if (adminUser && adminPass) {
        next('/admin/dashboard')
      } else {
        next()
      }
    }
  },
  { 
    path: '/admin/dashboard', 
    name: 'admin-dashboard', 
    component: AdminDashboard,
    beforeEnter: (to: RouteLocationNormalized, from: RouteLocationNormalized, next: NavigationGuardNext) => {
      const adminUser = localStorage.getItem('admin_user')
      const adminPass = localStorage.getItem('admin_pass')
      if (adminUser && adminPass) {
        next()
      } else {
        next('/admin')
      }
    }
  },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
