<template>
  <div class="min-h-screen bg-neutral-100 flex">
    <!-- Admin Sidebar -->
    <aside class="w-72 bg-card border-r border-border flex-shrink-0 hidden lg:block sticky top-0 h-screen overflow-y-auto">
      <div class="flex flex-col h-screen">
        <!-- Sidebar Header -->
        <div class="p-6 border-b border-border">
          <div class="flex items-center space-x-3">
            <div class="w-12 h-12 bg-custom-primary rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.031 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <div>
              <h2 class="text-xl font-bold text-foreground">Deep Ideas</h2>
              <p class="text-sm text-muted-foreground">Admin Panel</p>
            </div>
          </div>
        </div>

        <!-- Navigation Menu -->
        <nav class="flex-1 p-6">
          <div class="space-y-2">
            <div class="pb-4">
              <h3 class="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-3">Overview</h3>
              <a href="#" class="flex items-center px-3 py-3 text-sm font-medium rounded-lg bg-primary-50 text-custom-primary border-l-4 border-custom-primary">
                <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                Dashboard
              </a>
              <a href="#" class="flex items-center px-3 py-3 text-sm font-medium rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted transition-colors">
                <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
                All Ideas
                <span class="ml-auto bg-custom-primary text-white text-xs font-semibold px-2 py-1 rounded-full">{{ ideas.length }}</span>
              </a>
              <a href="#" class="flex items-center px-3 py-3 text-sm font-medium rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted transition-colors">
                <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
                </svg>
                Analytics
              </a>
            </div>

            <div class="pt-4 border-t border-border">
              <h3 class="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-3">Management</h3>
              <a href="#" class="flex items-center px-3 py-3 text-sm font-medium rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted transition-colors">
                <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" />
                </svg>
                Users
              </a>
              <a href="#" class="flex items-center px-3 py-3 text-sm font-medium rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted transition-colors">
                <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                Settings
              </a>
            </div>
          </div>
        </nav>

        <!-- Sidebar Footer -->
        <div class="p-6 border-t border-border">
          <div class="flex items-center justify-between">
            <router-link 
              to="/" 
              class="text-sm text-muted-foreground hover:text-custom-primary transition-colors"
            >
              ← Back to Site
            </router-link>
            <Button 
              variant="outline" 
              size="sm"
              @click="logout" 
              class="text-red-600 border-red-200 hover:bg-red-50 hover:border-red-300"
            >
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
              </svg>
              Logout
            </Button>
          </div>
        </div>
      </div>
    </aside>

    <!-- Mobile Header (visible on small screens) -->
    <div class="lg:hidden bg-card border-b border-border sticky top-0 z-50 w-full">
      <div class="px-4 py-3 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-8 h-8 bg-custom-primary rounded-lg flex items-center justify-center">
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4" />
            </svg>
          </div>
          <span class="text-lg font-bold text-foreground">Admin</span>
        </div>
        <div class="flex items-center space-x-2">
          <router-link to="/" class="text-sm text-muted-foreground">← Back</router-link>
          <Button variant="outline" size="sm" @click="logout" class="text-red-600 border-red-200">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7" />
            </svg>
          </Button>
        </div>
      </div>
    </div>

    <!-- Main Content Area -->
    <main class="flex-1 overflow-auto bg-neutral-50">
      <!-- Dashboard Header -->
      <div class="bg-white border-b border-border px-6 lg:px-8 py-6 sticky top-0 z-10">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <h1 class="text-3xl font-bold text-foreground">Admin Dashboard</h1>
            <p class="text-lg text-muted-foreground mt-1">Manage ideas and monitor platform activity</p>
          </div>
          <div class="flex items-center space-x-3">
            <Button 
              variant="outline" 
              size="sm"
              @click="load" 
              class="border-border hover:bg-muted px-4 py-2"
            >
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              Refresh
            </Button>
          </div>
        </div>
      </div>
      
      <div class="p-6 lg:p-8">

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
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
          <Card class="hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 hover:scale-105 border-0 bg-gradient-to-br from-white to-primary-50 shadow-lg">
            <CardContent class="p-8 text-center relative overflow-hidden">
              <div class="absolute top-0 right-0 w-20 h-20 bg-custom-primary/10 rounded-full -translate-y-8 translate-x-8"></div>
              <div class="w-20 h-20 bg-custom-primary rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-xl relative z-10">
                <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
              </div>
              <div class="text-5xl font-bold text-custom-primary mb-3 relative z-10">{{ ideas.length }}</div>
              <div class="text-xl font-bold text-foreground mb-2 relative z-10">Total Ideas</div>
              <div class="text-base text-muted-foreground relative z-10">All time submissions</div>
            </CardContent>
          </Card>
          
          <Card class="hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 hover:scale-105 border-0 bg-gradient-to-br from-white to-secondary-50 shadow-lg">
            <CardContent class="p-8 text-center relative overflow-hidden">
              <div class="absolute top-0 right-0 w-20 h-20 bg-custom-secondary/10 rounded-full -translate-y-8 translate-x-8"></div>
              <div class="w-20 h-20 bg-custom-secondary rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-xl relative z-10">
                <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                </svg>
              </div>
              <div class="text-5xl font-bold text-custom-secondary mb-3 relative z-10">{{ recentIdeasCount }}</div>
              <div class="text-xl font-bold text-foreground mb-2 relative z-10">This Week</div>
              <div class="text-base text-muted-foreground relative z-10">Recent activity</div>
            </CardContent>
          </Card>
          
          <Card class="hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 hover:scale-105 border-0 bg-gradient-to-br from-white to-yellow-50 shadow-lg sm:col-span-2 lg:col-span-1">
            <CardContent class="p-8 text-center relative overflow-hidden">
              <div class="absolute top-0 right-0 w-20 h-20 bg-custom-accent/10 rounded-full -translate-y-8 translate-x-8"></div>
              <div class="w-20 h-20 bg-custom-accent rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-xl relative z-10">
                <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
                </svg>
              </div>
              <div class="text-5xl font-bold text-custom-accent mb-3 relative z-10">{{ ideasWithFilesCount }}</div>
              <div class="text-xl font-bold text-foreground mb-2 relative z-10">With Files</div>
              <div class="text-base text-muted-foreground relative z-10">Ideas with attachments</div>
            </CardContent>
          </Card>
        </div>

        <!-- Enhanced Filter and Sort Controls -->
        <Card class="mb-8 shadow-lg border-0 bg-white">
          <CardContent class="p-8">
            <div class="flex flex-col lg:flex-row gap-6 items-start lg:items-center justify-between">
              <div class="flex flex-col sm:flex-row items-start sm:items-center gap-6">
                <div class="flex items-center gap-3">
                  <div class="w-2 h-8 bg-custom-primary rounded-full"></div>
                  <Label class="text-xl font-bold text-foreground whitespace-nowrap">Filter & Sort</Label>
                </div>
                <Select v-model="sortBy">
                  <SelectTrigger class="w-full sm:w-80 h-14 text-lg border-2 border-border focus:border-custom-primary focus:ring-2 focus:ring-custom-primary/20 transition-all rounded-xl">
                    <SelectValue placeholder="Select sort option" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="created_at">📅 Latest First</SelectItem>
                    <SelectItem value="title">🔤 Title (A-Z)</SelectItem>
                    <SelectItem value="oldest_first">⏰ Oldest First</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              
              <div class="flex items-center gap-4">
                <Badge class="bg-gradient-to-r from-custom-primary to-primary-700 text-white text-lg font-bold px-6 py-3 rounded-full shadow-lg">
                  {{ ideas.length }} {{ ideas.length === 1 ? 'Idea' : 'Ideas' }}
                </Badge>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Ideas List -->
        <div class="space-y-8">
          <div class="flex items-center gap-3 mb-6">
            <div class="w-3 h-8 bg-gradient-to-b from-custom-primary to-primary-700 rounded-full"></div>
            <h2 class="text-2xl font-bold text-foreground">Submitted Ideas</h2>
          </div>
          <div class="space-y-6">
            <IdeaCard 
              v-for="(idea, idx) in sortedIdeas" 
              :key="idea.id || idx" 
              :idea="idea" 
              layout="list"
              class="hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-1 border-0 shadow-lg bg-white"
            />
          </div>
        </div>
      </div>
      </div>
    </main>
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
