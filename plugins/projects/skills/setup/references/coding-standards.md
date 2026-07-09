---
description: มาตรฐาน TypeScript และ code style สำหรับ project นี้
paths:
  - src/**
  - tests/**
---

# Coding Standards

## TypeScript

```typescript
// ✅ ดี — ระบุ return type ชัดเจนบน public functions
export function formatDate(date: Date): string { ... }

// ❌ ห้าม — implicit any
function processData(data: any) { ... }

// ✅ ดี — discriminated union แทน boolean flags
type RequestStatus = 'idle' | 'loading' | 'success' | 'error'

// ✅ ดี — readonly สำหรับ data ที่ไม่ควร mutate
interface User { readonly id: string; name: string }

// ✅ ดี — satisfies operator สำหรับ typed constants
const DEFAULT_CONFIG = {
  timeout: 5000,
  retries: 3,
} satisfies Partial<AppConfig>
```

## React Components (ถ้าใช้ React)

```typescript
// ✅ named export, typed props, ไม่ใช้ default export
export interface ButtonProps { label: string; onClick: () => void }
export function Button({ label, onClick }: ButtonProps) { ... }

// ❌ ห้าม default export สำหรับ components
export default function Button() { ... }

// ✅ early return สำหรับ loading/empty states
function UserList() {
  const users = useStore(s => s.users)
  if (users.length === 0) return <EmptyState />
  return <ul>...</ul>
}
```

## File Naming

```
// ไฟล์: kebab-case
user-service.ts   auth-controller.ts   format-date.ts

// Class: PascalCase ตรงกับชื่อไฟล์
// user-service.ts → export class UserService

// Test files: อยู่ถัดจากไฟล์ต้นทาง
user-service.ts  →  user-service.test.ts
```

## Import Order

```typescript
// 1. Framework / runtime imports
// 2. External packages (node_modules)
// 3. Internal @-aliased paths (เรียงตามตัวอักษร)
// 4. Relative paths (เฉพาะภายใน module เดียวกัน)
import { useEffect } from 'react'
import axios from 'axios'
import { formatDate } from '@shared/utils/format-date'
import { UserSchema } from './user.types'
```

## Forbidden Patterns

- ❌ `console.log` ใน production code
- ❌ `// @ts-ignore` หรือ `// @ts-nocheck`
- ❌ `!` non-null assertion โดยไม่มี comment อธิบาย
- ❌ Inline styles (`style={{ }}`) — ใช้ CSS class หรือ utility framework
- ❌ Magic numbers — extract เป็น named constant เสมอ
- ❌ `any` type — ใช้ `unknown` แล้ว narrow ด้วย type guard
