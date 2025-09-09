<template>
  <section class="py-16 bg-gradient-to-br from-neutral-50 to-primary-50 lg:py-24">
    <div class="text-center max-w-4xl mx-auto px-4">
      <h1 class="text-4xl lg:text-6xl font-bold mb-6">
        <span class="bg-gradient-to-r from-primary-600 to-primary-700 bg-clip-text text-transparent font-extrabold">
          Transform Your Ideas
        </span>
        <br>
        <span class="text-neutral-900 dark:text-neutral-100">Into Reality</span>
      </h1>
      
      <p class="text-xl lg:text-2xl text-neutral-700 dark:text-neutral-300 max-w-3xl mx-auto leading-relaxed mb-8">
        Submit your innovative ideas and let our AI analyze impact, feasibility, and alignment with 
        <span class="text-primary-700 dark:text-primary-400 font-semibold">Deep Funding</span> goals. 
        Get instant feedback and join the future of decentralized innovation.
      </p>

      <div class="flex justify-center">
        <Button size="lg" class="bg-primary-gradient hover:shadow-xl transition-all duration-300 text-white px-8 py-6 text-lg font-semibold shadow-lg hover:scale-105">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
          Start Analyzing
        </Button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import Button from '@/components/ui/button/Button.vue'
</script>