<template>
  <div class="min-h-screen bg-purple-50 backdrop-blur-md">
    <!-- AI-Themed Header -->
    <header class="sticky top-0 z-50 border-b border-border bg-card/80 backdrop-blur-md">
      <div class="container mx-auto px-4">
        <div class="flex h-16 items-center justify-between">
          <!-- Brand Text -->
          <router-link 
            to="/" 
            class="text-xl font-bold text-primary transition-colors"
          >
            AI Idea Filter
          </router-link>

          <!-- Navigation -->
          <nav class="flex items-center gap-1">
           
            
         
            
            <router-link 
              to="/admin" 
              class="px-4 py-2 rounded-lg text-sm font-medium transition-all hover:bg-accent hover:text-accent-foreground"
              :class="$route.path === '/admin' ? 'bg-primary text-primary-foreground' : 'text-muted-foreground'"
            >
              <div class="flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                Admin
              </div>
            </router-link>

            <!-- Dark Mode Toggle -->
            <button 
              @click="toggleDarkMode"
              class="ml-4 p-2 rounded-lg text-muted-foreground hover:bg-accent hover:text-accent-foreground transition-all"
            >
              <svg v-if="isDark" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
              </svg>
            </button>
          </nav>
        </div>
      </div>
    </header>

    <!-- Main Content with AI Background -->
    <main class="relative">
      <!-- AI Grid Background -->
      <div class="fixed inset-0 -z-10 opacity-30">
        <div class="absolute inset-0 bg-gradient-to-br from-primary/5 via-transparent to-secondary/5"></div>
        <div class="absolute inset-0" style="background-image: radial-gradient(circle at 1px 1px, rgba(79, 70, 229, 0.15) 1px, transparent 0); background-size: 20px 20px;"></div>
      </div>
      
      <router-view />
    </main>

 
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const isDark = ref(false)

const toggleDarkMode = () => {
  isDark.value = !isDark.value
  document.documentElement.classList.toggle('dark', isDark.value)
  localStorage.setItem('darkMode', isDark.value.toString())
}

onMounted(() => {
  const stored = localStorage.getItem('darkMode')
  if (stored) {
    isDark.value = stored === 'true'
    document.documentElement.classList.toggle('dark', isDark.value)
  }
})
</script>
