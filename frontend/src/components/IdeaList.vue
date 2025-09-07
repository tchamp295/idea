<template>
  <div class="container mx-auto px-4 py-8 max-w-7xl">
    <!-- Header Section -->
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-blue-50 to-purple-50 text-purple-700 text-sm font-medium mb-6">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364-.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>
        Ideas Gallery
      </div>
      
      <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
        Innovation <span class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">Dashboard</span>
      </h1>
      
      <p class="text-lg text-gray-600 max-w-3xl mx-auto mb-8">
        Browse innovative ideas from our community.
      </p>

    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-20">
      <div class="text-center">
        <div class="w-12 h-12 border-3 border-blue-200 border-t-blue-600 rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-gray-600">Loading ideas...</p>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else-if="ideas.length === 0" class="text-center py-12">
      <p class="text-gray-500 mb-4">No ideas submitted yet.</p>
      <Button 
        @click="$router.push('/')" 
        size="lg"
        class="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white border-0"
      >
        <template #icon>
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
        </template>
        Submit Your First Idea
      </Button>
    </div>

    <!-- Ideas Grid -->
    <div v-else>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <IdeaCard 
          v-for="(idea, idx) in ideas" 
          :key="idea.id || idx" 
          :idea="idea"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { fetchIdeas, type Idea } from '../services/api'
import { useRouter } from 'vue-router'
import { Button } from './ui'
import IdeaCard from './IdeaCard.vue'

const router = useRouter()
const ideas = ref<Idea[]>([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await fetchIdeas()
    ideas.value = res.data || []
  } catch (err) {
    console.error('Failed to load ideas:', err)
    ideas.value = []
  } finally {
    loading.value = false
  }
})
</script>
