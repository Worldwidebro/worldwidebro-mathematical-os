-- Staffing OS Source of Truth Schema
-- D - Data Layer foundation for all workflows, economics, compliance

CREATE TABLE clients (id UUID PRIMARY KEY, name TEXT, industry TEXT, location TEXT, contact_email TEXT, billing_email TEXT, created_at TIMESTAMP, status TEXT);
CREATE TABLE jobs (id UUID PRIMARY KEY, client_id UUID REFERENCES clients(id), title TEXT, wage_rate DECIMAL(10,2), bill_rate DECIMAL(10,2), hours_per_week INT, required_skills TEXT[], location TEXT, status TEXT, created_at TIMESTAMP, filled_count INT);
CREATE TABLE candidates (id UUID PRIMARY KEY, name TEXT, email TEXT, phone TEXT, skills TEXT[], work_verified BOOLEAN, background_check_status TEXT, rate_expected DECIMAL(10,2), location TEXT, created_at TIMESTAMP, score DECIMAL(3,2));
CREATE TABLE assignments (id UUID PRIMARY KEY, candidate_id UUID REFERENCES candidates(id), job_id UUID REFERENCES jobs(id), client_id UUID REFERENCES clients(id), status TEXT, placed_at TIMESTAMP, placement_cost DECIMAL(10,2), expected_ltv DECIMAL(10,2));
CREATE TABLE shifts (id UUID PRIMARY KEY, assignment_id UUID REFERENCES assignments(id), scheduled_date DATE, start_time TIME, end_time TIME, hours INT, status TEXT, created_at TIMESTAMP);
CREATE TABLE timesheets (id UUID PRIMARY KEY, assignment_id UUID REFERENCES assignments(id), week_start DATE, regular_hours DECIMAL(5,2), overtime_hours DECIMAL(5,2), status TEXT, submitted_at TIMESTAMP, approved_at TIMESTAMP);
CREATE TABLE payroll (id UUID PRIMARY KEY, assignment_id UUID REFERENCES assignments(id), gross_pay DECIMAL(10,2), deductions DECIMAL(10,2), net_pay DECIMAL(10,2), period_start DATE, period_end DATE, paid_at TIMESTAMP);
CREATE TABLE invoices (id UUID PRIMARY KEY, client_id UUID REFERENCES clients(id), job_id UUID REFERENCES jobs(id), billable_hours INT, rate DECIMAL(10,2), gross_amount DECIMAL(10,2), created_at TIMESTAMP, sent_at TIMESTAMP, paid_at TIMESTAMP, status TEXT);
CREATE TABLE agent_runs (id UUID PRIMARY KEY, workflow_id TEXT, agent_id TEXT, task_type TEXT, input_data JSONB, output_data JSONB, started_at TIMESTAMP, completed_at TIMESTAMP, status TEXT);
CREATE TABLE action_ledger (id UUID PRIMARY KEY, agent_id TEXT, action_type TEXT, workflow_id TEXT, execution_mode TEXT, local_cost DECIMAL(10,4), external_cost DECIMAL(10,4), human_equivalent_cost DECIMAL(10,2), revenue_enabled DECIMAL(10,2), loss_avoided DECIMAL(10,2), outcome TEXT, confidence DECIMAL(3,2), created_at TIMESTAMP);
CREATE TABLE compliance_events (id UUID PRIMARY KEY, entity_type TEXT, entity_id UUID, check_type TEXT, status TEXT, details JSONB, created_at TIMESTAMP, resolved_at TIMESTAMP);
CREATE TABLE events (id UUID PRIMARY KEY, event_type TEXT, entity_id UUID, entity_type TEXT, data JSONB, created_at TIMESTAMP);

CREATE INDEX idx_clients_status ON clients(status);
CREATE INDEX idx_jobs_client_id ON jobs(client_id);
CREATE INDEX idx_candidates_verified ON candidates(work_verified);
CREATE INDEX idx_assignments_status ON assignments(status);
CREATE INDEX idx_invoices_status ON invoices(status);
CREATE INDEX idx_action_ledger_agent ON action_ledger(agent_id);
CREATE INDEX idx_events_type ON events(event_type);
