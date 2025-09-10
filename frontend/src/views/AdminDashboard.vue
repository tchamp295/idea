<template>
  <div class="space-y-8">
    <!-- Dashboard Header -->
    <div class="bg-gradient-to-r from-slate-50 to-blue-50 rounded-2xl p-8 border border-slate-200/50">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-3xl font-bold text-slate-800 mb-2">Admin Dashboard</h1>
          <p class="text-slate-600">Monitor and manage submitted ideas</p>
        </div>
        <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-20">
      <Card class="bg-white border-0 shadow-xl">
        <CardContent class="p-8 text-center">
          <div class="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-6"></div>
          <h3 class="text-xl font-semibold text-slate-800 mb-2">Loading Dashboard</h3>
          <p class="text-slate-500">Fetching submitted ideas and analytics...</p>
        </CardContent>
      </Card>
    </div>

    <!-- Ideas Dashboard -->
    <div v-else class="space-y-8">
      <!-- Statistics Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card class="bg-gradient-to-br from-blue-50 to-indigo-50 border-0 shadow-lg hover:shadow-xl transition-all duration-300 group">
          <CardContent class="p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-slate-600 mb-1">Total Ideas</p>
                <p class="text-3xl font-bold text-slate-800">{{ ideas.length }}</p>
                <p class="text-xs text-slate-500 mt-1">All time submissions</p>
              </div>
              <div class="w-12 h-12 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card class="bg-gradient-to-br from-emerald-50 to-green-50 border-0 shadow-lg hover:shadow-xl transition-all duration-300 group">
          <CardContent class="p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-slate-600 mb-1">This Week</p>
                <p class="text-3xl font-bold text-slate-800">{{ recentIdeasCount }}</p>
                <p class="text-xs text-slate-500 mt-1">Recent submissions</p>
              </div>
              <div class="w-12 h-12 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                </svg>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card class="bg-gradient-to-br from-amber-50 to-orange-50 border-0 shadow-lg hover:shadow-xl transition-all duration-300 group">
          <CardContent class="p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-slate-600 mb-1">With Files</p>
                <p class="text-3xl font-bold text-slate-800">{{ ideasWithFilesCount }}</p>
                <p class="text-xs text-slate-500 mt-1">Have attachments</p>
              </div>
              <div class="w-12 h-12 bg-gradient-to-br from-amber-500 to-amber-600 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
                </svg>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <!-- Recent Ideas Section -->
      <div class="bg-white rounded-2xl border border-slate-200/50 shadow-sm">
        <div class="px-8 py-6 border-b border-slate-100">
          <div class="flex items-center gap-4">
            <div class="w-2 h-8 bg-gradient-to-b from-blue-500 to-indigo-600 rounded-full"></div>
            <div>
              <h2 class="text-2xl font-semibold text-slate-800">Recent Ideas</h2>
              <p class="text-sm text-slate-500">Latest submissions from users</p>
            </div>
          </div>
        </div>
        <div class="p-8">
          <div class="space-y-4">
            <IdeaCard 
              v-for="(idea, idx) in sortedIdeas.slice(0, 5)" 
              :key="idea.id || idx" 
              :idea="idea" 
              layout="list"
              class="hover:shadow-lg transition-all duration-300 transform hover:-translate-y-1 border border-slate-100 hover:border-slate-200 rounded-xl bg-slate-50/50 hover:bg-white"
            />
          </div>
          <div class="mt-6 text-center" v-if="ideas.length > 5">
            <router-link 
              to="/admin/ideas" 
              class="inline-flex items-center gap-2 px-6 py-3 bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium rounded-xl transition-colors duration-200"
            >
              View All Ideas
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import IdeaCard from '../components/IdeaCard.vue'
import { fetchIdeas } from '../services/api'
import type { Idea } from '../types'
import { useRouter } from 'vue-router'
import { Card, CardContent } from '../components/ui'

const ideas = ref<Idea[]>([])
const loading = ref(true)
const sortBy = ref('created_at')
const router = useRouter()

// Computed properties for statistics
const recentIdeasCount = computed(() => {
  const weekAgo = new Date()
  weekAgo.setDate(weekAgo.getDate() - 7)
  return ideas.value.filter(idea => {
    if (!idea.created_at) return false
    return new Date(idea.created_at) > weekAgo
  }).length
})

const ideasWithFilesCount = computed(() => {
  return ideas.value.filter(idea => idea.file_url).length
})

// Sorted ideas based on current sort option
const sortedIdeas = computed(() => {
  const sorted = [...ideas.value]
  
  switch (sortBy.value) {
    case 'title':
      return sorted.sort((a, b) => (a.title || '').localeCompare(b.title || ''))
    case 'oldest_first':
      return sorted.sort((a, b) => new Date(a.created_at || 0).getTime() - new Date(b.created_at || 0).getTime())
    case 'created_at':
    default:
      return sorted.sort((a, b) => new Date(b.created_at || 0).getTime() - new Date(a.created_at || 0).getTime())
  }
})

const load = async () => {
  loading.value = true
  try {
    const username = localStorage.getItem('admin_user') || undefined
    const password = localStorage.getItem('admin_pass') || undefined
    const res = await fetchIdeas(username, password)
    ideas.value = res.data || []
  } catch (err) {
    console.error(err)
    router.push('/admin/login')
  } finally {
    loading.value = false
  }
}

const sortIdeas = () => {
  // Trigger reactivity - sortedIdeas computed will handle the actual sorting
}

onMounted(load)
</script>