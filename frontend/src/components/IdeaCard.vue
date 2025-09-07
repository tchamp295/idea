<template>
  <div class="bg-white rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-shadow p-6">
    <!-- Header -->
    <div class="flex items-start justify-between mb-3">
      <h3 class="text-xl font-semibold text-gray-900 flex-1 leading-tight">
        {{ idea.title || 'Untitled Idea' }}
      </h3>
      <span class="text-xs text-gray-500 ml-4 whitespace-nowrap">
        {{ formatDate(idea.created_at) }}
      </span>
    </div>

    <!-- Description -->
    <p class="text-gray-700 mb-4 leading-relaxed">
      {{ idea.description || 'No description provided.' }}
    </p>

    <!-- File Attachment -->
    <div v-if="idea.file_url" class="pt-2 border-t border-gray-100">
      <a 
        :href="`http://127.0.0.1:8000${idea.file_url}`" 
        target="_blank"
        class="inline-flex items-center gap-1 text-sm text-blue-600 hover:text-blue-800 font-medium"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
        </svg>
        View Attachment
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Idea } from '../services/api'

interface Props {
  idea: Idea
}

defineProps<Props>()

const formatDate = (dateString?: string) => {
  if (!dateString) return 'Unknown'
  try {
    return new Date(dateString).toLocaleDateString('en-US', { 
      month: 'short', 
      day: 'numeric'
    })
  } catch {
    return 'Unknown'
  }
}
</script>
