# Real Job Scraping Toolkit
## Complete Guide to Scrape 200+ Real Jobs from 6 Platforms

**Date Created:** June 6, 2026  
**Status:** Ready to Execute  
**Expected Outcome:** 200-400 real job listings with actual company names, salaries, and URLs  
**Time to Complete:** 2-3 hours

---

## 🎯 OBJECTIVE

Replace template framework with **REAL CURRENT JOB LISTINGS** from actual platforms.

**Current State:** Template documents with search links  
**Target State:** 200-400 real jobs with company names, salaries, URLs

---

## 📊 SCRAPING PLATFORMS (Priority Order)

### **TIER 1: High Priority**

#### 1. **Angel List (angel.co/jobs)**
**Why First:** Startup-focused, shows salary + equity, no auth needed

**Process:**
1. Visit: https://angel.co/jobs
2. Filter: "Seed", "Series A", "Series B"
3. Search terms:
   - "Operations Manager" → Extract 30-40 jobs
   - "Customer Success Manager" → Extract 30-40 jobs
   - "Sales Representative" → Extract 20-30 jobs
   - "Project Manager" → Extract 15-25 jobs

**Data to Extract per Job:**
```
Platform | Job Title | Company | Salary Min | Salary Max | Equity % | URL | Posted Date | Category
```

**Expected:** 80-110 real jobs

#### 2. **Remote OK (remoteok.ie)**
**Process:**
1. Visit: https://remoteok.ie/jobs
2. Search: "operations", "customer success", "sales", "project manager"
3. Extract: Title, Company, Salary, URL, Date

**Expected:** 40-55 real jobs

#### 3. **We Work Remotely (weworkremotely.com/jobs)**
**Process:**
1. Visit: https://weworkremotely.com/jobs
2. Search: "customer success", "sales", "operations"
3. Extract: Title, Company, Salary, URL, Date

**Expected:** 40-55 real jobs

### **TIER 2: Secondary (Bonus)**
- Remotive: 20-30 jobs
- Remote.co: 15-20 jobs
- Skip the Drive: 15-20 jobs
- **Tier 2 Total:** 50-70 jobs

**GRAND TOTAL: 200-300 REAL JOBS**

---

## 🛠️ THREE SCRAPING METHODS

### **Method 1: Manual (2-3 hours, fastest)**
- Open each site in browser
- Search and copy jobs into Google Sheet
- Clean up formatting
- Export to CSV

### **Method 2: Python Script (3-4 hours)**
- Write Selenium/Playwright script
- Automate job extraction
- Clean data
- Export to CSV

### **Method 3: BrowserOS (2-3 hours, integrated)**
- Use Browser automation in Claude Code
- Navigate sites
- Screenshot and extract
- Parse into CSV

---

## 📋 CSV TEMPLATE

```csv
Platform,Job_Rank,Job_Title,Company_Name,Salary_Min,Salary_Max,Equity,Job_URL,Posted_Date,Role_Category,Description
Angel List,1,Operations Manager,StartupXYZ,100000,130000,0.2%,https://angel.co/jobs/123,2026-06-05,operations,Operations Manager for seed-stage
Remote OK,2,Customer Success Manager,SaaSCorp,110000,140000,,https://remoteok.io/jobs/456,2026-06-04,customer_success,CSM for SaaS platform
We Work Remotely,3,Sales Representative,TechInc,80000,120000,,https://weworkremotely.com/jobs/789,2026-06-03,sales,B2B Sales Representative
```

---

## ⏱️ EXECUTION TIMELINE

| Phase | Task | Time | Jobs |
|-------|------|------|------|
| 1 | Set up spreadsheet | 15 min | - |
| 2 | Angel List scraping | 40 min | 80-110 |
| 3 | Remote OK scraping | 30 min | 40-55 |
| 4 | We Work Remotely | 30 min | 40-55 |
| 5 | Secondary sites | 30 min | 50-70 |
| 6 | Clean & deduplicate | 15 min | 200-300 |
| 7 | Update GitHub | 30 min | Done |
| **TOTAL** | **Real job data live** | **2.5-3 hours** | **200-300** |

---

## ✅ AFTER SCRAPING: UPDATE GITHUB

1. **Create:** `REAL-JOBS-SCRAPED-[DATE].csv` (200-300 jobs)
2. **Update:** `200-REMOTE-POSITIONS-ORGANIZED.md` with real company names
3. **Update:** `JOB-APPLICATION-PRIORITY-ORDER.md` with real URLs
4. **Update:** `APPLICATIONS-TRACKER.csv` with actual job links
5. **Commit to GitHub:**
   ```bash
   git add REAL-JOBS-SCRAPED-*.csv
   git commit -m "feat: Add 200+ real job listings from Angel List, Remote OK, We Work Remotely"
   git push
   ```

---

## 🎯 SUCCESS CRITERIA

After 3 hours, you should have:
- ✅ 200-300 real jobs
- ✅ Actual company names (not templates)
- ✅ Real salary ranges
- ✅ Working apply URLs
- ✅ Updated GitHub documents
- ✅ Antwuan ready to apply to REAL opportunities

---

## 📌 RECOMMENDATION

**Fastest method: Manual scraping with Google Sheet**
- Copy jobs as you find them
- Takes 2-3 hours for 200+ jobs
- No coding needed
- Results immediately usable

Start with Angel List (best data), then Remote OK, then We Work Remotely.

**Ready to start?** You have the framework and platform list. Begin with Angel List.
