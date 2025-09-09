<template>
  <div class="min-h-screen bg-background">
    <!-- Brand Colors Header -->
    <header v-if="!$route.path.includes('/admin/dashboard')" class="bg-card shadow-md sticky top-0 z-50 border-b border-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo with Brand Colors -->
          <router-link to="/" class="text-2xl font-bold text-custom-primary hover:text-accent-highlight transition-colors">
            Deep Ideas
          </router-link>

          <!-- Desktop Navigation -->
          <nav class="hidden md:flex space-x-8">
            <router-link 
              to="/admin" 
              class="text-foreground hover:text-custom-primary px-3 py-2 rounded-md font-medium transition-colors"
              :class="$route.path.startsWith('/admin') ? 'text-custom-primary bg-primary-50' : ''"
            >
              Admin
            </router-link>

            <router-link 
              to="/submit"
              class="bg-custom-primary hover:bg-custom-primary-hover text-white px-6 py-2.5 rounded-md font-semibold shadow-lg transition-all transform hover:scale-105"
            >
              Submit Idea
            </router-link>
          </nav>

          <!-- Mobile menu button -->
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="md:hidden p-2 rounded-md text-muted-foreground hover:text-foreground hover:bg-muted transition-colors"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Mobile menu -->
        <div v-show="mobileMenuOpen" class="md:hidden">
          <div class="px-2 pt-2 pb-3 space-y-1 bg-card border-t border-border">
            <router-link 
              to="/admin" 
              @click="mobileMenuOpen = false"
              class="block px-3 py-2 rounded-md text-foreground hover:text-custom-primary hover:bg-muted transition-colors"
              :class="$route.path.startsWith('/admin') ? 'text-custom-primary bg-primary-50' : ''"
            >
              Admin
            </router-link>

            <router-link 
              to="/submit"
              @click="mobileMenuOpen = false"
              class="block w-full mt-2 bg-custom-primary hover:bg-custom-primary-hover text-white px-4 py-2.5 rounded-md text-center font-semibold shadow-lg transition-all"
            >
              Submit Idea
            </router-link>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main>
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// Mobile menu state
const mobileMenuOpen = ref(false)
</script>
