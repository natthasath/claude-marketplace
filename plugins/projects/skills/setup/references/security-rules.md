---
description: กฎ security — input validation, XSS prevention, authentication, storage
paths:
  - src/**
---

# Security Rules

## Input Validation

```typescript
// ✅ Validate และ sanitize ทุก user input ที่ system boundary

function validateUsername(input: string): string {
  const stripped = input.replace(/<[^>]*>/g, '')  // strip HTML tags
  if (stripped.trim().length === 0) throw new ValidationError('Username is required')
  if (stripped.length > 100) throw new ValidationError('Username must be under 100 chars')
  return stripped.trim()
}

function validatePageSize(size: number, max = 100): number {
  if (!Number.isInteger(size) || size < 1) throw new ValidationError('Page size must be positive integer')
  if (size > max) throw new ValidationError(`Page size cannot exceed ${max}`)
  return size
}
```

## XSS Prevention

```typescript
// ✅ React escape ให้อัตโนมัติผ่าน {} interpolation — ปลอดภัยโดย default
<p>{userInput}</p>

// ❌ ห้ามเด็ดขาด dangerouslySetInnerHTML กับ user input
<p dangerouslySetInnerHTML={{ __html: userInput }} />

// ✅ ถ้าต้องการ render HTML ใช้ sanitizer library
import DOMPurify from 'dompurify'
<p dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userHtml) }} />
```

## Authentication & Authorization

```typescript
// ✅ ตรวจสอบ auth ทุก endpoint ที่ต้องการสิทธิ์
async function getUser(req: Request, res: Response) {
  const user = await verifyToken(req.headers.authorization)
  if (!user) return res.status(401).json({ error: 'Unauthorized' })
  // ... proceed
}

// ✅ ตรวจสอบ permission ไม่ใช่แค่ authentication
async function deletePost(req: Request, res: Response) {
  const post = await Post.findById(req.params.id)
  if (post.authorId !== req.user.id) return res.status(403).json({ error: 'Forbidden' })
  // ... proceed
}
```

## Data Validation on Import/Deserialization

```typescript
// ✅ Validate โครงสร้างข้อมูลที่รับจาก external source
function validateImportedData(data: unknown): data is AppData {
  if (typeof data !== 'object' || data === null) return false
  if (typeof (data as any).version !== 'string') return false
  if (!Array.isArray((data as any).records)) return false
  return true
}
```

## Storage Security

- ❌ ห้ามเก็บ passwords, tokens, หรือ sensitive data ใน localStorage เป็น plain text
- ❌ ห้าม log sensitive data (passwords, credit card numbers, PII)
- ✅ ใช้ httpOnly cookies สำหรับ session tokens
- ✅ Hash passwords ด้วย bcrypt หรือ Argon2 ก่อน store เสมอ
- ✅ Rotate secrets ที่อาจ leaked

## Content Security Policy (สำหรับ Web Apps)

```html
<meta http-equiv="Content-Security-Policy"
  content="default-src 'self';
           script-src 'self';
           style-src 'self' 'unsafe-inline';
           img-src 'self' data: blob:;
           connect-src 'self' https://api.yourdomain.com;">
```

## Dependencies

- รัน `npm audit` หรือ `composer audit` ทุก sprint
- ไม่เพิ่ม dependency ที่มี known high/critical vulnerabilities
- Review dependency permissions ก่อนเพิ่ม (ใช้ network? filesystem?)
