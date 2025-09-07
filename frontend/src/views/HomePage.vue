<template>
  <div class="min-h-screen">
    <!-- Enhanced Background -->
    <div class="fixed inset-0 -z-10">
      <!-- Base gradient -->
      <div class="absolute inset-0 bg-gradient-to-br from-primary/5 via-transparent to-ai-accent/5"></div>
      
      <!-- Neural network pattern -->
      <div 
        class="absolute inset-0 opacity-20" 
        style="background-image: radial-gradient(circle at 1px 1px, rgba(79, 70, 229, 0.15) 1px, transparent 0); background-size: 24px 24px;"
      ></div>
      
      <!-- Floating particles -->
      <div class="absolute inset-0">
        <div class="absolute top-20 left-10 w-2 h-2 bg-ai-accent/30 rounded-full animate-pulse"></div>
        <div class="absolute top-40 right-20 w-1 h-1 bg-primary/40 rounded-full animate-pulse" style="animation-delay: 1s"></div>
        <div class="absolute bottom-32 left-1/4 w-1.5 h-1.5 bg-secondary-500/30 rounded-full animate-pulse" style="animation-delay: 2s"></div>
        <div class="absolute bottom-20 right-1/3 w-1 h-1 bg-ai-accent/40 rounded-full animate-pulse" style="animation-delay: 0.5s"></div>
      </div>
    </div>

    <div class="relative z-10">
      <!-- Container with proper spacing -->
      <div class="container mx-auto px-4 py-8 space-y-16">
        
        <!-- Hero Section -->
        <HeroSection />
        
        <!-- Stats Section -->
        <StatsSection />
        
        <!-- Idea Submission Form -->
        <IdeaSubmissionForm />
        
        <!-- Analysis Features -->
        <AnalysisFeaturesSection />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import HeroSection from '@/components/sections/HeroSection.vue'
import StatsSection from '@/components/sections/StatsSection.vue'
import IdeaSubmissionForm from '@/components/forms/IdeaSubmissionForm.vue'
import AnalysisFeaturesSection from '@/components/sections/AnalysisFeaturesSection.vue'
import Button from '@/components/ui/button/Button.vue'
</script>