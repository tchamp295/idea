<template>
  <div class="min-h-screen w-full max-w-none px-4 py-8">
    <!-- Header Section -->
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-secondary/10 text-secondary-700 text-sm font-medium mb-4">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
        AI-Analyzed Ideas
      </div>
      
      <h1 class="text-display-md font-bold mb-4">
        Innovation <span class="bg-ai-gradient bg-clip-text text-transparent">Dashboard</span>
      </h1>
      
      <p class="text-xl text-muted-foreground max-w-5xl mx-auto mb-8">
        Discover cutting-edge ideas analyzed by our AI system. Each submission is scored for impact, feasibility, and alignment with Deep Funding goals.
      </p>

      <!-- Action Bar -->
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <Button 
          size="lg"
          @click="$router.push('/')"
        >
          <template #icon>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
          </template>
          Submit New Idea
        </Button>

        <!-- Filter/Sort Controls -->
        <div class="flex items-center gap-2">
          <select 
            v-model="sortBy" 
            @change="sortIdeas"
            class="px-4 py-2 border border-border rounded-lg bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-primary"
          >
            <option value="created_at">Latest First</option>
            <option value="impact_score">Impact Score</option>
            <option value="feasibility_score">Feasibility</option>
            <option value="alignment_score">Alignment</option>
            <option value="overall_score">Overall Score</option>
          </select>

          <button 
            @click="toggleLayout"
            class="p-2 border border-border rounded-lg hover:bg-accent transition-all"
            :title="isGridView ? 'Switch to List View' : 'Switch to Grid View'"
          >
            <svg v-if="isGridView" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" />
            </svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Content Area -->
    <div v-if="loading" class="flex items-center justify-center py-20">
      <div class="text-center">
        <div class="w-16 h-16 border-4 border-primary border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-muted-foreground">Loading AI-analyzed ideas...</p>
      </div>
    </div>

    <div v-else-if="ideas.length === 0" class="text-center py-20">
      <div class="w-24 h-24 bg-muted rounded-full flex items-center justify-center mx-auto mb-6">
        <svg class="w-12 h-12 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364-.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>
      </div>
      <h3 class="text-xl font-semibold mb-2">No Ideas Yet</h3>
      <p class="text-muted-foreground mb-6">Be the first to submit an innovative idea for AI analysis!</p>
      <Button 
        size="lg"
        @click="$router.push('/')"
      >
        <template #icon>
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
        </template>
        Submit Your First Idea
      </Button>
    </div>

    <!-- Ideas Grid/List -->
    <div v-else>
      <!-- Stats Summary -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <Card class="hover:shadow-lg transition-all">
          <CardContent class="p-6 text-center">
            <div class="text-2xl font-bold text-primary mb-1">{{ ideas.length }}</div>
            <div class="text-sm text-muted-foreground">Total Ideas</div>
          </CardContent>
        </Card>
        <Card class="hover:shadow-lg transition-all">
          <CardContent class="p-6 text-center">
            <div class="text-2xl font-bold text-success-600 mb-1">{{ highImpactCount }}</div>
            <div class="text-sm text-muted-foreground">High Impact</div>
          </CardContent>
        </Card>
        <Card class="hover:shadow-lg transition-all">
          <CardContent class="p-6 text-center">
            <div class="text-2xl font-bold text-secondary-600 mb-1">{{ averageScore.toFixed(1) }}</div>
            <div class="text-sm text-muted-foreground">Avg Score</div>
          </CardContent>
        </Card>
        <Card class="hover:shadow-lg transition-all">
          <CardContent class="p-6 text-center">
            <div class="text-2xl font-bold text-warning-600 mb-1">{{ duplicateCount }}</div>
            <div class="text-sm text-muted-foreground">Duplicates Found</div>
          </CardContent>
        </Card>
      </div>

      <!-- Ideas Container -->
      <div :class="isGridView ? 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6' : 'space-y-6'">
        <IdeaCard 
          v-for="(idea, idx) in sortedIdeas" 
          :key="idea.id || idx" 
          :idea="idea" 
          :layout="isGridView ? 'grid' : 'list'"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { fetchIdeas } from '../services/api'
import { useRouter } from 'vue-router'
import { Button, Card, CardContent } from './ui'
import IdeaCard from './IdeaCard.vue'

const router = useRouter()
const ideas = ref<Idea[]>([])
const loading = ref(true)
const sortBy = ref('created_at')
const isGridView = ref(true)

// Computed properties for stats
interface Idea {
  id?: string
  created_at?: string
  impact_score?: number
  feasibility_score?: number
  alignment_score?: number
  overall_score?: number
  is_duplicate?: boolean
  // Add other fields as needed
}

const highImpactCount = computed(() => {
  return ideas.value.filter((idea: Idea) => (idea.impact_score || 0) > 7).length
})


const averageScore = computed(() => {
  const scores = ideas.value.map(idea => idea.overall_score || 0)
  if (scores.length === 0) return 0
  return scores.reduce((a, b) => a + b, 0) / scores.length
})

const duplicateCount = computed(() => {
  return ideas.value.filter(idea => idea.is_duplicate).length
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
      return sorted.sort((a, b) => (b.overall_score || 0) - (a.overall_score || 0))
    case 'created_at':
    default:
      return sorted.sort((a, b) => new Date(b.created_at || 0).getTime() - new Date(a.created_at || 0).getTime())
  }
})

const sortIdeas = () => {
  // Trigger reactivity - sortedIdeas computed will handle the actual sorting
}

const toggleLayout = () => {
  isGridView.value = !isGridView.value
}

onMounted(async () => {
  try {
    const res = await fetchIdeas()
    ideas.value = res.data || []
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>
