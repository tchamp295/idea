<template>
  <div class="min-h-screen w-full max-w-none px-4 py-8">
    <!-- Header Section -->
    <div class="flex flex-col md:flex-row items-start md:items-center justify-between mb-8">
      <div>
        <div class="flex items-center gap-2 mb-2">
          <Badge variant="secondary" class="text-xs">
            <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.031 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
            Admin Panel
          </Badge>
        </div>
        <h1 class="text-display-md font-bold mb-2">
          Idea <span class="bg-ai-gradient bg-clip-text text-transparent">Management</span>
        </h1>
        <p class="text-muted-foreground max-w-2xl">
          Review and manage AI-analyzed ideas submitted to the Deep Funding platform.
        </p>
      </div>
      
      <div class="flex items-center gap-3 mt-4 md:mt-0">
        <Button variant="outline" size="sm" @click="load">
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Refresh
        </Button>
        <Button variant="destructive" size="sm" @click="logout">
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          Logout
        </Button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-20">
      <div class="text-center">
        <div class="w-16 h-16 border-4 border-primary border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-muted-foreground">Loading submitted ideas...</p>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else-if="ideas.length === 0" class="text-center py-20">
      <div class="w-24 h-24 bg-muted rounded-full flex items-center justify-center mx-auto mb-6">
        <svg class="w-12 h-12 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
        </svg>
      </div>
      <h3 class="text-xl font-semibold mb-2">No Ideas Submitted Yet</h3>
      <p class="text-muted-foreground mb-6">When users submit ideas, they will appear here for review.</p>
    </div>

    <!-- Ideas Dashboard -->
    <div v-else>
      <!-- Statistics Cards -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <Card class="hover:shadow-lg transition-all">
          <CardContent class="p-6 text-center">
            <div class="text-2xl font-bold text-primary mb-1">{{ ideas.length }}</div>
            <div class="text-sm text-muted-foreground">Total Submissions</div>
          </CardContent>
        </Card>
        <Card class="hover:shadow-lg transition-all">
          <CardContent class="p-6 text-center">
            <div class="text-2xl font-bold text-ai-accent mb-1">{{ highImpactCount }}</div>
            <div class="text-sm text-muted-foreground">High Impact Ideas</div>
          </CardContent>
        </Card>
        <Card class="hover:shadow-lg transition-all">
          <CardContent class="p-6 text-center">
            <div class="text-2xl font-bold text-ai-highlight mb-1">{{ duplicateCount }}</div>
            <div class="text-sm text-muted-foreground">Duplicates Detected</div>
          </CardContent>
        </Card>
        <Card class="hover:shadow-lg transition-all">
          <CardContent class="p-6 text-center">
            <div class="text-2xl font-bold text-ai-neural mb-1">{{ averageScore.toFixed(1) }}</div>
            <div class="text-sm text-muted-foreground">Average Score</div>
          </CardContent>
        </Card>
      </div>

      <!-- Filter and Sort Controls -->
      <Card class="mb-6">
        <CardContent class="p-4">
          <div class="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
            <div class="flex items-center gap-2">
              <Label class="text-sm font-medium">Sort by:</Label>
              <Select v-model="sortBy">
                <SelectTrigger class="w-48">
                  <SelectValue placeholder="Select sort option" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="created_at">Latest First</SelectItem>
                  <SelectItem value="impact_score">Impact Score</SelectItem>
                  <SelectItem value="feasibility_score">Feasibility</SelectItem>
                  <SelectItem value="alignment_score">Alignment</SelectItem>
                  <SelectItem value="overall_score">Overall Score</SelectItem>
                </SelectContent>
              </Select>
            </div>
            
            <div class="flex items-center gap-2">
              <Badge variant="outline" class="text-xs">
                Showing {{ ideas.length }} ideas
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
        />
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
const highImpactCount = computed(() => {
  return ideas.value.filter(idea => (idea.impact_score || 0) > 7).length
})

const duplicateCount = computed(() => {
  return ideas.value.filter(idea => idea.is_duplicate).length
})

const averageScore = computed(() => {
  const scores = ideas.value.map(idea => {
    const impact = idea.impact_score || 0
    const feasibility = idea.feasibility_score || 0
    const alignment = idea.alignment_score || 0
    return (impact + feasibility + alignment) / 3
  })
  if (scores.length === 0) return 0
  return scores.reduce((a, b) => a + b, 0) / scores.length
})

// Sorted ideas based on current sort option
const sortedIdeas = computed(() => {
  const sorted = [...ideas.value]
  
  switch (sortBy.value) {
    case 'impact_score':
      return sorted.sort((a, b) => (b.impact_score || 0) - (a.impact_score || 0))
    case 'feasibility_score':
      return sorted.sort((a, b) => (b.feasibility_score || 0) - (a.feasibility_score || 0))
    case 'alignment_score':
      return sorted.sort((a, b) => (b.alignment_score || 0) - (a.alignment_score || 0))
    case 'overall_score':
      return sorted.sort((a, b) => {
        const aScore = ((a.impact_score || 0) + (a.feasibility_score || 0) + (a.alignment_score || 0)) / 3
        const bScore = ((b.impact_score || 0) + (b.feasibility_score || 0) + (b.alignment_score || 0)) / 3
        return bScore - aScore
      })
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
    router.push('/admin/login')
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
  router.push('/admin/login')
}

onMounted(load)
</script>
