---
description: Performance guidelines — rendering, memory management, lazy loading, database
paths:
  - src/**
---

# Performance Rules

## Bundle Size (สำหรับ Frontend)

กำหนด budget ตาม project requirement:

| Chunk | แนวทาง |
|---|---|
| Initial bundle | ≤ 150 KB gzipped (ปรับตาม project) |
| Lazy-loaded chunks | ≤ 100 KB gzipped ต่อ chunk |
| Total app | ≤ 300 KB gzipped |

ตรวจสอบ bundle size หลังเพิ่ม dependency ใหม่ทุกครั้ง

## Rendering Performance (React / Frontend)

```typescript
// ✅ Subscribe เฉพาะ data ที่ใช้ — ป้องกัน unnecessary re-renders
const userName = useStore(s => s.user.name)
const userEmail = useStore(s => s.user.email)

// ❌ Subscribe ทั้ง object — re-renders ทุกครั้งที่ object เปลี่ยน
const user = useStore(s => s.user)

// ✅ useMemo เฉพาะ expensive derivations
const sortedItems = useMemo(() => [...items].sort(byDate), [items])
```

## Memory Management

```typescript
// ✅ ล้าง subscriptions/listeners ใน cleanup เสมอ
useEffect(() => {
  const subscription = eventBus.subscribe('update', handleUpdate)
  return () => subscription.unsubscribe()
}, [])

// ✅ ล้าง intervals ใน cleanup
useEffect(() => {
  const interval = setInterval(poll, 5000)
  return () => clearInterval(interval)
}, [])
```

## Lazy Loading

```typescript
// ✅ Lazy load routes ที่ไม่ใช่ initial view
const SettingsPage = lazy(() => import('@pages/settings'))
const ReportsPage = lazy(() => import('@pages/reports'))

// HomePage โหลดปกติ (critical path)
```

## Database / API Performance

- ใช้ pagination สำหรับ list endpoints (ห้าม return ทั้งหมด)
- ใช้ index บน fields ที่ query บ่อย (foreign keys, status, created_at)
- ใช้ `select()` เฉพาะ fields ที่ต้องการ ไม่ `SELECT *`
- Cache responses ที่ไม่เปลี่ยนบ่อย (เช่น config, reference data)
- N+1 query problem: ใช้ eager loading หรือ DataLoader

## Web Vitals Targets (สำหรับ Web Apps)

| Metric | Target |
|---|---|
| FCP (First Contentful Paint) | < 1.5s |
| LCP (Largest Contentful Paint) | < 2.5s |
| TBT (Total Blocking Time) | < 200ms |
| CLS (Cumulative Layout Shift) | < 0.1 |
| INP (Interaction to Next Paint) | < 200ms |
