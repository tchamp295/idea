<template>
  <div class="min-h-screen bg-custom-light">
    <!-- Admin Navbar -->
    <header class="bg-card shadow-md sticky top-0 z-50 border-b border-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Admin Logo -->
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-custom-primary rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.031 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <span class="text-xl font-bold text-custom-primary">Deep Ideas Admin</span>
          </div>

          <!-- Admin Actions -->
          <div class="flex items-center space-x-3">
            <router-link 
              to="/" 
              class="text-foreground hover:text-custom-primary px-3 py-2 rounded-md font-medium transition-colors text-sm"
            >
              ← Back to Site
            </router-link>
            <Button 
              variant="destructive" 
              size="sm"
              @click="logout" 
              class="bg-red-600 hover:bg-red-700"
            >
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
              </svg>
              Logout
            </Button>
          </div>
        </div>
      </div>
    </header>

    <!-- Page Header Section -->
    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 py-8">
      <div class="text-center">
        <div class="flex items-center justify-center gap-3 mb-4">
          <Badge class="bg-primary-50 text-custom-primary border-custom-primary/20 text-base font-semibold px-4 py-2">
            Admin Dashboard
          </Badge>
        </div>
        <h1 class="text-4xl lg:text-5xl font-bold mb-4">
          <span class="text-foreground">Idea</span>
          <span class="text-custom-primary ml-2">Management</span>
        </h1>
        <p class="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
          Review and manage AI-analyzed ideas submitted to the 
          <span class="text-custom-primary font-semibold">Deep Funding</span> platform.
        </p>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">

      <!-- Loading State -->
      <div v-if="loading" class="flex items-center justify-center py-20">
        <Card class="max-w-md mx-auto">
          <CardContent class="p-8 text-center">
            <div class="w-20 h-20 border-4 border-custom-primary border-t-transparent rounded-full animate-spin mx-auto mb-6"></div>
            <h3 class="text-xl font-semibold text-foreground mb-2">Loading Dashboard</h3>
            <p class="text-muted-foreground">Fetching submitted ideas and analytics...</p>
          </CardContent>
        </Card>
      </div>

      <!-- Empty State -->
      <div v-else-if="ideas.length === 0" class="text-center py-20">
        <Card class="max-w-lg mx-auto">
          <CardContent class="p-12 text-center">
            <div class="w-24 h-24 bg-primary-50 rounded-2xl flex items-center justify-center mx-auto mb-6">
              <svg class="w-12 h-12 text-custom-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-foreground mb-3">No Ideas Submitted Yet</h3>
            <p class="text-lg text-muted-foreground mb-6">When users submit their innovative ideas, they will appear here for review and analysis.</p>
            <Button @click="load" class="bg-custom-primary hover-primary text-white px-6 py-3 rounded-lg shadow-lg">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              Refresh
            </Button>
          </CardContent>
        </Card>
      </div>

      <!-- Ideas Dashboard -->
      <div v-else>
        <!-- Enhanced Statistics Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
          <Card class="hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 border-2 border-primary-100">
            <CardContent class="p-8 text-center">
              <div class="w-16 h-16 bg-custom-primary rounded-2xl flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <div class="text-4xl font-bold text-custom-primary mb-2">{{ ideas.length }}</div>
              <div class="text-lg font-semibold text-foreground mb-1">Total Submissions</div>
              <div class="text-sm text-muted-foreground">All time submissions</div>
            </CardContent>
          </Card>
          
          <Card class="hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 border-2 border-secondary-100">
            <CardContent class="p-8 text-center">
              <div class="w-16 h-16 bg-custom-secondary rounded-2xl flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3a2 2 0 012-2h4a2 2 0 012 2v4m-8 0h8m0 0v5a2 2 0 01-2 2H10a2 2 0 01-2-2V7" />
                </svg>
              </div>
              <div class="text-4xl font-bold text-custom-secondary mb-2">{{ recentIdeasCount }}</div>
              <div class="text-lg font-semibold text-foreground mb-1">This Week</div>
              <div class="text-sm text-muted-foreground">Recent submissions</div>
            </CardContent>
          </Card>
          
          <Card class="hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 border-2 border-yellow-200">
            <CardContent class="p-8 text-center">
              <div class="w-16 h-16 bg-custom-accent rounded-2xl flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
                </svg>
              </div>
              <div class="text-4xl font-bold text-custom-accent mb-2">{{ ideasWithFilesCount }}</div>
              <div class="text-lg font-semibold text-foreground mb-1">With Files</div>
              <div class="text-sm text-muted-foreground">Ideas with attachments</div>
            </CardContent>
          </Card>
        </div>

        <!-- Enhanced Filter and Sort Controls -->
        <Card class="mb-8 border-2 border-border">
          <CardContent class="p-6">
            <div class="flex flex-col lg:flex-row gap-6 items-start lg:items-center justify-between">
              <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4">
                <Label class="text-lg font-semibold text-foreground whitespace-nowrap">Sort by:</Label>
                <Select v-model="sortBy">
                  <SelectTrigger class="w-full sm:w-64 h-12 text-base border-2 border-border focus:border-custom-primary">
                    <SelectValue placeholder="Select sort option" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="created_at">Latest First</SelectItem>
                    <SelectItem value="title">Title (A-Z)</SelectItem>
                    <SelectItem value="oldest_first">Oldest First</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              
              <div class="flex items-center gap-3">
                <Badge class="bg-primary-50 text-custom-primary border-custom-primary/30 text-base font-semibold px-4 py-2">
                  {{ ideas.length }} {{ ideas.length === 1 ? 'Idea' : 'Ideas' }}
                </Badge>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Ideas List -->
        <div class="space-y-6">
          <IdeaCard 
            v-for="(idea, idx) in sortedIdeas" 
            :key="idea.id || idx" 
            :idea="idea" 
            layout="list"
            class="hover:shadow-lg transition-shadow duration-300"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import IdeaCard from './IdeaCard.vue'
import { fetchIdeas } from '../services/api'
import type { Idea } from '../services/api'
import { useRouter } from 'vue-router'
import { Button, Card, CardContent, Badge, Label, Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from './ui'

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
    // if unauthorized or error, redirect to login
    router.push('/admin')
  } finally {
    loading.value = false
  }
}

const sortIdeas = () => {
  // Trigger reactivity - sortedIdeas computed will handle the actual sorting
}

const logout = () => {
  localStorage.removeItem('admin_user')
  localStorage.removeItem('admin_pass')
  router.push('/admin')
}

onMounted(load)
</script>
