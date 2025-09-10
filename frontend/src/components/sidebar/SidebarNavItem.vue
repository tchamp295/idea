<template>
  <router-link 
    :to="to" 
    :class="[
      'flex items-center px-3 py-3 text-sm font-medium rounded-lg transition-all duration-200',
      isActive 
        ? 'bg-primary-50 text-custom-primary border-l-4 border-custom-primary shadow-sm' 
        : 'text-muted-foreground hover:text-foreground hover:bg-muted hover:shadow-sm'
    ]"
  >
    <svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="icon" />
    </svg>
    
    <span class="flex-1">{{ label }}</span>
    
    <span 
      v-if="badgeCount !== undefined" 
      class="ml-auto bg-custom-primary text-white text-xs font-semibold px-2 py-1 rounded-full min-w-[1.5rem] text-center"
    >
      {{ badgeCount }}
    </span>
  </router-link>
</template>

<script setup lang="ts">
interface Props {
  icon: string
  label: string
  to: string
  isActive?: boolean
  badgeCount?: number
}

withDefaults(defineProps<Props>(), {
  isActive: false,
  badgeCount: undefined
})
</script>