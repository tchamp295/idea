<template>
  <div class="p-6 border-t border-border">
    <div :class="isMobile ? 'flex flex-col space-y-3' : 'flex items-center justify-between'">
      <router-link 
        to="/" 
        class="text-sm text-muted-foreground hover:text-custom-primary transition-colors inline-flex items-center"
      >
        <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Back to Site
      </router-link>
      
      <Button 
        variant="outline" 
        :size="isMobile ? 'default' : 'sm'"
        @click="$emit('logout')" 
        class="text-red-600 border-red-200 hover:bg-red-50 hover:border-red-300 transition-colors"
      >
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path 
            stroke-linecap="round" 
            stroke-linejoin="round" 
            stroke-width="2" 
            d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" 
          />
        </svg>
        Logout
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Button } from '../ui'

interface Props {
  isMobile: boolean
}

defineProps<Props>()
defineEmits<{
  logout: []
}>()
</script>