<template>
  <div class="flex flex-col h-full">
    <!-- Sidebar Header -->
    <SidebarHeader :is-mobile="isMobile" @close="$emit('close')" />

    <!-- Navigation Menu -->
    <SidebarNavigation :ideas-count="ideas.length" @navigate="handleNavigate" />

    <!-- Sidebar Footer -->
    <SidebarFooter :is-mobile="isMobile" @logout="$emit('logout')" />
  </div>
</template>

<script setup lang="ts">
import type { Idea } from '../types'
import SidebarHeader from './sidebar/SidebarHeader.vue'
import SidebarNavigation from './sidebar/SidebarNavigation.vue'
import SidebarFooter from './sidebar/SidebarFooter.vue'

interface Props {
  ideas: Idea[]
  isMobile: boolean
}

defineProps<Props>()

const emit = defineEmits<{
  logout: []
  close: []
}>()

const handleNavigate = () => {
  // Close mobile sidebar when navigating
  emit('close')
}
</script>