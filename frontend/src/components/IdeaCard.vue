<template>
  <Card 
    :variant="idea.is_duplicate ? 'outline' : 'default'"
    :hover="true"
    :glow="overallScore >= 8"
    :padding="layout === 'list' ? 'lg' : 'md'"
    :class="[
      layout === 'list' ? 'flex items-start gap-6' : '',
      idea.is_duplicate ? 'border-warning-200 bg-warning-50/50' : '',
      overallScore >= 8 ? 'ring-2 ring-success-200 bg-success-50/30' : '',
      overallScore >= 7 ? 'ring-1 ring-primary-200 bg-primary-50/20' : ''
    ]"
  >
    <!-- Card Content -->
    <div :class="layout === 'list' ? 'flex-1' : ''">
      <!-- Header with badges -->
      <div class="flex items-start justify-between mb-4">
        <div class="flex-1">
          <div class="flex items-center gap-2 mb-2">
            <!-- AI Processing Badge -->
            <Badge variant="primary" size="sm" dot>
              AI Analyzed
            </Badge>
            
            <!-- Duplicate Badge -->
            <Badge v-if="idea.is_duplicate" variant="warning" size="sm">
              <template #icon>
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.664-.833-2.464 0L4.35 16.5c-.77.833.192 2.5 1.732 2.5z" />
                </svg>
              </template>
              Similar Found
            </Badge>
            
            <!-- High Impact Badge -->
            <Badge v-if="overallScore >= 8" variant="success" size="sm">
              <template #icon>
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </template>
              High Impact
            </Badge>
          </div>
          
          <h3 class="text-xl font-bold text-foreground mb-2 group-hover:text-primary transition-colors">
            {{ idea.title || 'Untitled Idea' }}
          </h3>
        </div>
        
        <!-- Submission Date -->
        <div class="text-xs text-muted-foreground ml-4">
          {{ formatDate(idea.created_at) }}
        </div>
      </div>

      <!-- Description -->
      <p class="text-muted-foreground mb-6 line-clamp-3 leading-relaxed">
        {{ idea.description }}
      </p>

      <!-- AI Analysis Scores -->
      <div class="mb-6">
        <div class="flex items-center justify-between mb-3">
          <h4 class="text-sm font-semibold text-foreground">AI Analysis</h4>
          <div class="text-2xl font-bold text-primary">
            {{ overallScore.toFixed(1) }}
          </div>
        </div>
        
        <div class="grid grid-cols-3 gap-4">
          <!-- Impact Score -->
          <div>
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs text-muted-foreground">Impact</span>
              <span class="text-sm font-medium">{{ (idea.impact_score || 0).toFixed(1) }}</span>
            </div>
            <div class="w-full bg-muted rounded-full h-2">
              <div 
                class="h-2 rounded-full transition-all duration-500"
                :class="getScoreColor(idea.impact_score || 0)"
                :style="{ width: `${Math.min((idea.impact_score || 0) * 10, 100)}%` }"
              ></div>
            </div>
          </div>

          <!-- Feasibility Score -->
          <div>
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs text-muted-foreground">Feasibility</span>
              <span class="text-sm font-medium">{{ (idea.feasibility_score || 0).toFixed(1) }}</span>
            </div>
            <div class="w-full bg-muted rounded-full h-2">
              <div 
                class="h-2 rounded-full transition-all duration-500"
                :class="getScoreColor(idea.feasibility_score || 0)"
                :style="{ width: `${Math.min((idea.feasibility_score || 0) * 10, 100)}%` }"
              ></div>
            </div>
          </div>

          <!-- Alignment Score -->
          <div>
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs text-muted-foreground">Alignment</span>
              <span class="text-sm font-medium">{{ (idea.alignment_score || 0).toFixed(1) }}</span>
            </div>
            <div class="w-full bg-muted rounded-full h-2">
              <div 
                class="h-2 rounded-full transition-all duration-500"
                :class="getScoreColor(idea.alignment_score || 0)"
                :style="{ width: `${Math.min((idea.alignment_score || 0) * 10, 100)}%` }"
              ></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Categories -->
      <div v-if="idea.category" class="mb-6">
        <div class="flex flex-wrap gap-2">
          <div class="px-3 py-1 bg-secondary/10 text-secondary-700 rounded-full text-xs font-medium">
            {{ idea.category }}
          </div>
          <div v-if="idea.subcategory" class="px-3 py-1 bg-muted text-muted-foreground rounded-full text-xs">
            {{ idea.subcategory }}
          </div>
        </div>
      </div>

      <!-- Footer Actions -->
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <!-- File Attachment -->
          <a 
            v-if="idea.file_url" 
            :href="idea.file_url" 
            target="_blank"
            class="inline-flex items-center gap-1 px-3 py-1 text-xs font-medium text-primary hover:bg-primary/10 rounded-lg transition-all"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
            </svg>
            View Document
          </a>

          <!-- Similar Ideas Link -->
          <button 
            v-if="idea.similar_ideas && idea.similar_ideas.length > 0"
            @click="showSimilarIdeas = !showSimilarIdeas"
            class="inline-flex items-center gap-1 px-3 py-1 text-xs font-medium text-warning-600 hover:bg-warning-50 rounded-lg transition-all"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" />
            </svg>
            {{ idea.similar_ideas.length }} Similar
          </button>
        </div>

        <!-- View Details Button -->
        <Button variant="ghost" size="sm" @click="showDetails = !showDetails">
          {{ showDetails ? 'Hide' : 'View' }} Details
          <template #icon>
            <svg 
              class="w-4 h-4 transition-transform"
              :class="showDetails ? 'rotate-180' : ''"
              fill="none" stroke="currentColor" viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </template>
        </Button>
      </div>
    </div>

    <!-- AI Score Visualization (Grid Only) -->
    <div v-if="layout === 'grid'" class="mt-6 p-4 bg-muted/30 rounded-xl">
      <div class="text-center">
        <div 
          class="w-20 h-20 mx-auto rounded-full border-4 flex items-center justify-center text-2xl font-bold"
          :class="overallScore >= 8 ? 'border-success-500 text-success-700 bg-success-50' : 
                  overallScore >= 7 ? 'border-primary text-primary bg-primary/10' :
                  overallScore >= 5 ? 'border-warning-500 text-warning-700 bg-warning-50' :
                  'border-muted-foreground text-muted-foreground'"
        >
          {{ overallScore.toFixed(1) }}
        </div>
        <div class="text-xs text-muted-foreground mt-2">Overall Score</div>
      </div>
    </div>

    <!-- Expandable Details -->
    <div v-if="showDetails" class="mt-6 pt-6 border-t border-border">
      <div class="space-y-4">
        <!-- AI Feedback -->
        <div v-if="idea.feedback">
          <h5 class="text-sm font-semibold text-foreground mb-2">AI Feedback</h5>
          <p class="text-sm text-muted-foreground bg-muted/50 p-3 rounded-lg">
            {{ idea.feedback }}
          </p>
        </div>

        <!-- Similar Ideas -->
        <div v-if="showSimilarIdeas && idea.similar_ideas && idea.similar_ideas.length > 0">
          <h5 class="text-sm font-semibold text-foreground mb-2">Similar Ideas Found</h5>
          <div class="space-y-2">
            <div 
              v-for="similar in idea.similar_ideas.slice(0, 3)" 
              :key="similar.id"
              class="p-3 bg-warning-50 border border-warning-200 rounded-lg"
            >
              <div class="flex items-center justify-between">
                <span class="text-sm font-medium text-warning-800">{{ similar.title }}</span>
                <span class="text-xs text-warning-600">{{ (similar.similarity * 100).toFixed(0) }}% match</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Processing Status -->
        <div class="flex items-center justify-between text-xs text-muted-foreground">
          <span>Processed: {{ formatDate(idea.created_at) }}</span>
          <span class="flex items-center gap-1">
            <div class="w-2 h-2 rounded-full bg-success-500"></div>
            Analysis Complete
          </span>
        </div>
      </div>
    </div>
  </Card>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import type { Idea } from '../services/api'
import { Button, Card, Badge } from './ui'

interface Props {
  idea: Idea
  layout?: 'grid' | 'list'
}

const props = withDefaults(defineProps<Props>(), {
  layout: 'grid'
})

const showDetails = ref(false)
const showSimilarIdeas = ref(false)

// Computed properties
const overallScore = computed(() => {
  const impact = props.idea.impact_score || 0
  const feasibility = props.idea.feasibility_score || 0
  const alignment = props.idea.alignment_score || 0
  return (impact + feasibility + alignment) / 3
})

const getScoreColor = (score: number) => {
  if (score >= 8) return 'bg-success-500'
  if (score >= 7) return 'bg-primary'
  if (score >= 5) return 'bg-warning-500'
  return 'bg-muted-foreground'
}

const formatDate = (dateString: string) => {
  if (!dateString) return 'Unknown'
  
  const date = new Date(dateString)
  const now = new Date()
  const diffTime = Math.abs(now.getTime() - date.getTime())
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  
  if (diffDays === 1) return 'Yesterday'
  if (diffDays <= 7) return `${diffDays} days ago`
  if (diffDays <= 30) return `${Math.ceil(diffDays / 7)} weeks ago`
  
  return date.toLocaleDateString('en-US', { 
    month: 'short', 
    day: 'numeric', 
    year: date.getFullYear() !== now.getFullYear() ? 'numeric' : undefined 
  })
}
</script>
