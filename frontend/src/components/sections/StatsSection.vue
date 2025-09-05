<template>
  <section class="py-12">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
      <Card 
        v-for="stat in stats" 
        :key="stat.id"
        class="hover:shadow-lg transition-all duration-300 cursor-pointer border-0 bg-card/50 backdrop-blur-sm"
        :class="stat.highlight"
      >
        <CardContent class="pt-8 pb-6">
          <div class="text-center">
            <div class="w-16 h-16 mx-auto mb-4 rounded-2xl flex items-center justify-center" :class="stat.iconBg">
              <component :is="stat.icon" class="w-8 h-8" :class="stat.iconColor" />
            </div>
            <div class="text-3xl font-bold mb-2" :class="stat.valueColor">
              {{ stat.value }}
            </div>
            <div class="text-sm text-muted-foreground font-medium">
              {{ stat.label }}
            </div>
            <div class="text-xs text-muted-foreground mt-1">
              {{ stat.description }}
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  </section>
</template>

<script setup lang="ts">
import Card from '@/components/ui/card/Card.vue'
import CardContent from '@/components/ui/card/CardContent.vue'
import { h } from 'vue'

const stats = [
  {
    id: 1,
    value: '95%',
    label: 'Accuracy Rate',
    description: 'AI Analysis Precision',
    icon: h('svg', { 
      fill: 'none', 
      stroke: 'currentColor', 
      viewBox: '0 0 24 24',
      class: 'w-8 h-8'
    }, [
      h('path', { 
        'stroke-linecap': 'round', 
        'stroke-linejoin': 'round', 
        'stroke-width': '2', 
        d: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z' 
      })
    ]),
    iconBg: 'bg-success-500/10',
    iconColor: 'text-success-600',
    valueColor: 'text-success-600',
    highlight: 'hover:border-success-500/20'
  },
  {
    id: 2,
    value: '< 2s',
    label: 'Processing Time',
    description: 'Lightning Fast Analysis',
    icon: h('svg', { 
      fill: 'none', 
      stroke: 'currentColor', 
      viewBox: '0 0 24 24',
      class: 'w-8 h-8'
    }, [
      h('path', { 
        'stroke-linecap': 'round', 
        'stroke-linejoin': 'round', 
        'stroke-width': '2', 
        d: 'M13 10V3L4 14h7v7l9-11h-7z' 
      })
    ]),
    iconBg: 'bg-ai-accent/10',
    iconColor: 'text-ai-accent',
    valueColor: 'text-ai-accent',
    highlight: 'hover:border-ai-accent/20'
  },
  {
    id: 3,
    value: '1,247',
    label: 'Ideas Processed',
    description: 'Growing Community',
    icon: h('svg', { 
      fill: 'none', 
      stroke: 'currentColor', 
      viewBox: '0 0 24 24',
      class: 'w-8 h-8'
    }, [
      h('path', { 
        'stroke-linecap': 'round', 
        'stroke-linejoin': 'round', 
        'stroke-width': '2', 
        d: 'M9.663 17h4.673M12 3v1m6.364-.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z' 
      })
    ]),
    iconBg: 'bg-primary/10',
    iconColor: 'text-primary',
    valueColor: 'text-primary',
    highlight: 'hover:border-primary/20'
  }
]
</script>