<template>
  <section class="bg-custom-light min-h-screen py-20">
    <div class="max-w-5xl mx-auto px-6 sm:px-8 lg:px-12">
      <div class="text-center mb-16">
        <h1 class="text-5xl sm:text-6xl font-bold mb-6">
          <span class="text-foreground">Submit Your</span>
          <br>
          <span class="text-custom-primary font-extrabold">
            Big Idea
          </span>
        </h1>
        <p class="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
          Share your innovative concept with the Deep Funding community and help shape the future of 
          <span class="text-custom-primary font-semibold">decentralized technology</span>.
        </p>
      </div>

      <Card class="shadow-2xl border-0 bg-card max-w-4xl mx-auto">
        <CardContent class="p-12">
          <form @submit.prevent="submitIdea" class="space-y-8">
            <div>
              <Label for="title" class="text-lg font-semibold text-foreground mb-3 block">
                Idea Title *
              </Label>
              <Input
                id="title"
                v-model="form.title"
                placeholder="Enter a compelling title for your idea"
                required
                class="h-14 text-lg border-2 border-border focus:border-custom-primary focus:ring-2 focus:ring-custom-primary/20 transition-all w-full"
              />
            </div>

            <div>
              <Label for="description" class="text-lg font-semibold text-foreground mb-3 block">
                Detailed Description *
              </Label>
              <Textarea
                id="description"
                v-model="form.description"
                placeholder="Describe your idea in detail. What problem does it solve? How does it work? What makes it innovative?"
                required
                rows="8"
                class="text-lg resize-none border-2 border-border focus:border-custom-primary focus:ring-2 focus:ring-custom-primary/20 transition-all w-full"
              />
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div>
                <Label for="category" class="text-lg font-semibold text-foreground mb-3 block">
                  Category *
                </Label>
                <Select v-model="form.category" required>
                  <SelectTrigger class="!h-14 text-lg border-2 border-border focus:border-custom-primary focus:ring-2 focus:ring-custom-primary/20 transition-all w-full" style="height: 3.5rem !important; min-height: 3.5rem !important;">
                    <SelectValue placeholder="Select a category" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="ai-ml">AI & Machine Learning</SelectItem>
                    <SelectItem value="blockchain">Blockchain & DeFi</SelectItem>
                    <SelectItem value="iot">Internet of Things</SelectItem>
                    <SelectItem value="sustainability">Sustainability</SelectItem>
                    <SelectItem value="healthcare">Healthcare</SelectItem>
                    <SelectItem value="education">Education</SelectItem>
                    <SelectItem value="social-impact">Social Impact</SelectItem>
                    <SelectItem value="other">Other</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div>
                <Label for="submitter" class="text-lg font-semibold text-foreground mb-3 block">
                  Your Name *
                </Label>
                <Input
                  id="submitter"
                  v-model="form.submitter_name"
                  placeholder="Enter your full name"
                  required
                  class="h-14 text-lg border-2 border-border focus:border-custom-primary focus:ring-2 focus:ring-custom-primary/20 transition-all w-full"
                />
              </div>
            </div>

            <div>
              <Label for="email" class="text-lg font-semibold text-foreground mb-3 block">
                Email Address *
              </Label>
              <Input
                id="email"
                v-model="form.email"
                type="email"
                placeholder="your.email@example.com"
                required
                class="h-14 text-lg border-2 border-border focus:border-custom-primary focus:ring-2 focus:ring-custom-primary/20 transition-all w-full"
              />
            </div>

            <div class="flex justify-center pt-8">
              <Button 
                type="submit" 
                :disabled="isSubmitting"
                class="bg-custom-primary hover-primary text-white min-w-[280px] h-16 px-12 text-xl font-bold rounded-full shadow-2xl hover:shadow-custom-primary/25 transform hover:scale-105 hover:-translate-y-1 transition-all duration-300 border-0 relative overflow-hidden group"
              >
                <span v-if="!isSubmitting" class="flex items-center justify-center">
                  <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                  </svg>
                  Submit Your Idea
                </span>
                <span v-else class="flex items-center justify-center">
                  <svg class="animate-spin -ml-1 mr-3 h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Submitting...
                </span>
                <div class="absolute inset-0 bg-white/10 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"></div>
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Card from '@/components/ui/card/Card.vue'
import CardContent from '@/components/ui/card/CardContent.vue'
import Button from '@/components/ui/button/Button.vue'
import Input from '@/components/ui/input/Input.vue'
import Textarea from '@/components/ui/textarea/Textarea.vue'
import Label from '@/components/ui/label/Label.vue'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'

const router = useRouter()

const form = ref({
  title: '',
  description: '',
  category: '',
  submitter_name: '',
  email: ''
})

const isSubmitting = ref(false)

const submitIdea = async () => {
  isSubmitting.value = true
  
  try {
    const response = await fetch('http://localhost:8000/api/submit-idea/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(form.value)
    })

    if (response.ok) {
      alert('Your idea has been submitted successfully!')
      form.value = {
        title: '',
        description: '',
        category: '',
        submitter_name: '',
        email: ''
      }
      router.push('/')
    } else {
      throw new Error('Failed to submit idea')
    }
  } catch (error) {
    console.error('Error submitting idea:', error)
    alert('There was an error submitting your idea. Please try again.')
  } finally {
    isSubmitting.value = false
  }
}
</script>