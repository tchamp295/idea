<template>
  <div class="min-h-screen w-full max-w-none px-4 py-8">
    <!-- Hero Section -->
    <div class="text-center mb-12">
      <div class="py-12">
        <h1 class="text-4xl lg:text-5xl font-bold bg-gradient-to-r from-indigo-500 to-purple-600 bg-clip-text text-transparent mb-4">
          Transform Your Ideas Into Reality
        </h1>
        
        <p class="text-xl text-muted-foreground max-w-2xl mx-auto leading-relaxed">
          Submit your innovative ideas and let our AI analyze impact, feasibility, and alignment with Deep Funding goals. 
          Get instant feedback and join the future of decentralized innovation.
        </p>
      </div>

      <!-- Stats Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto mb-12">
        <Card class="hover:shadow-lg transition-all cursor-pointer">
          <CardContent class="pt-6">
            <div class="text-center">
              <div class="text-2xl font-bold text-primary mb-2">95%</div>
              <div class="text-sm text-muted-foreground">Accuracy Rate</div>
            </div>
          </CardContent>
        </Card>
        
        <Card class="hover:shadow-lg transition-all cursor-pointer">
          <CardContent class="pt-6">
            <div class="text-center">
              <div class="text-2xl font-bold text-emerald-600 mb-2">&lt; 2s</div>
              <div class="text-sm text-muted-foreground">Processing Time</div>
            </div>
          </CardContent>
        </Card>
        
        <Card class="hover:shadow-lg transition-all cursor-pointer">
          <CardContent class="pt-6">
            <div class="text-center">
              <div class="text-2xl font-bold text-violet-600 mb-2">1,247</div>
              <div class="text-sm text-muted-foreground">Ideas Processed</div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>

    <!-- Main Form -->
    <div class="max-w-4xl mx-auto">
      <Card class="shadow-xl">
        <CardHeader>
          <div class="flex items-center gap-4">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364-.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <div>
              <CardTitle class="text-2xl">Share Your Innovation</CardTitle>
              <p class="text-muted-foreground mt-1">Our AI will analyze and provide instant feedback</p>
            </div>
          </div>
        </CardHeader>
        
        <CardContent class="space-y-6">

          <!-- Title Input -->
          <div class="space-y-2">
            <Label for="title" class="flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
              </svg>
              Idea Title
              <Badge variant="secondary" class="text-xs">Optional</Badge>
            </Label>
            <Input
              id="title"
              v-model="title"
              placeholder="e.g., AI-Powered Smart Contract Auditing System"
              class="h-12"
            />
          </div>

          <!-- Description Textarea -->
          <div class="space-y-2">
            <Label for="description" class="flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              Describe Your Idea
              <Badge variant="destructive" class="text-xs">Required</Badge>
            </Label>
            <Textarea 
              id="description"
              v-model="description" 
              :rows="6" 
              placeholder="Describe your innovative idea in detail. Include the problem it solves, your proposed solution, target audience, and potential impact. The more detail you provide, the better our AI can analyze it."
              class="resize-none"
            />
            <div class="flex justify-between text-xs text-muted-foreground">
              <span>{{ description.length }} characters</span>
              <span>Minimum 50 characters recommended</span>
            </div>
          </div>

          <!-- File Upload -->
          <div class="space-y-2">
            <Label class="flex items-center gap-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
              </svg>
              Supporting Documents
              <Badge variant="secondary" class="text-xs">Optional</Badge>
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
                class="w-full p-6 border-2 border-dashed border-border rounded-xl cursor-pointer transition-all
                       hover:border-primary hover:bg-primary/5 group"
              >
                <div class="text-center">
                  <svg class="w-8 h-8 text-muted-foreground group-hover:text-primary mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                  </svg>
                  <p class="text-sm text-muted-foreground group-hover:text-primary">
                    <span class="font-medium">Click to upload</span> or drag and drop
                  </p>
                  <p class="text-xs text-muted-foreground mt-1">PDF, DOC, TXT, MD up to 10MB</p>
                </div>
              </div>

              <!-- File Display -->
              <div v-if="fileName" class="mt-3 flex items-center gap-2 p-3 bg-muted rounded-lg">
                <svg class="w-4 h-4 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span class="text-sm text-muted-foreground">{{ fileName }}</span>
                <button @click="removeFile" class="ml-auto text-destructive hover:bg-destructive/10 p-1 rounded">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </CardContent>

        <!-- Action Buttons -->
        <div class="px-6 pb-6">
          <div class="flex flex-col sm:flex-row gap-4">
            <Button
              @click="submit"
              :disabled="submitting || !description.trim()"
              size="lg"
              class="flex-1 bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700"
            >
              <svg v-if="submitting" class="w-5 h-5 mr-2 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              <svg v-else class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              {{ submitting ? 'Processing with AI...' : 'Submit & Analyze with AI' }}
            </Button>

            <Button variant="outline" size="lg" @click="$router.push('/ideas')">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
              </svg>
              View All Ideas
            </Button>
          </div>
        </div>

      </Card>

      <!-- Status Messages -->
      <Alert v-if="message" class="mt-6">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <AlertDescription>
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

      <!-- AI Features Preview -->
      <div class="mt-12">
        <div class="text-center mb-8">
          <h3 class="text-2xl font-bold mb-2">How Our AI Analyzes Your Idea</h3>
          <p class="text-muted-foreground">Advanced algorithms provide comprehensive feedback in seconds</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="text-center p-6 bg-card border border-border rounded-xl hover:shadow-lg transition-all">
            <div class="w-12 h-12 bg-primary/10 rounded-xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h4 class="font-semibold mb-2">Impact Score</h4>
            <p class="text-sm text-muted-foreground">Measures potential market impact and innovation value</p>
          </div>

          <div class="text-center p-6 bg-card border border-border rounded-xl hover:shadow-lg transition-all">
            <div class="w-12 h-12 bg-secondary/10 rounded-xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-secondary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
              </svg>
            </div>
            <h4 class="font-semibold mb-2">Feasibility</h4>
            <p class="text-sm text-muted-foreground">Analyzes technical and resource requirements</p>
          </div>

          <div class="text-center p-6 bg-card border border-border rounded-xl hover:shadow-lg transition-all">
            <div class="w-12 h-12 bg-success-500/10 rounded-xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
              </svg>
            </div>
            <h4 class="font-semibold mb-2">Alignment</h4>
            <p class="text-sm text-muted-foreground">Evaluates fit with Deep Funding objectives</p>
          </div>

          <div class="text-center p-6 bg-card border border-border rounded-xl hover:shadow-lg transition-all">
            <div class="w-12 h-12 bg-warning-500/10 rounded-xl flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-warning-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" />
              </svg>
            </div>
            <h4 class="font-semibold mb-2">Duplicate Detection</h4>
            <p class="text-sm text-muted-foreground">Identifies similar existing proposals</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { submitIdea } from '../services/api'
import { useRouter } from 'vue-router'

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
