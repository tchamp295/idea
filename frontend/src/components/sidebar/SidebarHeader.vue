<template>
  <div class="p-6 border-b border-border">
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <div class="w-12 h-12 bg-custom-primary rounded-xl flex items-center justify-center shadow-lg">
          <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.031 9-11.622 0-1.042-.133-2.052-.382-3.016z" 
            />
          </svg>
        </div>
        <div>
          <h2 class="text-xl font-bold text-foreground">Deep Ideas</h2>
          <p class="text-sm text-muted-foreground">Admin Panel</p>
        </div>
      </div>
      
      <!-- Mobile Close Button -->
      <Button
        v-if="isMobile"
        variant="ghost"
        size="sm"
        @click="$emit('close')"
        class="p-2 hover:bg-muted lg:hidden"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
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
  close: []
}>()
</script>