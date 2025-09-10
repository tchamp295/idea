<template>
  <div class="min-h-screen w-full flex items-center justify-center px-4">
    <Card class="w-full max-w-md">
      <CardHeader>
        <div class="text-center mb-2">
          <div class="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center mx-auto mb-4">
            <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.031 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
          </div>
          <CardTitle class="text-2xl">Admin Access</CardTitle>
          <p class="text-muted-foreground mt-2">Sign in to manage submitted ideas</p>
        </div>
      </CardHeader>
      
      <CardContent class="space-y-4">
        <div class="space-y-2">
          <Label for="username">Username</Label>
          <Input 
            id="username"
            v-model="username" 
            placeholder="Enter your username" 
            type="text"
            autocomplete="username"
          />
        </div>
        
        <div class="space-y-2">
          <Label for="password">Password</Label>
          <Input 
            id="password"
            v-model="password" 
            type="password" 
            placeholder="Enter your password"
            autocomplete="current-password"
            @keyup.enter="login"
          />
        </div>

        <Alert v-if="error" variant="destructive">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <AlertDescription>
            {{ error }}
          </AlertDescription>
        </Alert>

        <div class="flex flex-col gap-3 pt-2">
          <Button @click="login" class="w-full" size="lg">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
            Sign In
          </Button>
          <Button variant="ghost" @click="$router.push('/')" class="w-full">
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Back to Home
          </Button>
        </div>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { adminLogin } from '../services/api'
import { useRouter } from 'vue-router'
import { Button, Card, CardHeader, CardTitle, CardContent, Input, Label, Alert, AlertDescription } from '../components/ui'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const login = async () => {
  error.value = ''
  try {
    await adminLogin(username.value, password.value)
    // simple approach: store credentials locally (not secure long-term)
    localStorage.setItem('admin_user', username.value)
    localStorage.setItem('admin_pass', password.value)
    router.push('/admin/dashboard')
  } catch (err: any) {
    console.error(err)
    error.value = err?.response?.data?.detail || 'Login failed'
  }
}
</script>
