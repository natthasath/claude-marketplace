---
description: นโยบาย testing, mocking, และ coverage targets
paths:
  - src/**
  - tests/**
---

# Testing Rules

## หลักการ

1. **Test behavior ไม่ใช่ implementation** — tests ต้องไม่ break เมื่อ refactor internal code
2. **Arrange-Act-Assert** — ทุก test ต้องมีโครงสร้างชัดเจน
3. **One assertion per concept** — ไม่ยัด unrelated assertions ใน test เดียว
4. **Descriptive names** — ชื่อ test อ่านแล้วรู้ behavior โดยไม่ดู code

## ประเภท Tests

### Unit Tests
- **ทดสอบ:** Functions, services, utilities, data transformations
- **ตำแหน่ง:** Co-located กับ source file (`user-service.test.ts` ถัดจาก `user-service.ts`)
- **เวลา:** < 100ms ต่อ test

### Integration Tests
- **ทดสอบ:** Feature flows ที่ cross หลาย modules/services
- **ตำแหน่ง:** `src/features/<feature>/__tests__/` หรือ `tests/integration/`
- **กฎ:** ใช้ real dependencies เมื่อทำได้, mock เฉพาะ external services

### E2E Tests
- **ทดสอบ:** Critical user journeys ตั้งแต่ต้นจนจบ
- **ตำแหน่ง:** `tests/e2e/`
- **กฎ:** real environment, ไม่ mock anything

## Mocking Policy

```typescript
// ✅ Mock: External systems เท่านั้น
// - Third-party APIs
// - Email/SMS services
// - File system (สำหรับ unit tests)
// - Date/Time (ถ้าต้องการ deterministic)

// ❌ ห้าม mock: Internal modules, utilities, ที่เราเขียนเอง
```

## Test Description Format

```typescript
describe('UserService', () => {
  it('should return user by id when user exists', () => { ... })
  it('should throw ValidationError when id is empty', () => { ... })
  it('should hash password before saving to database', () => { ... })
})
```

## Async Test Pattern

```typescript
it('should save user and return created record', async () => {
  // Arrange
  const input = { name: 'Alice', email: 'alice@example.com' }

  // Act
  const result = await userService.create(input)

  // Assert
  expect(result.id).toBeDefined()
  expect(result.name).toBe('Alice')
})
```

## Coverage Requirements

ปรับ targets ตาม tech stack และขนาดโปรเจค:

- Core business logic — ≥ 90% branch coverage
- API handlers / Controllers — ≥ 80% branch coverage
- Utility functions — ≥ 90% branch coverage
- UI components (ถ้ามี) — ≥ 70% line coverage
- Exclude: generated files, type definitions, re-exports
