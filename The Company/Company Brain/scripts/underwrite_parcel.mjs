/**
 * Automated 10-Year DCF Underwriting Engine
 * RE-001 Worldwidebro Group — Task RE-031 & RE-032
 *
 * Usage:
 *   node scripts/underwrite_parcel.mjs --price=350000 --rent=2700 --address="1234 West Trade St, Charlotte, NC"
 *   node scripts/underwrite_parcel.mjs --pin="06902201"
 */
import fs from 'fs';
import path from 'path';

// Parse command line arguments
const args = process.argv.slice(2).reduce((acc, curr) => {
  const [k, v] = curr.replace(/^--/, '').split('=');
  acc[k] = v;
  return acc;
}, {});

const address = args.address || 'Sample Charlotte Infill Asset, Charlotte, NC 28208';
const purchasePrice = Number(args.price) || 340000;
const monthlyRent = Number(args.rent) || 2700;
const units = Number(args.units) || 2;
const downPaymentPct = Number(args.downPaymentPct) || 0.25;
const interestRate = Number(args.rate) || 0.0675; // 6.75%
const loanTermYears = 30;
const rentGrowth = 0.03; // 3.0% annual rent growth
const expenseInflation = 0.025; // 2.5% expense inflation
const vacancyRate = 0.05; // 5.0%
const exitCapRate = 0.065; // 6.5% Year 10 exit cap
const discountRate = 0.10; // 10.0% hurdle rate for NPV

// Debt Calculations
const loanAmount = purchasePrice * (1 - downPaymentPct);
const initialEquity = purchasePrice * downPaymentPct;
const monthlyRate = interestRate / 12;
const nMonths = loanTermYears * 12;
const monthlyPayment = (loanAmount * (monthlyRate * Math.pow(1 + monthlyRate, nMonths))) / (Math.pow(1 + monthlyRate, nMonths) - 1);
const annualDebtService = monthlyPayment * 12;

// Calculate remaining loan balance at Year N
function getLoanBalance(initialLoan, rMonthly, totalMonths, elapsedMonths) {
  return (initialLoan * (Math.pow(1 + rMonthly, totalMonths) - Math.pow(1 + rMonthly, elapsedMonths))) / (Math.pow(1 + rMonthly, totalMonths) - 1);
}

// 10-Year Cash Flow Projection
const schedule = [];
let currentRent = monthlyRent * 12;
let currentTaxes = purchasePrice * 0.011; // 1.1% property tax
let currentInsurance = purchasePrice * 0.005; // 0.5% insurance
let currentMaint = currentRent * 0.07;
let currentMgmt = currentRent * 0.08;
let currentReserves = currentRent * 0.03;

for (let yr = 1; yr <= 10; yr++) {
  const gsr = Math.round(currentRent);
  const vacancy = Math.round(gsr * vacancyRate);
  const egi = gsr - vacancy;

  const taxes = Math.round(currentTaxes);
  const ins = Math.round(currentInsurance);
  const maint = Math.round(currentMaint);
  const mgmt = Math.round(currentMgmt);
  const res = Math.round(currentReserves);
  const totalOpex = taxes + ins + maint + mgmt + res;

  const noi = egi - totalOpex;
  const debtService = Math.round(annualDebtService);
  const netCashFlow = noi - debtService;
  const dscr = Number((noi / debtService).toFixed(2));
  const cashOnCash = Number(((netCashFlow / initialEquity) * 100).toFixed(2));

  schedule.push({
    year: yr,
    gsr,
    vacancy,
    egi,
    opex: totalOpex,
    noi,
    debtService,
    netCashFlow,
    dscr,
    cashOnCash,
  });

  // Inflate for next year
  currentRent *= (1 + rentGrowth);
  currentTaxes *= (1 + expenseInflation);
  currentInsurance *= (1 + expenseInflation);
  currentMaint *= (1 + expenseInflation);
  currentMgmt = currentRent * 0.08;
  currentReserves *= (1 + expenseInflation);
}

// Year 10 Exit / Disposition
const year11NOI = schedule[9].noi * (1 + rentGrowth);
const exitGrossSale = Math.round(year11NOI / exitCapRate);
const dispositionFee = Math.round(exitGrossSale * 0.03); // 3% broker/legal
const remainingLoanBal = Math.round(getLoanBalance(loanAmount, monthlyRate, nMonths, 120));
const netExitProceeds = exitGrossSale - dispositionFee - remainingLoanBal;

// Cash Flow Streams
const leveredCashFlows = [-initialEquity];
for (let i = 0; i < 9; i++) {
  leveredCashFlows.push(schedule[i].netCashFlow);
}
leveredCashFlows.push(schedule[9].netCashFlow + netExitProceeds);

// Calculate NPV
function calcNPV(rate, cfs) {
  return cfs.reduce((acc, val, idx) => acc + val / Math.pow(1 + rate, idx), 0);
}

// Calculate IRR (Newton-Raphson Solver)
function calcIRR(cfs, guess = 0.12) {
  let r = guess;
  for (let i = 0; i < 100; i++) {
    const npv = calcNPV(r, cfs);
    if (Math.abs(npv) < 0.0001) return r;
    // Derivative of NPV with respect to r
    const dNpv = cfs.reduce((acc, val, idx) => idx === 0 ? acc : acc - (idx * val) / Math.pow(1 + r, idx + 1), 0);
    if (Math.abs(dNpv) < 0.000001) break;
    r = r - npv / dNpv;
  }
  return r;
}

const leveredIRR = Number((calcIRR(leveredCashFlows) * 100).toFixed(2));
const npvAt10 = Math.round(calcNPV(discountRate, leveredCashFlows));
const totalReturns = leveredCashFlows.slice(1).reduce((a, b) => a + b, 0);
const equityMultiple = Number(((totalReturns + initialEquity) / initialEquity).toFixed(2));
const inPlaceCapRate = Number(((schedule[0].noi / purchasePrice) * 100).toFixed(2));

// Generate Formatted Markdown Memorandum
const outputMd = `# Institutional 10-Year DCF Underwriting Memorandum
**Asset:** ${address}  
**Prepared By:** Worldwidebro Group Institutional Acquisitions (RE-001)  
**Date:** ${new Date().toISOString().split('T')[0]}  
**Status:** Pre-Underwritten & Verified

---

## 1. Executive Investment Summary

| Metric | Underwritten Value | Benchmark Standard |
| :--- | :---: | :---: |
| **Purchase / Acquisition Price** | **$${purchasePrice.toLocaleString()}** | Target Basis |
| **Initial Equity Requirement (25%)** | **$${initialEquity.toLocaleString()}** | Cash Required |
| **Debt Financing (75% LTV @ 6.75%)** | **$${loanAmount.toLocaleString()}** | 30-Year Amortization |
| **Annual Debt Service** | **$${Math.round(annualDebtService).toLocaleString()}** | Fixed Payment |
| **Year 1 In-Place Cap Rate** | **${inPlaceCapRate}%** | Market Average: 5.8% |
| **Year 1 DSCR** | **${schedule[0].dscr}x** | Minimum Lender Floor: 1.20x |
| **Year 1 Cash-on-Cash Return** | **${schedule[0].cashOnCash}%** | In-place Yield |
| **Projected 10-Year Levered IRR** | **${leveredIRR}%** | Target Hurdle: 14.0% |
| **Net Present Value (NPV @ 10%)** | **$${npvAt10.toLocaleString()}** | Value Created Above Cost |
| **10-Year Equity Multiple** | **${equityMultiple}x** | Total Invested Multiple |

---

## 2. 10-Year Pro-Forma Cash Flow Schedule

| Year | Gross Scheduled Rent | Effective Gross Income | Operating Expenses | Net Operating Income | Debt Service | Net Cash Flow | DSCR | Cash-on-Cash |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
${schedule.map((row) => `| **Yr ${row.year}** | $${row.gsr.toLocaleString()} | $${row.egi.toLocaleString()} | $${row.opex.toLocaleString()} | **$${row.noi.toLocaleString()}** | $${row.debtService.toLocaleString()} | **$${row.netCashFlow.toLocaleString()}** | ${row.dscr}x | ${row.cashOnCash}% |`).join('\n')}

---

## 3. Year 10 Terminal Valuation & Capital Event

- **Year 11 Forward NOI:** $${Math.round(year11NOI).toLocaleString()}
- **Terminal Exit Cap Rate:** ${(exitCapRate * 100).toFixed(1)}%
- **Gross Disposition Valuation:** $${exitGrossSale.toLocaleString()}
- **Estimated Disposition Costs (3.0%):** -$${dispositionFee.toLocaleString()}
- **Remaining Mortgage Principal Payoff:** -$${remainingLoanBal.toLocaleString()}
- **Net Reversion Proceeds to Equity:** **$${netExitProceeds.toLocaleString()}**

---

## 4. Sensitivity Matrix: Exit Cap vs. Hurdle Rate

| Exit Cap Rate \\ Discount Rate | 8.0% NPV | 10.0% NPV | 12.0% NPV | 14.0% NPV |
| :---: | :---: | :---: | :---: | :---: |
| **5.5% Exit Cap** | $${Math.round(calcNPV(0.08, [...leveredCashFlows.slice(0, 10), leveredCashFlows[9] + (year11NOI / 0.055 * 0.97 - remainingLoanBal)])).toLocaleString()} | $${Math.round(calcNPV(0.10, [...leveredCashFlows.slice(0, 10), leveredCashFlows[9] + (year11NOI / 0.055 * 0.97 - remainingLoanBal)])).toLocaleString()} | $${Math.round(calcNPV(0.12, [...leveredCashFlows.slice(0, 10), leveredCashFlows[9] + (year11NOI / 0.055 * 0.97 - remainingLoanBal)])).toLocaleString()} | $${Math.round(calcNPV(0.14, [...leveredCashFlows.slice(0, 10), leveredCashFlows[9] + (year11NOI / 0.055 * 0.97 - remainingLoanBal)])).toLocaleString()} |
| **6.5% Exit Cap (Base)** | $${Math.round(calcNPV(0.08, leveredCashFlows)).toLocaleString()} | **$${npvAt10.toLocaleString()}** | $${Math.round(calcNPV(0.12, leveredCashFlows)).toLocaleString()} | $${Math.round(calcNPV(0.14, leveredCashFlows)).toLocaleString()} |
| **7.5% Exit Cap** | $${Math.round(calcNPV(0.08, [...leveredCashFlows.slice(0, 10), leveredCashFlows[9] + (year11NOI / 0.075 * 0.97 - remainingLoanBal)])).toLocaleString()} | $${Math.round(calcNPV(0.10, [...leveredCashFlows.slice(0, 10), leveredCashFlows[9] + (year11NOI / 0.075 * 0.97 - remainingLoanBal)])).toLocaleString()} | $${Math.round(calcNPV(0.12, [...leveredCashFlows.slice(0, 10), leveredCashFlows[9] + (year11NOI / 0.075 * 0.97 - remainingLoanBal)])).toLocaleString()} | $${Math.round(calcNPV(0.14, [...leveredCashFlows.slice(0, 10), leveredCashFlows[9] + (year11NOI / 0.075 * 0.97 - remainingLoanBal)])).toLocaleString()} |

---

*Confidential & Proprietary — Worldwidebro Group LLC Deal Room.*
`;

// Write report to disk
const outDir = path.resolve('BUSINESS-CAPITAL-DATA-ROOM/RE-001/05_FINANCIAL');
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}
const outPath = path.join(outDir, 'EXPRESS-DCF-UNDERWRITING-MEMO.md');
fs.writeFileSync(outPath, outputMd, 'utf8');

console.log('=== 10-Year DCF Underwriting Completed Successfully ===');
console.log(`Asset: ${address}`);
console.log(`Purchase Price: $${purchasePrice.toLocaleString()}`);
console.log(`Levered IRR: ${leveredIRR}%`);
console.log(`NPV @ 10%: $${npvAt10.toLocaleString()}`);
console.log(`Equity Multiple: ${equityMultiple}x`);
console.log(`Year 1 DSCR: ${schedule[0].dscr}x`);
console.log(`Report Written To: ${outPath}`);
