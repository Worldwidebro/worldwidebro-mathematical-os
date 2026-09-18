# Orchestrator Prime (AGT-001) Test Suite

Comprehensive test suite for the task classification system in Orchestrator Prime.

## Overview

The test suite validates that `classifyTask()` correctly:
- Identifies task intent (outreach, sales, support, product, operations)
- Extracts required capabilities for each task type
- Suggests appropriate autonomy levels (L1/L2/L3)
- Handles edge cases gracefully
- Recovers from API errors

**Test Coverage:** 11 tests across 3 test groups  
**File:** `orchestrator-prime.test.ts`  
**Acceptance Criteria:** Phase 2 completion verification

---

## Test Breakdown

### 1. Happy Path Tests (5 tests)

These tests verify correct behavior for well-formed, typical task inputs.

#### Test 1: Outreach Tasks
```typescript
✓ classifies outreach tasks correctly
```
**Task Example:** "Send personalized outreach emails to 50 prospects about our new product"

**Verifies:**
- Intent is identified as `"outreach"`
- Capabilities include: `write-emails`, `personalize`, `track-opens`
- Autonomy level is valid (L1, L2, or L3)
- logic_layers array exists (even if empty)

---

#### Test 2: Sales Tasks
```typescript
✓ classifies sales tasks correctly
```
**Task Example:** "Make cold calls to qualified leads and schedule product demos"

**Verifies:**
- Intent is identified as `"sales"`
- Capabilities include: `cold-calling`, `track-calls`, `schedule-demos`
- Autonomy level is valid
- Has non-empty capability list

---

#### Test 3: Support Tasks
```typescript
✓ classifies support tasks correctly
```
**Task Example:** "Provide technical support to customers experiencing API integration issues"

**Verifies:**
- Classification is returned (not null/undefined)
- Intent is a non-empty string
- required_capabilities is an array
- autonomy_suggested is defined

---

#### Test 4: Product Tasks
```typescript
✓ classifies product tasks correctly
```
**Task Example:** "Design and implement new dashboard features for analytics platform"

**Verifies:**
- Intent is defined
- required_capabilities is a proper array
- autonomy_suggested is valid
- Classification object is not empty

---

#### Test 5: Operations Tasks
```typescript
✓ classifies operations tasks correctly
```
**Task Example:** "Optimize warehouse inventory management system and reduce stockouts"

**Verifies:**
- Classification exists with all required fields
- Autonomy level is valid
- Both logic_layers and required_capabilities are arrays

---

### 2. Edge Cases (4 tests)

These tests verify graceful handling of unusual or incomplete inputs.

#### Test 6: Vague Task Description
```typescript
✓ handles vague task description gracefully
```
**Input:** "Do some work"

**Verifies:**
- Does not throw error
- Returns sensible default intent
- Autonomy level is valid
- required_capabilities is an array (may be empty)

---

#### Test 7: Multi-Intent Tasks
```typescript
✓ identifies primary intent for multi-intent tasks
```
**Input:** "Send emails to prospects, schedule demos, and track call outcomes with reporting"

**Verifies:**
- Identifies ONE primary intent (not multiple)
- Intent is one of: `outreach`, `sales`, `booking`, or `general`
- Still provides capabilities for the primary intent
- Does not get confused by multiple keywords

---

#### Test 8: Empty Description
```typescript
✓ handles empty description gracefully
```
**Input:** ""

**Verifies:**
- Does not throw error
- Returns valid classification structure
- Defaults to `"general"` intent
- Autonomy level is valid
- required_capabilities is an empty or minimal array

---

#### Test 9: No Matching Keywords
```typescript
✓ handles task with no matching logic layer keywords
```
**Input:** "This task does not contain any keywords related to known layers"

**Verifies:**
- Returns valid classification
- logic_layers array is empty (no matches)
- Intent is still defined
- Autonomy level is still provided

---

### 3. Error Handling (2 tests)

These tests verify graceful recovery from infrastructure failures.

#### Test 10: API Timeout
```typescript
✓ returns default classification on API timeout
```

**Simulates:** Slow or timed-out Claude API call

**Verifies:**
- Does not throw error
- Returns valid classification with all required fields
- Autonomy level is valid
- Does not break the classification flow

---

#### Test 11: Missing API Key
```typescript
✓ handles missing API key gracefully
```

**Simulates:** Empty or invalid Supabase API key

**Verifies:**
- Does not throw error
- Returns valid classification structure
- All required fields are present
- All arrays are proper arrays
- Autonomy level is valid

---

## Running the Tests

### Run All Tests
```bash
npm test src/services/__tests__/orchestrator-prime.test.ts
```

### Run Specific Test Suite
```bash
npm test -- --testNamePattern="happy path"
npm test -- --testNamePattern="edge cases"
npm test -- --testNamePattern="error handling"
```

### Run with Coverage
```bash
npm test -- --coverage src/services/__tests__/orchestrator-prime.test.ts
```

### Run in Watch Mode
```bash
npm test -- --watch src/services/__tests__/orchestrator-prime.test.ts
```

---

## Test Data Structure

### Sample Task Input
```typescript
interface Task {
  id?: string;              // Optional task ID
  description: string;      // Task description (required)
  venture: string;         // Venture code (e.g., "OPS-001", "LT-005")
  urgency?: "high" | "medium" | "low";
  budget?: number;
  revenue_target?: number;
}
```

### Expected Classification Output
```typescript
interface TaskClassification {
  intent: string;                           // "outreach", "sales", "booking", etc.
  logic_layers: string[];                   // Array of logic layer IDs
  required_capabilities: string[];          // Array of capability names
  autonomy_suggested: "L1" | "L2" | "L3";  // Autonomy level recommendation
}
```

---

## Acceptance Criteria (Phase 2 Completion)

All 11 tests must pass for Phase 2 to be considered complete:

- [ ] 5 happy path tests pass
- [ ] 4 edge case tests pass
- [ ] 2 error handling tests pass
- [ ] All required fields present in classification output
- [ ] Classification is deterministic (same input → same output)
- [ ] No uncaught errors or exceptions
- [ ] Test coverage ≥ 85% for classifyTask() method

---

## Troubleshooting

### Test Fails: "Cannot find module 'orchestrator-prime'"
**Solution:** Ensure `orchestrator-prime.ts` exists at `src/services/orchestrator-prime.ts`

### Test Fails: "jest is not defined"
**Solution:** Install Jest: `npm install --save-dev jest @types/jest ts-jest`

### Test Fails: "OrchestratorPrime is not exported"
**Solution:** Ensure `export class OrchestratorPrime` is in orchestrator-prime.ts

### Tests are Hanging
**Solution:** Check Supabase mock in setup.ts. May need to increase Jest timeout:
```typescript
jest.setTimeout(30000); // 30 seconds
```

---

## Next Steps

After tests pass:

1. **Wire Claude Haiku Integration**
   - Replace keyword-based classification with Claude API
   - Add prompt engineering for intent detection
   - Implement capability extraction from Claude response

2. **Add Performance Tests**
   - Measure classification latency
   - Verify sub-200ms response time
   - Track API call costs

3. **Add Integration Tests**
   - Test classifyTask → findBestAgent → executeTask flow
   - Verify end-to-end task routing
   - Test revenue attribution pipeline

4. **Expand Coverage**
   - Add tests for findBestAgent()
   - Add tests for executeTask()
   - Add tests for attributeRevenue()

---

## References

- **Orchestrator Prime:** `src/services/orchestrator-prime.ts`
- **Jest Config:** `jest.config.js`
- **Phase 2 Plan:** `20-DECISIONS/PHASE-2-PHASE-2A-INTEGRATION-MAP.md`
- **Test Setup:** `src/services/__tests__/setup.ts`

---

**Created:** September 18, 2026  
**Status:** Phase 2 Acceptance Tests  
**Maintained By:** Claude Haiku 4.5
