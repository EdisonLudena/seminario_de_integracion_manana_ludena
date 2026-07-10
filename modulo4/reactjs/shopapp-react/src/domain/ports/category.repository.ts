// src/domain/ports/category.repository.ts
import type { Category } from '../entities/category.entity'

export interface CategoryRepository {
  getStats(): Promise<import("../entities/category-stats.entity").CategoryStats>
  getCategories(): Promise<Category[]>
  createCategory(payload: {
    name: string
    slug: string
    description?: string
    is_active?: boolean
  }): Promise<Category>
  updateCategory(
    id: number,
    payload: { name?: string; description?: string; is_active?: boolean },
  ): Promise<Category>
  deleteCategory(id: number): Promise<void>
}