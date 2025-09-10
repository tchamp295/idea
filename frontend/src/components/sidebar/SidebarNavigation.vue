<template>
  <nav class="flex-1 p-6">
    <div class="space-y-2">
      <div class="pb-4">
        <h3 class="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-3">
          Overview
        </h3>
        
        <div class="space-y-1">
          <SidebarNavItem
            :icon="DashboardIcon"
            label="Dashboard"
            to="/admin/dashboard"
            :is-active="$route.name === 'admin-dashboard'"
            @click="$emit('navigate')"
          />
          
          <SidebarNavItem
            :icon="IdeaIcon"
            label="All Ideas"
            to="/admin/ideas"
            :badge-count="ideasCount"
            :is-active="$route.name === 'admin-ideas'"
            @click="$emit('navigate')"
          />
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import SidebarNavItem from './SidebarNavItem.vue'

interface Props {
  ideasCount: number
}

defineProps<Props>()
defineEmits<{
  navigate: []
}>()

const $route = useRoute()

const DashboardIcon = `M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z`
const IdeaIcon = `M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z`
</script>