<template>
  <section class="py-12">
    <div class="max-w-4xl mx-auto">
      <Card class="shadow-2xl border-0 bg-card/80 backdrop-blur-sm">
        <CardHeader class="pb-8">
          <div class="flex items-center gap-4">
            <div class="w-14 h-14 rounded-2xl bg-ai-gradient flex items-center justify-center">
              <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364-.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <div>
              <CardTitle class="text-2xl lg:text-3xl font-bold">Share Your Innovation</CardTitle>
              <p class="text-muted-foreground mt-2 text-lg">Our AI will analyze and provide instant feedback</p>
            </div>
          </div>
        </CardHeader>
        
        <CardContent class="space-y-8">
          <!-- Title Input -->
          <div class="space-y-3">
            <Label for="title" class="flex items-center gap-2 text-base font-semibold">
              <svg class="w-4 h-4 text-ai-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
              </svg>
              Idea Title
              <Badge variant="secondary" class="text-xs ml-auto">Optional</Badge>
            </Label>
            <Input
              id="title"
              v-model="title"
              placeholder="e.g., AI-Powered Smart Contract Auditing System"
              class="h-14 text-base border-2 focus:border-primary transition-colors"
            />
          </div>

          <!-- Description Textarea -->
          <div class="space-y-3">
            <Label for="description" class="flex items-center gap-2 text-base font-semibold">
              <svg class="w-4 h-4 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              Describe Your Idea
              <Badge variant="destructive" class="text-xs ml-auto">Required</Badge>
            </Label>
            <Textarea 
              id="description"
              v-model="description" 
              :rows="6" 
              placeholder="Describe your innovative idea in detail. Include the problem it solves, your proposed solution, target audience, and potential impact. The more detail you provide, the better our AI can analyze it."
              class="resize-none text-base border-2 focus:border-primary transition-colors"
            />
            <div class="flex justify-between text-sm text-muted-foreground">
              <span>{{ description.length }} characters</span>
              <span class="flex items-center gap-1">
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Minimum 50 characters recommended
              </span>
            </div>
          </div>

          <!-- File Upload -->
          <div class="space-y-3">
            <Label class="flex items-center gap-2 text-base font-semibold">
              <svg class="w-4 h-4 text-secondary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
              </svg>
              Supporting Documents
              <Badge variant="secondary" class="text-xs ml-auto">Optional</Badge>
            </Label>
            
            <div class="relative">
              <input 
                type="file" 
                @change="onFile" 
                class="hidden" 
                ref="fileInput" 
                accept=".pdf,.doc,.docx,.txt,.md"
              />
              
              <div 
                @click="() => fileInput?.click()"
                class="w-full p-8 border-2 border-dashed border-border rounded-2xl cursor-pointer transition-all
                       hover:border-primary hover:bg-primary/5 group"
              >
                <div class="text-center">
                  <div class="w-16 h-16 mx-auto mb-4 bg-muted rounded-2xl flex items-center justify-center group-hover:bg-primary/10 transition-colors">
                    <svg class="w-8 h-8 text-muted-foreground group-hover:text-primary transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                    </svg>
                  </div>
                  <p class="text-base text-muted-foreground group-hover:text-primary transition-colors mb-2">
                    <span class="font-semibold">Click to upload</span> or drag and drop
                  </p>
                  <p class="text-sm text-muted-foreground">PDF, DOC, TXT, MD up to 10MB</p>
                </div>
              </div>

              <!-- File Display -->
              <div v-if="fileName" class="mt-4 flex items-center gap-3 p-4 bg-success-500/10 border border-success-500/20 rounded-xl">
                <div class="w-8 h-8 bg-success-500/20 rounded-lg flex items-center justify-center">
                  <svg class="w-4 h-4 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <span class="text-sm font-medium text-success-800 dark:text-success-200 flex-1">{{ fileName }}</span>
                <Button @click="removeFile" variant="ghost" size="sm" class="text-success-600 hover:text-success-700 hover:bg-success-500/20 p-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </Button>
              </div>
            </div>
          </div>
        </CardContent>

        <!-- Action Buttons -->
        <div class="px-8 pb-8">
          <div class="flex flex-col sm:flex-row gap-4">
            <Button
              @click="submit"
              :disabled="submitting || !description.trim()"
              size="lg"
              class="flex-1 h-14 text-base font-semibold bg-ai-gradient hover:opacity-90 text-white"
            >
              <svg v-if="submitting" class="w-5 h-5 mr-2 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              <svg v-else class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              {{ submitting ? 'Processing with AI...' : 'Submit & Analyze with AI' }}
            </Button>

            <Button variant="outline" size="lg" @click="$router.push('/ideas')" class="h-14 text-base font-semibold border-2">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
              </svg>
              View All Ideas
            </Button>
          </div>
        </div>
      </Card>

      <!-- Status Messages -->
      <Alert v-if="message" class="mt-6 border-success-500/20 bg-success-500/10">
        <svg class="w-4 h-4 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <AlertDescription class="text-success-800 dark:text-success-200 font-medium">
          {{ message }}
        </AlertDescription>
      </Alert>

      <Alert v-if="error" variant="destructive" class="mt-6">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <AlertDescription>
          {{ error }}
        </AlertDescription>
      </Alert>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { submitIdea } from '@/services/api'
import { useRouter } from 'vue-router'
import Card from '@/components/ui/card/Card.vue'
import CardContent from '@/components/ui/card/CardContent.vue'
import CardHeader from '@/components/ui/card/CardHeader.vue'
import CardTitle from '@/components/ui/card/CardTitle.vue'
import Button from '@/components/ui/button/Button.vue'
import Input from '@/components/ui/input/Input.vue'
import Textarea from '@/components/ui/textarea/Textarea.vue'
import Label from '@/components/ui/label/Label.vue'
import Badge from '@/components/ui/badge/Badge.vue'
import Alert from '@/components/ui/alert/Alert.vue'
import AlertDescription from '@/components/ui/alert/AlertDescription.vue'

const title = ref('')
const description = ref('')
const file = ref<File | null>(null)
const fileName = ref('')
const submitting = ref(false)
const message = ref('')
const error = ref('')
const router = useRouter()
const fileInput = ref<HTMLInputElement>()

const onFile = (e: Event) => {
  const target = e.target as HTMLInputElement
  const f = target.files && target.files[0]
  if (f) {
    file.value = f
    fileName.value = f.name
  } else {
    file.value = null
    fileName.value = ''
  }
}

const removeFile = () => {
  file.value = null
  fileName.value = ''
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

const submit = async () => {
  error.value = ''
  message.value = ''
  if (!description.value.trim()) {
    error.value = 'Please describe your idea before submitting.'
    return
  }
  submitting.value = true
  try {
    const fd = new FormData()
    fd.append('title', title.value)
    fd.append('description', description.value)
    if (file.value) fd.append('file', file.value)

    await submitIdea(fd)
    message.value = '🎉 Your idea has been submitted and is being analyzed by our AI!'
    
    // Reset form
    title.value = ''
    description.value = ''
    file.value = null
    fileName.value = ''
    if (fileInput.value) {
      fileInput.value.value = ''
    }

    // Navigate to ideas list after 2 seconds
    setTimeout(() => {
      router.push('/ideas')
    }, 2000)
    
  } catch (err: any) {
    console.error(err)
    error.value = err?.response?.data?.detail || 'Failed to submit idea. Please try again.'
  } finally {
    submitting.value = false
  }
}
</script>