<template>
  <div class="min-h-screen bg-background">
    <!-- Header -->
    <header class="border-b border-border bg-card/50 backdrop-blur-sm sticky top-0 z-50">
      <div class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          <h1 class="text-display-md font-bold bg-ai-gradient bg-clip-text text-transparent">
            AI Idea Filter Design System
          </h1>
          <Button variant="ai" size="sm">
            <template #icon>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </template>
            AI Powered
          </Button>
        </div>
      </div>
    </header>

    <main class="container mx-auto px-4 py-8 space-y-12">
      <!-- Color Palette Section -->
      <section>
        <h2 class="text-display-sm mb-8">Color Palette</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Primary Colors -->
          <Card>
            <template #header>
              <h3 class="font-semibold">Primary Colors</h3>
            </template>
            <div class="space-y-2">
              <div v-for="shade in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]" 
                   :key="shade"
                   class="flex items-center justify-between p-2 rounded"
                   :class="`bg-primary-${shade} ${shade >= 600 ? 'text-white' : 'text-gray-900'}`">
                <span>{{ shade }}</span>
                <span class="font-mono text-xs">primary-{{ shade }}</span>
              </div>
            </div>
          </Card>

          <!-- AI Theme Colors -->
          <Card variant="ai">
            <template #header>
              <h3 class="font-semibold">AI Theme Colors</h3>
            </template>
            <div class="space-y-3">
              <div class="p-3 rounded bg-ai-accent text-white">
                <span class="font-medium">AI Accent</span>
              </div>
              <div class="p-3 rounded bg-ai-neural text-white">
                <span class="font-medium">AI Neural</span>
              </div>
              <div class="p-3 rounded bg-ai-data text-white">
                <span class="font-medium">AI Data</span>
              </div>
              <div class="p-3 rounded bg-ai-gradient text-white">
                <span class="font-medium">AI Gradient</span>
              </div>
            </div>
          </Card>

          <!-- Status Colors -->
          <Card>
            <template #header>
              <h3 class="font-semibold">Status Colors</h3>
            </template>
            <div class="space-y-2">
              <div class="p-2 rounded bg-success-500 text-white">Success</div>
              <div class="p-2 rounded bg-warning-500 text-white">Warning</div>
              <div class="p-2 rounded bg-error-500 text-white">Error</div>
              <div class="p-2 rounded bg-info-500 text-white">Info</div>
            </div>
          </Card>
        </div>
      </section>

      <!-- Typography Section -->
      <section>
        <h2 class="text-display-sm mb-8">Typography</h2>
        <Card padding="lg">
          <div class="space-y-6">
            <div>
              <h1 class="text-display-2xl">Display 2XL</h1>
              <p class="text-muted-foreground">4.5rem • 800 weight • -0.02em spacing</p>
            </div>
            <div>
              <h2 class="text-display-xl">Display XL</h2>
              <p class="text-muted-foreground">3.75rem • 800 weight • -0.02em spacing</p>
            </div>
            <div>
              <h3 class="text-display-lg">Display Large</h3>
              <p class="text-muted-foreground">3rem • 700 weight • -0.02em spacing</p>
            </div>
            <div>
              <h4 class="text-display-md">Display Medium</h4>
              <p class="text-muted-foreground">2.25rem • 700 weight • -0.02em spacing</p>
            </div>
            <div>
              <h5 class="text-display-sm">Display Small</h5>
              <p class="text-muted-foreground">1.875rem • 600 weight • -0.02em spacing</p>
            </div>
          </div>
        </Card>
      </section>

      <!-- Button Components -->
      <section>
        <h2 class="text-display-sm mb-8">Buttons</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- Button Variants -->
          <Card>
            <template #header>
              <h3 class="font-semibold">Button Variants</h3>
            </template>
            <div class="space-y-4">
              <div class="flex flex-wrap gap-3">
                <Button variant="primary">Primary</Button>
                <Button variant="secondary">Secondary</Button>
                <Button variant="outline">Outline</Button>
                <Button variant="ghost">Ghost</Button>
                <Button variant="destructive">Destructive</Button>
                <Button variant="ai">AI Special</Button>
              </div>
            </div>
          </Card>

          <!-- Button Sizes -->
          <Card>
            <template #header>
              <h3 class="font-semibold">Button Sizes</h3>
            </template>
            <div class="space-y-4">
              <div class="flex flex-wrap items-center gap-3">
                <Button size="sm">Small</Button>
                <Button size="md">Medium</Button>
                <Button size="lg">Large</Button>
                <Button size="xl">Extra Large</Button>
              </div>
            </div>
          </Card>

          <!-- Button States -->
          <Card>
            <template #header>
              <h3 class="font-semibold">Button States</h3>
            </template>
            <div class="space-y-4">
              <div class="flex flex-wrap gap-3">
                <Button>Normal</Button>
                <Button loading>Loading</Button>
                <Button disabled>Disabled</Button>
                <Button full-width>Full Width</Button>
              </div>
            </div>
          </Card>

          <!-- Buttons with Icons -->
          <Card>
            <template #header>
              <h3 class="font-semibold">Buttons with Icons</h3>
            </template>
            <div class="space-y-4">
              <div class="flex flex-wrap gap-3">
                <Button variant="primary">
                  <template #icon>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                    </svg>
                  </template>
                  Add Idea
                </Button>
                <Button variant="ai">
                  <template #icon>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                  </template>
                  AI Analyze
                </Button>
              </div>
            </div>
          </Card>
        </div>
      </section>

      <!-- Input Components -->
      <section>
        <h2 class="text-display-sm mb-8">Input Components</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <Card>
            <template #header>
              <h3 class="font-semibold">Input Variants</h3>
            </template>
            <div class="space-y-4">
              <Input
                label="Default Input"
                placeholder="Enter your idea..."
                hint="This is a hint message"
              />
              <Input
                label="AI Enhanced Input"
                variant="ai"
                placeholder="AI will help process this..."
              />
              <Input
                label="Required Field"
                required
                placeholder="This field is required"
              />
              <Input
                label="Error State"
                error="This field has an error"
                placeholder="Invalid input"
              />
            </div>
          </Card>

          <Card>
            <template #header>
              <h3 class="font-semibold">Input with Icons</h3>
            </template>
            <div class="space-y-4">
              <Input
                label="Search Ideas"
                placeholder="Search..."
              >
                <template #icon>
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                  </svg>
                </template>
              </Input>
              
              <Input
                label="Email"
                type="email"
                placeholder="you@example.com"
              >
                <template #suffix>
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                  </svg>
                </template>
              </Input>
            </div>
          </Card>
        </div>
      </section>

      <!-- Badge Components -->
      <section>
        <h2 class="text-display-sm mb-8">Badges</h2>
        
        <Card>
          <template #header>
            <h3 class="font-semibold">Badge Variants & Sizes</h3>
          </template>
          <div class="space-y-6">
            <!-- Variants -->
            <div>
              <h4 class="font-medium mb-3">Variants</h4>
              <div class="flex flex-wrap gap-2">
                <Badge>Default</Badge>
                <Badge variant="primary">Primary</Badge>
                <Badge variant="secondary">Secondary</Badge>
                <Badge variant="success">Success</Badge>
                <Badge variant="warning">Warning</Badge>
                <Badge variant="error">Error</Badge>
                <Badge variant="info">Info</Badge>
                <Badge variant="ai">AI Enhanced</Badge>
              </div>
            </div>

            <!-- Sizes -->
            <div>
              <h4 class="font-medium mb-3">Sizes</h4>
              <div class="flex flex-wrap items-center gap-3">
                <Badge size="sm" variant="primary">Small</Badge>
                <Badge size="md" variant="primary">Medium</Badge>
                <Badge size="lg" variant="primary">Large</Badge>
              </div>
            </div>

            <!-- With Dots -->
            <div>
              <h4 class="font-medium mb-3">With Status Dots</h4>
              <div class="flex flex-wrap gap-2">
                <Badge dot variant="success">Active</Badge>
                <Badge dot variant="warning">Pending</Badge>
                <Badge dot variant="error">Failed</Badge>
                <Badge dot variant="ai">AI Processing</Badge>
              </div>
            </div>
          </div>
        </Card>
      </section>

      <!-- Card Components -->
      <section>
        <h2 class="text-display-sm mb-8">Cards</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card>
            <template #header>
              <div class="flex items-center justify-between">
                <h3 class="font-semibold">Default Card</h3>
                <Badge variant="success">Active</Badge>
              </div>
            </template>
            <p class="text-muted-foreground">
              This is a default card with header and footer sections.
            </p>
            <template #footer>
              <div class="flex gap-2">
                <Button size="sm" variant="outline">Cancel</Button>
                <Button size="sm">Continue</Button>
              </div>
            </template>
          </Card>

          <Card variant="ai" hover glow>
            <template #header>
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-ai-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
                <h3 class="font-semibold">AI Enhanced Card</h3>
              </div>
            </template>
            <p class="text-muted-foreground">
              This card has AI theming with hover effects and glow animation.
            </p>
            <template #footer>
              <Button variant="ai" size="sm" full-width>
                Process with AI
              </Button>
            </template>
          </Card>

          <Card variant="outline" hover>
            <div class="text-center space-y-4">
              <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mx-auto">
                <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </div>
              <h3 class="font-semibold">Add New Idea</h3>
              <p class="text-sm text-muted-foreground">
                Submit your innovative ideas for AI processing
              </p>
              <Button variant="outline" size="sm">
                Get Started
              </Button>
            </div>
          </Card>
        </div>
      </section>

      <!-- Animations -->
      <section>
        <h2 class="text-display-sm mb-8">Animations & Effects</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card class="animate-pulse-ai">
            <div class="text-center space-y-2">
              <h3 class="font-semibold">Pulse Animation</h3>
              <p class="text-sm text-muted-foreground">AI processing indicator</p>
            </div>
          </Card>

          <Card class="animate-glow">
            <div class="text-center space-y-2">
              <h3 class="font-semibold">Glow Effect</h3>
              <p class="text-sm text-muted-foreground">Highlighting important content</p>
            </div>
          </Card>

          <Card hover>
            <div class="text-center space-y-2">
              <h3 class="font-semibold">Hover Effects</h3>
              <p class="text-sm text-muted-foreground">Interactive elements</p>
            </div>
          </Card>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { Button, Card, Input, Badge } from './ui'
</script>