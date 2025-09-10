<template>

  <!-- Loading State -->
  <div v-if="loading" class="flex items-center justify-center py-20">
    <Card class="max-w-md mx-auto">
      <CardContent class="p-8 text-center">
        <div class="w-20 h-20 border-4 border-custom-primary border-t-transparent rounded-full animate-spin mx-auto mb-6"></div>
        <h3 class="text-xl font-semibold text-foreground mb-2">Loading Ideas</h3>
        <p class="text-muted-foreground">Fetching all submitted ideas...</p>
      </CardContent>
    </Card>
  </div>

  <!-- Ideas List -->
  <div v-else>
    <div class="flex items-center gap-3 mb-6">
      <div class="w-3 h-8 bg-gradient-to-b from-custom-primary to-primary-700 rounded-full"></div>
      <h2 class="text-2xl font-bold text-foreground">All Ideas</h2>
      <Badge variant="secondary" class="ml-auto">{{ ideas.length }} total</Badge>
    </div>

    <!-- Sort Controls -->
    <div class="mb-6 flex flex-wrap gap-4 items-center">
      <Label for="sort-select" class="text-sm font-medium">Sort by:</Label>
      <Select v-model="sortBy" @update:modelValue="sortIdeas">
        <SelectTrigger id="sort-select" class="w-48">
          <SelectValue placeholder="Select sorting option" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="created_at">Newest First</SelectItem>
          <SelectItem value="oldest_first">Oldest First</SelectItem>
          <SelectItem value="title">Title A-Z</SelectItem>
        </SelectContent>
      </Select>
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
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import IdeaCard from '../components/IdeaCard.vue'
import { fetchIdeas } from '../services/api'
import type { Idea } from '../types'
import { useRouter } from 'vue-router'
import { Card, CardContent, Badge, Label, Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../components/ui'

const ideas = ref<Idea[]>([])
const loading = ref(true)
const sortBy = ref('created_at')
const router = useRouter()

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