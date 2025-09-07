import axios from 'axios'

export type Idea = {
  id?: string
  title?: string
  description?: string
  file_url?: string
  created_at?: string
  evaluation?: string
  impact_score?: number
  feasibility_score?: number
  alignment_score?: number
  overall_score?: number
  is_duplicate?: boolean
  feedback?: string
  category?: string
  subcategory?: string
  similar_ideas?: Array<{
    id: string
    title: string
    similarity: number
  }>
}

const API = axios.create({
  baseURL: (import.meta.env.VITE_API_URL as string) || 'http://127.0.0.1:8000',
  timeout: 15000,
})

export async function submitIdea(formData: FormData) {
  // expects backend /api/submit-idea/ to accept multipart/form-data
  return API.post('/api/submit-idea/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
}

export async function adminLogin(username: string, password: string) {
  const body = new URLSearchParams()
  body.append('username', username)
  body.append('password', password)
  return API.post('/api/admin-login/', body)
}

export async function fetchIdeas(username?: string, password?: string) {
  // backend expects /api/ideas/
  const params: any = username && password ? { username, password } : {}
  return API.get<Idea[]>('/api/ideas/', { params })
}
