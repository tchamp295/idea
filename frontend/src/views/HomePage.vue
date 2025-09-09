<template>
  <!-- Clean Hero Section with Brand Colors -->
  <section class="min-h-screen flex items-center justify-center py-20 bg-custom-light">
    <div class="max-w-6xl mx-auto px-6 sm:px-8 lg:px-12 text-center">
      <h1 class="text-5xl sm:text-6xl lg:text-7xl font-bold mb-8 leading-tight">
        <span class="text-foreground tracking-tight">Share Your Next</span>
        <br>
        <span class="text-custom-primary font-extrabold tracking-wide animate-glow">
          Big Idea
        </span>
      </h1>
      
      <p class="text-xl sm:text-2xl mb-12 max-w-4xl mx-auto leading-relaxed text-muted-foreground font-medium">
        Our community and AI tools will evaluate your proposal for 
        <span class="text-custom-primary font-bold">impact</span>, 
        <span class="text-custom-primary font-bold">feasibility</span>, and 
        <span class="text-custom-primary font-bold">alignment</span> with our mission.
        <br>
        <span class="text-custom-secondary">Join us in driving innovation and making a difference!</span>
      </p>
      
      <div class="flex justify-center">
        <Button 
          @click="$router.push('/submit')"
          class="bg-custom-primary hover-primary text-white font-bold min-w-[240px] h-16 px-10 text-xl rounded-full shadow-xl hover:shadow-2xl transform hover:scale-105 hover:-translate-y-1 transition-all duration-300 border-0 relative overflow-hidden group"
        >
          <span class="relative z-10 flex items-center justify-center">
            <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
            Submit Your Idea
          </span>
          <div class="absolute inset-0 bg-accent-primary/20 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"></div>
        </Button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>