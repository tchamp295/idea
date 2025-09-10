import { createRouter, createWebHistory, type RouteLocationNormalized, type NavigationGuardNext } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import SubmitIdea from '../views/SubmitIdea.vue'
import IdeaList from '../views/IdeaList.vue'
import AdminLogin from '../views/AdminLogin.vue'
import AdminLayout from '../layouts/AdminLayout.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import AdminIdeas from '../views/AdminIdeas.vue'

const adminAuthGuard = (to: RouteLocationNormalized, from: RouteLocationNormalized, next: NavigationGuardNext) => {
  const adminUser = localStorage.getItem('admin_user')
  const adminPass = localStorage.getItem('admin_pass')
  if (adminUser && adminPass) {
    next()
  } else {
    next('/admin/login')
  }
}

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/submit', name: 'submit', component: SubmitIdea },
  { 
    path: '/admin/login', 
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
    path: '/admin',
    component: AdminLayout,
    beforeEnter: adminAuthGuard,
    children: [
      { 
        path: 'dashboard', 
        name: 'admin-dashboard', 
        component: AdminDashboard
      },
      { 
        path: 'ideas', 
        name: 'admin-ideas', 
        component: AdminIdeas
      }
    ]
  }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
