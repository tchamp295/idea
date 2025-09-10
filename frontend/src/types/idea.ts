export interface SimilarIdea {
  id: string
  title: string
  similarity: number
}

export interface Idea {
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
  similar_ideas?: SimilarIdea[]
}

export interface IdeaSubmissionData {
  title?: string
  description: string
  file?: File
}

export interface ApiResponse<T> {
  data: T
  message?: string
  status: number
}