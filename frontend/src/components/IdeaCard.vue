<template>
  <Card class="hover:shadow-lg transition-all duration-200">
    <CardContent class="p-6">
      <!-- Header -->
      <div class="flex items-start justify-between mb-4">
        <div class="flex-1">
          <CardTitle class="text-lg mb-2 leading-tight">
            {{ idea.title || 'Untitled Idea' }}
          </CardTitle>
          <div class="flex items-center gap-2 text-sm text-muted-foreground">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3a4 4 0 118 0v4a4 4 0 118 0v4a4 4 0 11-8 0V7z" />
            </svg>
            {{ formatDate(idea.created_at) }}
          </div>
        </div>
        <Badge variant="secondary" class="ml-4">
          {{ idea.id ? `#${idea.id.slice(-6)}` : 'Draft' }}
        </Badge>
      </div>

      <!-- Description -->
      <CardDescription class="text-base leading-relaxed mb-4 text-foreground">
        {{ idea.description || 'No description provided.' }}
      </CardDescription>

      <!-- File Attachment -->
      <div v-if="idea.file_url" class="flex items-center gap-2 pt-4 border-t">
        <Button 
          variant="outline" 
          size="sm"
          @click="openFile"
        >
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
          </svg>
          View Attachment
        </Button>
      </div>

      <!-- Admin Actions -->
      <div v-if="layout === 'list'" class="flex items-center justify-between pt-4 border-t">
        <div class="text-sm text-muted-foreground">
          Submitted {{ formatRelativeDate(idea.created_at) }}
        </div>
        <div class="flex items-center gap-2">
          <Button variant="ghost" size="sm">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
            View Details
          </Button>
        </div>
      </div>
    </CardContent>
  </Card>
</template>

<script setup lang="ts">
import type { Idea } from '../services/api'
import { Card, CardContent, CardDescription, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'

interface Props {
  idea: Idea
  layout?: 'card' | 'list'
}

const props = withDefaults(defineProps<Props>(), {
  layout: 'card'
})

const formatDate = (dateString?: string) => {
  if (!dateString) return 'Unknown'
  try {
    return new Date(dateString).toLocaleDateString('en-US', { 
      month: 'short', 
      day: 'numeric',
      year: 'numeric'
    })
  } catch {
    return 'Unknown'
  }
}

const formatRelativeDate = (dateString?: string) => {
  if (!dateString) return 'unknown time'
  try {
    const date = new Date(dateString)
    const now = new Date()
    const diff = now.getTime() - date.getTime()
    const days = Math.floor(diff / (1000 * 60 * 60 * 24))
    
    if (days === 0) return 'today'
    if (days === 1) return 'yesterday'
    if (days < 7) return `${days} days ago`
    if (days < 30) return `${Math.floor(days / 7)} weeks ago`
    return `${Math.floor(days / 30)} months ago`
  } catch {
    return 'unknown time'
  }
}

const openFile = () => {
  if (props.idea.file_url) {
    window.open(`http://127.0.0.1:8000${props.idea.file_url}`, '_blank')
  }
}
</script>
