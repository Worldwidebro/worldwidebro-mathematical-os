# Analytics: Media Performance & Retention Scoring

This document defines the metrics, mathematical formulas, and analytics schemas used to measure content virality and routing efficiency.

---

## 1. Key Performance Indicators (KPIs)

Our media engine optimizes for four core metrics:

```text
1. Hook Rate ➔ 2. Retention Rate ➔ 3. Engagement Rate ➔ 4. Lead Conversion Rate
```

### A. Hook Rate (Stop-Scroll Power)
- **Definition**: The percentage of viewers who watch the first 3 seconds of the video.
- **Formula**:
  \[\text{Hook Rate} = \frac{\text{3-Second Views}}{\text{Total Impressions}} \times 100\]
- **Benchmarks**:
  - **Fail**: < 40% (Weak hook, poor visual pattern interrupt)
  - **Good**: 50% - 65% (Strong text/visual trigger)
  - **Excellent**: > 70% (Viral potential)

### B. Retention Rate (Content Quality)
- **Definition**: The percentage of viewers who watch the video until the end (Completion Rate) or average watch time.
- **Formula**:
  \[\text{Completion Rate} = \frac{\text{Completed Video Views}}{\text{Total Impressions}} \times 100\]
- **Benchmarks**:
  - **Fail**: < 15% (Audience drops off early, boring middle section)
  - **Good**: 20% - 35% (Good pacing and micro-transitions)
  - **Excellent**: > 40% (Superb pacing, open loops executed well)

### C. Engagement Rate
- **Formula**:
  \[\text{Engagement Rate} = \frac{\text{Likes} + \text{Comments} + \text{Shares} + \text{Saves}}{\text{Total Views}} \times 100\]
- **Significance**: Comments and saves tell the algorithm the content is highly valuable. Saves indicate utility; comments indicate controversy or curiosity.

### D. Lead Conversion Rate (LCR)
- **Formula**:
  \[\text{LCR} = \frac{\text{Lead Magnet Signups}}{\text{Unique Profile Visitors}} \times 100\]
- **Goal**: > 10% conversion from profile visit to email lead.

---

## 2. Feedback Routing Schema

The dashboard's `REVENUE-ANALYTICS` ingestion script listens for these numbers. Any video that exceeds an **Overall Score (OS)** of 85 (where $OS = 0.4 \times \text{Hook Rate} + 0.6 \times \text{Completion Rate}$) is automatically sent to the `PRODUCT-VALIDATION` engine as a greenlight to spin up relevant digital or affiliate products.
