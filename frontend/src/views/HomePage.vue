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
        
        <!-- Call to Action Footer -->
        <section class="py-16 text-center">
          <div class="max-w-3xl mx-auto">
            <div class="p-8 bg-card/60 backdrop-blur-sm rounded-3xl border">
              <h3 class="text-2xl lg:text-3xl font-bold mb-4">
                Ready to Transform Your Idea?
              </h3>
              <p class="text-muted-foreground mb-6 text-lg">
                Join thousands of innovators who trust our AI to evaluate their groundbreaking concepts
              </p>
              <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" class="bg-ai-gradient hover:opacity-90 text-white px-8 py-6 text-lg font-semibold">
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                  Get Started Now
                </Button>
                <Button variant="outline" size="lg" class="px-8 py-6 text-lg border-2" @click="$router.push('/ideas')">
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                  Browse Ideas
                </Button>
              </div>
            </div>
          </div>
        </section>
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