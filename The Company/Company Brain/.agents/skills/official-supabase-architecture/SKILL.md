---
name: official-supabase-architecture
description: Official Supabase architecture and database engineering skill covering Row Level Security (RLS), multi-tenant schemas, auth triggers, connection pooling (PgBouncer/Supavisor), and Edge Functions.
source: VoltAgent/awesome-agent-skills
origin: Supabase Official Engineering Standards
---

[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# ⚡ Official Supabase Architecture Skill

> Authoritative backend and database architecture standards based on Supabase official documentation, PostgreSQL RLS, and secure Auth lifecycle patterns.

## 🧠 Core Principles

1. **RLS Enabled by Default**: Every table created in `public` must immediately run `ALTER TABLE <table> ENABLE ROW LEVEL SECURITY;`.
2. **Defensive Policies**: Prefer restrictive policies with explicit `USING` and `WITH CHECK` clauses. Never rely on client filters for authorization.
3. **Connection Pooling Separation**: Use Transaction mode (port 6543) for serverless edge handlers and Session mode (port 5432) for long-running migrations and schema updates.
4. **Auth Decoupling**: Link application user data to `auth.users(id)` via foreign key cascades, keeping sensitive credentials inside the managed auth schema.

---

## 🛠️ Implementation Patterns

### 1. Robust Row Level Security (RLS) Policy

```sql
-- Create table with explicit timestamps and UUID primary key
CREATE TABLE ventures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    owner_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    sector_id TEXT NOT NULL,
    stage TEXT NOT NULL DEFAULT 'planned'
);

-- Enable RLS
ALTER TABLE ventures ENABLE ROW LEVEL SECURITY;

-- 1. Read access for owner
CREATE POLICY "Users can view their own ventures"
ON ventures FOR SELECT
USING (auth.uid() = owner_id);

-- 2. Insert restriction to current user
CREATE POLICY "Users can create ventures for themselves"
ON ventures FOR INSERT
WITH CHECK (auth.uid() = owner_id);

-- 3. Update restricted to owner
CREATE POLICY "Users can update their own ventures"
ON ventures FOR UPDATE
USING (auth.uid() = owner_id)
WITH CHECK (auth.uid() = owner_id);
```

### 2. User Profile Synchronization Trigger

```sql
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, full_name, avatar_url, updated_at)
  VALUES (
    NEW.id,
    NEW.raw_user_meta_data->>'full_name',
    NEW.raw_user_meta_data->>'avatar_url',
    NOW()
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
```

---

## 🔒 Production Verification Checklist

- [ ] All foreign keys are indexed to optimize join performance.
- [ ] RLS policies use indexed columns in their `USING` clauses.
- [ ] Service role key is kept strictly in server-side environment variables and never bundled client-side.
