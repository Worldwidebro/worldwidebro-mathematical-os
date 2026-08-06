---
name: realestate-os/API
title: API Reference
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# API Reference

Base URL: `http://localhost:3001/api` (dev) or `https://your-railway-url/api` (prod)

All endpoints require:
- `Content-Type: application/json`
- `X-User-ID: <UUID>` header (after auth)

---

## Auth

### POST /auth/register
Register new user (landlord or tenant).

**Request:**
```json
{
  "email": "landlord@example.com",
  "password": "securepassword",
  "fullName": "John Doe",
  "role": "landlord"
}
```

**Response:**
```json
{
  "userId": "550e8400-e29b-41d4-a716-446655440000"
}
```

### POST /auth/login
Authenticate user.

**Request:**
```json
{
  "email": "landlord@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": { "id": "...", "email": "..." }
}
```

---

## Properties

### GET /properties
List landlord's properties.

**Response:**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "address": "123 Main St",
    "city": "Austin",
    "state": "TX",
    "zip_code": "78701",
    "units_count": 2,
    "units": [
      { "id": "...", "unit_number": "101", "rent_amount": 1500, "tenant_id": null }
    ]
  }
]
```

### POST /properties
Create property.

**Request:**
```json
{
  "address": "456 Oak Ave",
  "city": "Austin",
  "state": "TX",
  "zipCode": "78702",
  "unitsCount": 3
}
```

### GET /properties/:id
Get property detail with units & leases.

### PUT /properties/:id
Update property.

---

## Rent Payments

### POST /rent-payments/create-payment-link
Create Stripe checkout session.

**Request:**
```json
{
  "unitId": "550e8400-e29b-41d4-a716-446655440002",
  "month": "2024-01",
  "amount": 1500.00
}
```

**Response:**
```json
{
  "url": "https://checkout.stripe.com/pay/cs_test_..."
}
```

### GET /rent-payments
List payments for property (query: `?propertyId=<uuid>`).

### POST /webhooks/stripe
Stripe webhook (auto-updates rent_payments on payment).

---

## Maintenance Requests

### POST /maintenance
Tenant creates request.

**Request:**
```json
{
  "propertyId": "550e8400-e29b-41d4-a716-446655440000",
  "description": "Leaky faucet",
  "photoUrl": "https://s3.amazonaws.com/photos/leak.jpg"
}
```

### GET /maintenance
List requests for property (query: `?propertyId=<uuid>`).

### PUT /maintenance/:id
Update request status (landlord).

**Request:**
```json
{
  "status": "assigned",
  "assignedTo": "550e8400-e29b-41d4-a716-446655440006"
}
```

Status: `open` → `assigned` → `in_progress` → `completed`

---

## Reports

### GET /reports/property/:id/plp
Property P&L (rent in vs. maintenance out).

**Response:**
```json
{
  "rentIn": 4500,
  "maintenanceOut": 200,
  "net": 4300
}
```

### GET /reports/property/:id/tenants
Tenant roster CSV export.

---

## Error Responses

```json
{
  "error": "User not found or invalid credentials"
}
```

**Status codes:**
- `200` — OK
- `201` — Created
- `400` — Bad request
- `401` — Unauthorized
- `403` — Forbidden
- `404` — Not found
- `500` — Server error
