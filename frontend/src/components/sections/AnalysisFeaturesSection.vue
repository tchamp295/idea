<template>
  <section class="py-16">
    <div class="text-center mb-12">
      <h3 class="text-3xl lg:text-4xl font-bold mb-4">
        How Our <span class="text-ai-accent">AI Analyzes</span> Your Idea
      </h3>
      <p class="text-lg text-muted-foreground max-w-2xl mx-auto">
        Advanced algorithms provide comprehensive feedback in seconds using cutting-edge machine learning
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <Card 
        v-for="feature in analysisFeatures" 
        :key="feature.id"
        class="text-center border-0 bg-card/50 backdrop-blur-sm hover:shadow-xl hover:scale-105 transition-all duration-300 cursor-pointer group"
        :class="feature.hoverEffect"
      >
        <CardContent class="p-8">
          <div class="w-16 h-16 mx-auto mb-6 rounded-2xl flex items-center justify-center transition-all duration-300" 
               :class="[feature.iconBg, 'group-hover:scale-110 group-hover:shadow-lg']">
            <component :is="feature.icon" class="w-8 h-8 transition-colors duration-300" :class="feature.iconColor" />
          </div>
          
          <h4 class="font-bold text-lg mb-3" :class="feature.titleColor">{{ feature.title }}</h4>
          <p class="text-sm text-muted-foreground leading-relaxed">{{ feature.description }}</p>
          
          <div class="mt-4 flex items-center justify-center">
            <Badge variant="secondary" class="text-xs font-medium" :class="feature.badgeColor">
              {{ feature.metric }}
            </Badge>
          </div>
        </CardContent>
      </Card>
    </div>

  </section>
</template>

<script setup lang="ts">
import Card from '@/components/ui/card/Card.vue'
import CardContent from '@/components/ui/card/CardContent.vue'
import Badge from '@/components/ui/badge/Badge.vue'
import { h } from 'vue'

const analysisFeatures = [
  {
    id: 1,
    title: 'Impact Score',
    description: 'Measures potential market impact, innovation value, and societal benefits using advanced impact modeling',
    metric: '95% Accuracy',
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
        d: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' 
      })
    ]),
    iconBg: 'bg-primary/10',
    iconColor: 'text-primary',
    titleColor: 'text-primary',
    badgeColor: 'bg-primary/10 text-primary',
    hoverEffect: 'hover:border-primary/20 hover:bg-primary/5'
  },
  {
    id: 2,
    title: 'Feasibility Analysis',
    description: 'Analyzes technical requirements, resource needs, timeline estimates, and implementation challenges',
    metric: '12 Factors',
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
        d: 'M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4' 
      })
    ]),
    iconBg: 'bg-secondary-600/10',
    iconColor: 'text-secondary-600',
    titleColor: 'text-secondary-600',
    badgeColor: 'bg-secondary-600/10 text-secondary-600',
    hoverEffect: 'hover:border-secondary-600/20 hover:bg-secondary-600/5'
  },
  {
    id: 3,
    title: 'Deep Funding Alignment',
    description: 'Evaluates alignment with Deep Funding objectives, community needs, and decentralization principles',
    metric: '8 Criteria',
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
        d: 'M13 7h8m0 0v8m0-8l-8 8-4-4-6 6' 
      })
    ]),
    iconBg: 'bg-success-500/10',
    iconColor: 'text-success-600',
    titleColor: 'text-success-600',
    badgeColor: 'bg-success-500/10 text-success-600',
    hoverEffect: 'hover:border-success-500/20 hover:bg-success-500/5'
  },
  {
    id: 4,
    title: 'Duplicate Detection',
    description: 'Advanced similarity detection identifies existing proposals and suggests differentiation strategies',
    metric: '1000+ Ideas',
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
        d: 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z' 
      })
    ]),
    iconBg: 'bg-ai-accent/10',
    iconColor: 'text-ai-accent',
    titleColor: 'text-ai-accent',
    badgeColor: 'bg-ai-accent/10 text-ai-accent',
    hoverEffect: 'hover:border-ai-accent/20 hover:bg-ai-accent/5'
  }
]

</script>