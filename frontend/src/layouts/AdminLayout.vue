<template>
  <div class="min-h-screen bg-neutral-100 flex">
    <!-- Mobile Sidebar Overlay -->
    <div
      v-if="isMobileSidebarOpen"
      class="fixed inset-0 z-50 lg:hidden"
      @click="closeMobileSidebar"
    >
      <div class="fixed inset-0 bg-black/50" />
      <div
        class="fixed left-0 top-0 h-full w-80 max-w-[85vw] bg-card border-r border-border shadow-xl transform transition-transform duration-300"
        @click.stop
      >
        <AdminSidebar 
          :ideas="ideas" 
          @logout="logout"
          :is-mobile="true"
          @close="closeMobileSidebar"
        />
      </div>
    </div>

    <!-- Desktop Sidebar -->
    <aside class="w-72 bg-card border-r border-border flex-shrink-0 hidden lg:block sticky top-0 h-screen overflow-y-auto">
      <AdminSidebar :ideas="ideas" @logout="logout" :is-mobile="false" />
    </aside>

    <!-- Main Content Area -->
    <main class="flex-1 overflow-auto bg-neutral-50">
      <div class="p-4 sm:p-6 lg:p-8 max-w-full">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '../components/AdminSidebar.vue'
import { fetchIdeas } from '../services/api'
import type { Idea } from '../types'
import { useRouter } from 'vue-router'

const ideas = ref<Idea[]>([])
const isMobileSidebarOpen = ref(false)
const router = useRouter()

const load = async () => {
  try {
    const username = localStorage.getItem('admin_user') || undefined
    const password = localStorage.getItem('admin_pass') || undefined
    const res = await fetchIdeas(username, password)
    ideas.value = res.data || []
  } catch (err) {
    console.error(err)
    router.push('/admin')
  }
}

const toggleMobileSidebar = () => {
  isMobileSidebarOpen.value = !isMobileSidebarOpen.value
}

const closeMobileSidebar = () => {
  isMobileSidebarOpen.value = false
}

const logout = () => {
  localStorage.removeItem('admin_user')
  localStorage.removeItem('admin_pass')
  router.push('/admin/login')
}

onMounted(load)
</script>