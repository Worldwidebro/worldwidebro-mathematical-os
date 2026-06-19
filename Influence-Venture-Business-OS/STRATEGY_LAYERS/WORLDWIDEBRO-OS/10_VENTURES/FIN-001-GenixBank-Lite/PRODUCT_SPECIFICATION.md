# GenixBank Lite - Complete Product Specification

**Venture:** FIN-001 GenixBank Lite
**Phase:** 3 (Product Creation)
**Status:** VALIDATED ✅ → READY FOR DEVELOPMENT
**PMF Score:** 0.83/1.0 (GO DECISION)
**Launch Target:** 2026-08-15

---

## Problem & Solution

**Problem:** SMB founders (solopreneurs to 10-person teams) spend 5-10 hrs/week managing multiple bank accounts, manual expense categorization, disconnected accounting tools. Can't afford $500/month software.

**Solution:** GenixBank Lite — One dashboard for cash flow, AI expense tagging, invoicing. Price: $99/month.

---

## MVP Features (August 2026 Launch)

### 1. Dashboard
- Real-time balance (linked accounts)
- 30-day cash flow chart
- Upcoming bills
- Monthly P&L summary

### 2. Account Linking
- Up to 5 bank accounts via Plaid
- Real-time sync (10-min refresh)
- Transaction history view

### 3. Expense Categorization
- AI auto-tagging (Claude API)
- Manual override
- Custom categories
- Monthly summaries

### 4. Invoicing
- Template-based invoice creation
- Email + shareable link
- Payment reminders
- Invoice tracking

### 5. Mobile
- React Native iOS/Android
- View balance, transactions
- Create invoices on-the-go

---

## Technology Stack

| Layer | Tech |
|-------|------|
| Frontend | Next.js 14 + React |
| Mobile | React Native (Expo) |
| UI Components | design-system (shared) |
| Backend API | genixbank-financial-system |
| Database | PostgreSQL (schema: fin_001) |
| Cache | Redis |
| Queue | RabbitMQ |
| AI Tagging | Claude API |
| Bank Link | Plaid |
| Payments | Stripe |
| Email | SendGrid |
| Hosting | Vercel (frontend) + AWS (backend) |

---

## Data Schema

```sql
-- Users
CREATE TABLE fin_001.users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE,
  company_name VARCHAR(255),
  subscription_tier VARCHAR(50),
  created_at TIMESTAMP
);

-- Linked bank accounts
CREATE TABLE fin_001.accounts (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  plaid_account_id VARCHAR(255),
  account_name VARCHAR(255),
  balance_cents BIGINT,
  last_synced TIMESTAMP
);

-- Transactions from banks
CREATE TABLE fin_001.transactions (
  id UUID PRIMARY KEY,
  account_id UUID REFERENCES accounts(id),
  amount_cents BIGINT,
  description VARCHAR(500),
  transaction_date DATE,
  category_id UUID,
  ai_category VARCHAR(100),
  created_at TIMESTAMP
);

-- Invoices
CREATE TABLE fin_001.invoices (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  invoice_number VARCHAR(50),
  client_name VARCHAR(255),
  amount_cents BIGINT,
  due_date DATE,
  status VARCHAR(50),
  created_at TIMESTAMP
);
```

---

## Development Timeline (11 Weeks)

| Sprint | Week | Focus | Deliverable |
|--------|------|-------|-------------|
| 1 | 1-2 | Setup + Dashboard | Dashboard UI, API integration |
| 2 | 3-4 | Accounts + Expenses | Plaid link, AI categorization |
| 3 | 5-6 | Invoicing + Mobile | Invoice system, React Native app |
| 4 | 7-8 | Polish + Security | UI refinements, security audit |
| 5 | 9-10 | Beta Testing | 10 beta users, feedback loop |
| Launch | 11 | Public Release | 100 beta users, paid tier live |

---

## Pricing

| Tier | Price | Features |
|------|-------|----------|
| Lite | $99/mo | 1 account, basic features, mobile |
| Pro | $199/mo | 5 accounts, team, reporting (Q3 2026) |
| Enterprise | Custom | Unlimited, white-label, dedicated support |

---

## Success Metrics

| Metric | Target | By |
|--------|--------|-----|
| Waitlist | 1,000 | 2026-06-30 |
| Beta users | 100 | 2026-08-15 |
| Paid customers | 50 | 2026-09-15 |
| MRR | $5K | 2026-10-15 |
| NPS | >50 | 2026-10-31 |
| Churn | <3% | 2026-11-30 |

---

**READY FOR DEVELOPMENT**
