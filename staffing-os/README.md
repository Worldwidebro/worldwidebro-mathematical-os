# Staffing OS - Full Venture Build

**Production-ready staffing agency operations system** integrating worker placement, payroll automation, job matching, and commission tracking for Worldwidebro Companies.

## Quick Start

### Prerequisites
- Node.js 18+
- Docker & Docker Compose
- npm/pnpm

### Setup

```bash
# Clone repo
git clone <your-repo>
cd staffing-os

# Install deps
npm install

# Setup environment
cp .env.example .env
# Edit .env with your Supabase/Venmo credentials

# Start infrastructure
docker-compose up -d

# Run migrations
npm run migrate

# Seed sample data
npm run seed

# Start dev server
npm run dev
```

Server runs at http://localhost:3000

## Architecture

### Database (Prisma)
- **Workers**: Full profiles, skills, hourly rates
- **Clients**: Companies we dispatch jobs to
- **Jobs**: Job listings with skill requirements
- **Placements**: Worker↔Job matches
- **Timesheets**: Hours tracked, payroll calculation
- **Commissions**: Referral payments to Worldwidebro contacts

### API Endpoints

**Workers**
- `POST /api/workers` - Create new worker
- `GET /api/workers` - List all workers
- `GET /api/workers/available` - List available workers

**Jobs**
- `POST /api/jobs` - Create job listing
- `GET /api/jobs` - List all jobs with placements

**Placements**
- `POST /api/placements` - Assign worker to job

**Timesheets**
- `POST /api/timesheets` - Log hours worked
- `GET /api/timesheets/pending` - Unapproved timesheets

**Commissions**
- `POST /api/commissions` - Record referral commission
- `GET /api/commissions/pending` - Unpaid commissions

## n8n Workflows

### Worker Onboarding Flow
- Webhook trigger on new worker registration
- Validates contact info
- Creates worker in database
- Sends welcome email with hourly rate & skills

**Deploy to n8n:**
```bash
n8n import --file n8n-workflows/worker-onboarding.json
```

### Job Matching Engine
- Triggers when job created
- Fetches available workers
- Filters by required skills
- Ranks by hourly rate
- Assigns best match + emails worker

**Handles:**
- Multi-skill matching
- Rate optimization (find worker under 70% of billing rate)
- No-match fallback (notifies ops)

### Weekly Payroll & Commission Processing
- Cron trigger: Every Monday at 9am
- Aggregates weekly timesheets
- Calculates pay: hours × hourly_rate
- Sends Venmo/bank transfers
- Emails payroll summary

**Commission Flow:**
- Referral comes in → Creates commission record
- Marks as "pending"
- Weekly payout run processes all pending
- Updates status to "paid"

## Deployment

### Docker (Production)
```bash
docker-compose up --build -d
```

Includes:
- PostgreSQL 15
- Node.js Express app
- Auto-migration on startup
- Port 3000 exposed

### Manual Deploy
```bash
npm run build
npm start
```

## Integration with Worldwidebro Ecosystem

### Supabase Sync
- Contacts from 150-contact CSV → Workers table
- Referrals from dispatch → Commissions table
- Jobs from Charlotte contractors → Jobs table

### n8n → Worldwidebro Workflows
- n8n job matching → Sends job to worker via WhatsApp
- Timesheet approval → Triggers payroll via Make.com
- Commission payment → Syncs to Venmo tracker

### AI Layer (Future)
- Skill matching embeddings (worker skills vs job requirements)
- Dynamic pricing based on demand
- Predictive job allocation (which workers → which jobs → highest margin)

## Development

### Run tests
```bash
npm test
```

### View database
```bash
npm run studio
```
Opens Prisma Studio at http://localhost:5555

### Seed sample data
```bash
npm run seed
```
Adds 5 workers, 3 clients, 2 jobs for testing

## Margin Model

| Metric | Value |
|--------|-------|
| Worker Hourly Rate | $15-25/hr |
| Client Bill Rate | $35-50/hr |
| Gross Margin | $10-35/hr |
| Payroll Taxes + Insurance | ~15% of gross |
| **Net Margin** | **$8-30/hr** |

Example: HVAC tech at $20/hr, billed at $45/hr
- Gross: $25/hr
- Taxes/Insurance: $3.75
- **Net profit: $21.25/hr**

## Support

- `contacts.md`: Contact list structure
- `commission-structure.md`: Rate cards
- `flier-templates.md`: Marketing templates

---

**Built for Worldwidebro Holdings** | License: MIT
