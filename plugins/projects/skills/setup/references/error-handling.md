---
description: Error handling patterns — custom errors, async safety, user-facing messages
paths:
  - src/**
---

# Error Handling Rules

## หลักการ

1. **User เห็น friendly message** — ไม่เห็น stack trace, error codes, หรือ internal details
2. **Developer เห็น context ครบ** — log เก็บ error จริงๆ ไว้ debug
3. **App ไม่ crash** — ทุก async operation มี error handler
4. **Fail gracefully** — ถ้า feature หนึ่งพัง feature อื่นยังทำงานได้

---

## Custom Error Classes

```typescript
// shared/lib/errors.ts

export class AppError extends Error {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options)
    this.name = 'AppError'
  }
}

export class ValidationError extends AppError {
  constructor(message: string, public field?: string) {
    super(message)
    this.name = 'ValidationError'
  }
}

export class StorageError extends AppError {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options)
    this.name = 'StorageError'
  }
}

export class NetworkError extends AppError {
  constructor(message: string, public statusCode?: number) {
    super(message)
    this.name = 'NetworkError'
  }
}
```

```typescript
// ✅ catch แยกตาม error type
try {
  await saveData(payload)
} catch (error) {
  if (error instanceof ValidationError) {
    showFieldError(error.field, error.message)
  } else if (error instanceof NetworkError) {
    showToast('บันทึกไม่สำเร็จ กรุณาลองใหม่')
  } else {
    throw error  // re-throw unexpected errors
  }
}
```

---

## Async Error Handling

```typescript
// ✅ ทุก async operation ต้องมี try-catch
async function saveUser(user: User): Promise<void> {
  try {
    await db.users.save(user)
  } catch (error) {
    throw new StorageError('บันทึกข้อมูลไม่สำเร็จ', { cause: error })
  }
}

// ❌ ห้าม — async โดยไม่มี error handler
async function saveUser(user: User) {
  await db.users.save(user)  // ถ้าพัง error หายเงียบ
}
```

### JSON Parse

```typescript
// ✅ ใช้ safe parse wrapper เสมอ
function safeJsonParse<T>(raw: string): T | null {
  try {
    return JSON.parse(raw) as T
  } catch {
    return null
  }
}
```

---

## User-Facing Error Messages

```typescript
// ✅ ภาษาที่ user เข้าใจ บอกว่าต้องทำอะไรต่อ
'บันทึกไม่สำเร็จ กรุณาลองใหม่'
'ไฟล์ข้อมูลไม่ถูกต้อง กรุณาตรวจสอบแล้วนำเข้าใหม่'
'Session หมดอายุ กรุณา Login ใหม่'

// ❌ ห้ามแสดงต่อ user
'TypeError: Cannot read property of undefined at service.ts:42'
'SQL Error: duplicate key value violates unique constraint'
```

### Error Display Pattern

| สถานการณ์ | วิธีแสดง |
|---|---|
| Form validation | Inline ใต้ field (ไม่ใช่ toast) |
| Action ล้มเหลว (save, delete) | Toast notification สั้นๆ |
| Feature ทั้งหมดพัง | Fallback UI + retry button |
| ไม่มีข้อมูล | Empty state + CTA (ไม่ใช่ error) |

---

## สิ่งที่ห้าม

- ❌ `catch (e) {}` — catch แล้วเงียบ (silent failure)
- ❌ แสดง `error.message` หรือ `error.stack` ต่อ user โดยตรง
- ❌ `console.error` เป็น error handling เดียว (ต้องมี user feedback ด้วย)
- ❌ `throw new Error('something went wrong')` — message ไม่ specific พอสำหรับ debug
