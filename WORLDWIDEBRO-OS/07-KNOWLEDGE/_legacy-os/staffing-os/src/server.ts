import express, { Express, Request, Response } from "express";
import cors from "cors";
import dotenv from "dotenv";
import { PrismaClient } from "@prisma/client";

dotenv.config();

const app: Express = express();
const prisma = new PrismaClient();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.get("/", (req: Request, res: Response) => {
  res.json({ message: "Staffing OS API - Production Ready" });
});

// Worker Routes
app.post("/api/workers", async (req: Request, res: Response) => {
  try {
    const { fullName, phone, email, skills, hourlyRate } = req.body;
    const worker = await prisma.worker.create({
      data: {
        fullName,
        phone,
        email,
        skills,
        hourlyRate: parseFloat(hourlyRate),
      },
    });
    res.json(worker);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

app.get("/api/workers", async (req: Request, res: Response) => {
  try {
    const workers = await prisma.worker.findMany();
    res.json(workers);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

app.get("/api/workers/available", async (req: Request, res: Response) => {
  try {
    const workers = await prisma.worker.findMany({
      where: { status: "active" },
      include: { placements: true },
    });
    res.json(workers);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

// Job Routes
app.post("/api/jobs", async (req: Request, res: Response) => {
  try {
    const { title, location, skillsNeeded, billRate, duration, clientId } =
      req.body;
    const job = await prisma.job.create({
      data: {
        title,
        location,
        skillsNeeded,
        billRate: parseFloat(billRate),
        duration,
        clientId,
      },
    });
    res.json(job);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

app.get("/api/jobs", async (req: Request, res: Response) => {
  try {
    const jobs = await prisma.job.findMany({
      include: { client: true, placements: true },
    });
    res.json(jobs);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

// Placement Routes (Matching)
app.post("/api/placements", async (req: Request, res: Response) => {
  try {
    const { workerId, jobId } = req.body;
    const placement = await prisma.placement.create({
      data: { workerId, jobId },
      include: { worker: true, job: true },
    });
    res.json(placement);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

// Timesheet Routes
app.post("/api/timesheets", async (req: Request, res: Response) => {
  try {
    const { workerId, placementId, date, hours, notes } = req.body;
    const timesheet = await prisma.timesheet.create({
      data: {
        workerId,
        placementId,
        date: new Date(date),
        hours: parseFloat(hours),
        notes,
      },
    });
    res.json(timesheet);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

// Commission Routes
app.post("/api/commissions", async (req: Request, res: Response) => {
  try {
    const { referralId, serviceType, amount } = req.body;
    const commission = await prisma.commission.create({
      data: {
        referralId,
        serviceType,
        amount: parseFloat(amount),
      },
    });
    res.json(commission);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

app.get("/api/commissions/pending", async (req: Request, res: Response) => {
  try {
    const commissions = await prisma.commission.findMany({
      where: { status: "pending" },
    });
    res.json(commissions);
  } catch (error) {
    res.status(400).json({ error: String(error) });
  }
});

// Error handler
app.use((err: Error, req: Request, res: Response) => {
  console.error(err);
  res.status(500).json({ error: "Internal server error" });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

export default app;
