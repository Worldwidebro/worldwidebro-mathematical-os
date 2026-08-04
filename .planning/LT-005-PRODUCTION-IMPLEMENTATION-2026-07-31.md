# LT-005 Production Implementation: Services + Frontend Integration

**Status**: Architecture designed, ready for backend build  
**Date**: 2026-07-31  
**Services**: OSRM, Temporal, Socket.io, OpenFGA, Novu  
**Deployment**: Vercel (frontend) + Docker (backend services)

---

## Phase 1: Infrastructure Setup

### 1.1 Local Development (docker-compose.yml - READY ✅)

```bash
# Start all 5 services locally
docker-compose -f docker-compose.yml up -d

# Verify health
curl http://localhost:5000/route/v1/driving/0,0;1,1  # OSRM
curl http://localhost:7233/health                    # Temporal
redis-cli ping                                        # Redis
curl http://localhost:8081/health                    # OpenFGA
curl http://localhost:3001/api/health                # Novu
```

**Services running:**
- OSRM (routing): `localhost:5000`
- Temporal (workflows): `localhost:7233` + UI at `localhost:8080`
- Redis (cache/pub-sub): `localhost:6379`
- OpenFGA (permissions): `localhost:8081`
- Novu (notifications): `localhost:3001`

---

## Phase 2: Laravel Backend Integration (App Architecture)

### 2.1 Database Schema (PostgreSQL migrations)

```sql
-- Pickups Table
CREATE TABLE pickups (
  id UUID PRIMARY KEY,
  customer_id UUID NOT NULL,
  pickup_address JSONB,
  delivery_address JSONB,
  specimen_type VARCHAR(50),
  priority ENUM('STANDARD', 'STAT') DEFAULT 'STANDARD',
  status ENUM('REQUESTED', 'ASSIGNED', 'IN_TRANSIT', 'DELIVERED') DEFAULT 'REQUESTED',
  driver_id UUID,
  eta_minutes INT,
  distance_km FLOAT,
  cost DECIMAL(10,2),
  route_polyline JSONB,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Drivers Table
CREATE TABLE drivers (
  id UUID PRIMARY KEY,
  name VARCHAR(255),
  phone VARCHAR(20),
  vehicle_id UUID,
  status ENUM('AVAILABLE', 'IN_TRANSIT', 'BREAK', 'OFFLINE'),
  current_location POINT,
  assignments_today INT,
  total_miles FLOAT,
  created_at TIMESTAMP
);

-- Compliance Logs (Audit Trail)
CREATE TABLE compliance_logs (
  id UUID PRIMARY KEY,
  pickup_id UUID,
  event_type VARCHAR(100),
  actor_id UUID,
  actor_role VARCHAR(50),
  timestamp TIMESTAMP,
  details JSONB
);

-- Notifications Log (Novu tracking)
CREATE TABLE notification_logs (
  id UUID PRIMARY KEY,
  recipient_id UUID,
  notification_type VARCHAR(50),
  channel ENUM('EMAIL', 'SMS', 'PUSH', 'IN_APP'),
  status ENUM('SENT', 'DELIVERED', 'FAILED'),
  sent_at TIMESTAMP
);
```

### 2.2 Service Classes (app/Services/)

**RoutingService.php** - OSRM Integration
```php
class RoutingService {
  public function getRoute($from, $to)      // Get distance, ETA, polyline
  public function getETA($current, $dest)   // Real-time ETA
  public function getMatrix($locations)     // Multi-stop optimization
}
```

**WorkflowService.php** - Temporal Integration
```php
class WorkflowService {
  public function startDispatchWorkflow($pickup_id)    // Dispatch workflow
  public function logAuditEvent($event)                // Compliance logging
  public function getWorkflowStatus($workflow_id)      // Workflow status
}
```

**NotificationService.php** - Novu Integration
```php
class NotificationService {
  public function sendPickupConfirmed($pickup_id)  // Customer confirmation
  public function notifyDriver($driver_id, $job)   // Driver assignment
  public function sendDeliveryProof($pickup_id)    // Proof of delivery
}
```

**PermissionService.php** - OpenFGA Integration
```php
class PermissionService {
  public function canViewShipment($user_id, $shipment_id)    // Fine-grained access
  public function canEditPickup($user_id, $pickup_id)        // Modify permissions
  public function addAuditLog($action, $user_id, $resource)  // HIPAA compliance
}
```

**RealtimeService.php** - Socket.io Integration
```php
class RealtimeService {
  public function broadcastDriverLocation($driver_id, $location)  // Live map
  public function broadcastPickupStatus($pickup_id, $status)      // Order updates
  public function notifyCustomer($pickup_id, $message)            // Push notification
}
```

### 2.3 API Routes (routes/api.php)

```php
Route::post('/pickups/book', [PickupController::class, 'book']);
  // Payload: { customer_id, from, to, specimen_type, priority }
  // Returns: { pickup_id, eta_minutes, cost, route }
  // Triggers: Temporal workflow

Route::get('/pickups/{id}/route', [TrackingController::class, 'getRoute']);
  // Returns real-time route + ETA from OSRM

Route::post('/dispatch/assign', [DispatchController::class, 'assign']);
  // Payload: { pickup_id, driver_id }
  // Sends SMS/email via Novu
  // Broadcasts via Socket.io

Route::get('/permissions/check', [PermissionController::class, 'check']);
  // Fine-grained access check via OpenFGA
  // Logs to compliance_logs

Route::get('/shipments/{id}/track', [TrackingController::class, 'track']);
  // Real-time tracking (via Socket.io subscription)
  // Route + ETA + driver location
```

---

## Phase 3: Frontend Integration (Updated Pages)

### 3.1 Critical 14 Pages (for revenue)

| Page | Service | Real-Time | Data |
|------|---------|-----------|------|
| Book Pickup | OSRM + Temporal | No | Distance, ETA, cost |
| Dispatcher Map | Socket.io + OSRM | YES | Driver locations, routes, queue |
| Driver Jobs | Temporal + Socket.io | YES | Assigned jobs, navigation, POD |
| Customer Tracking | Socket.io + OSRM | YES | Driver location, ETA, status |
| Invoice | Stripe (already set) | No | Line items, total, payment |
| Help Center | Novu + (search) | No | FAQ, contact form |
| Compliance Report | Compliance logs | No | Audit trail, certifications |

### 3.2 React Components (Updated)

**DispatcherMap.jsx** - Real-time tracking
```jsx
import io from 'socket.io-client';

export default function DispatcherMap() {
  const socket = io(process.env.VITE_SOCKET_IO_URL);
  
  useEffect(() => {
    // Subscribe to driver locations
    socket.on('driver:location', (data) => {
      updateMapMarker(data.driver_id, data.location);
      updateETA(data.driver_id);
    });
    
    // Subscribe to pickup status changes
    socket.on('pickup:status', (pickup) => {
      updateQueueDisplay(pickup);
    });
  }, []);
  
  const assignDriver = async (pickup, driver) => {
    const res = await fetch('/api/dispatch/assign', {
      method: 'POST',
      body: JSON.stringify({ pickup_id: pickup.id, driver_id: driver.id })
    });
    // Socket.io automatically broadcasts driver assignment
  };
}
```

**BookPickup.jsx** - Real-time pricing + ETA
```jsx
import { useQuery } from '@tanstack/react-query';

export default function BookPickup() {
  const [from, setFrom] = useState(null);
  const [to, setTo] = useState(null);

  // Query OSRM for distance/ETA
  const { data: route } = useQuery({
    queryKey: ['route', from, to],
    queryFn: () => fetch(`/api/route?from=${from}&to=${to}`).then(r => r.json()),
    enabled: from && to,
  });

  const handleBook = async () => {
    // POST to /api/pickups/book
    // Triggers Temporal workflow
    // Customer receives SMS/email via Novu
  };

  return (
    <form onSubmit={handleBook}>
      <input placeholder="Pickup address" value={from} onChange={e => setFrom(e.target.value)} />
      <input placeholder="Delivery address" value={to} onChange={e => setTo(e.target.value)} />
      
      {route && (
        <>
          <p>Distance: {route.distance_km} km</p>
          <p>ETA: {route.duration_minutes} minutes</p>
          <p>Estimated cost: ${route.cost}</p>
        </>
      )}
      
      <button type="submit">Book Pickup</button>
    </form>
  );
}
```

**CustomerTracking.jsx** - Live tracking
```jsx
export default function CustomerTracking({ pickupId }) {
  const [pickup, setPickup] = useState(null);
  const [driverLocation, setDriverLocation] = useState(null);
  
  useEffect(() => {
    const socket = io(process.env.VITE_SOCKET_IO_URL);
    
    // Subscribe to this pickup's updates
    socket.on(`pickup:${pickupId}:status`, (data) => {
      setPickup(data);
    });
    
    socket.on(`driver:${pickup?.driver_id}:location`, (location) => {
      setDriverLocation(location);
    });
  }, [pickupId]);

  return (
    <div>
      <h2>Your Delivery</h2>
      <p>Status: {pickup?.status}</p>
      <p>Driver: {pickup?.driver_name}</p>
      <p>ETA: {pickup?.eta_minutes} minutes</p>
      <Map driverLocation={driverLocation} route={pickup?.route_polyline} />
    </div>
  );
}
```

---

## Phase 4: Cross-Venture Benefits

### 4.1 Which Ventures Share This Infrastructure

**LT-005 (Medical Courier)** - PRIMARY  
✓ OSRM (route planning)  
✓ Temporal (dispatch workflows, cold-chain compliance)  
✓ Socket.io (real-time tracking)  
✓ OpenFGA (HIPAA access control)  
✓ Novu (delivery notifications)  

**LT-011 (Fleet Management)**  
✓ OSRM (fleet optimization)  
✓ Socket.io (vehicle status tracking)  
✓ Temporal (maintenance workflows)  

**STA-001 (Staffing/Dispatch)**  
✓ OSRM (worker location/routing)  
✓ Temporal (assignment workflows)  
✓ Socket.io (real-time availability)  
✓ Novu (shift notifications)  

**CON-001 (Construction)**  
✓ OSRM (crew routing to job sites)  
✓ Temporal (project workflows)  
✓ OpenFGA (site access control)  

**EC-112 (E-commerce Delivery)**  
✓ OSRM (delivery optimization)  
✓ Socket.io (order tracking)  
✓ Novu (customer notifications)  

**RE-001 (Real Estate)**  
✓ OSRM (agent routing)  
✓ Socket.io (showing live property tours)  
✓ Novu (appointment reminders)  

**Cost savings:** Infrastructure built once, shared by 6+ ventures = 60-80% cost reduction per venture.

---

## Phase 5: Deployment Strategy

### 5.1 Local Development
```bash
docker-compose up -d
npm install
npm run dev
# Open http://localhost:3000
```

### 5.2 Production Deployment

**Backend Services (Docker):**
```bash
# Deploy to AWS ECS / Digital Ocean / Railway
docker build -f Dockerfile -t medcourierios:latest .
docker-compose -f docker-compose.prod.yml up -d
```

**Frontend (Vercel):**
```bash
# Already deployed: lt-005-deploy-temp.vercel.app
# Update env vars in Vercel Dashboard:
VITE_SOCKET_IO_URL=https://api.medcourierios.com
OSRM_API_URL=https://routing.medcourierios.com
```

**Database (Supabase):**
- Use existing Supabase project for production database
- PostgreSQL auto-manages pickups, drivers, compliance_logs

---

## Phase 6: Employee + Customer Workflows

### 6.1 Employee Workflow (Dispatcher)

1. **Morning Start**
   - Open dispatcher map
   - See all drivers online (via Socket.io)
   - View pending pickups in queue (via Temporal)

2. **Incoming Pickup (Real-time)**
   - Customer books via BookPickup page
   - Temporal workflow triggered
   - Dispatcher notified via Socket.io
   - Queue updates in real-time

3. **Dispatch Assignment**
   - Click "Assign to Driver"
   - OpenFGA checks permission (must be dispatcher)
   - Temporal workflow executes:
     - Calculate optimal route (OSRM)
     - Create delivery job
     - Send SMS to driver (Novu)
     - Log to compliance_logs (HIPAA)
     - Broadcast assignment via Socket.io

4. **Monitor & Optimize**
   - Watch driver locations on map
   - See ETAs update in real-time
   - Change assignments if needed (Temporal handles cancellation)

### 6.2 Customer Workflow

1. **Book Pickup (BookPickup page)**
   - Enter pickup/delivery addresses
   - System calculates distance + ETA + price (OSRM)
   - Pay with Stripe
   - Receive SMS confirmation + tracking link (Novu)

2. **Real-time Tracking (CustomerTracking page)**
   - Open tracking link
   - See driver location on map (Socket.io)
   - See estimated arrival (OSRM)
   - Receive SMS when driver is 5 min away (Novu workflow)

3. **Proof of Delivery**
   - Driver scans barcode (mobile app)
   - Takes photo
   - Gets customer signature
   - Sends to backend
   - Customer receives email confirmation + receipt (Novu)

---

## Phase 7: Revenue Activation

### 7.1 Minimum Viable Operations
- ✅ Customers can book (BookPickup)
- ✅ Get real-time pricing (OSRM)
- ✅ Employees dispatch drivers (Dispatcher + Temporal)
- ✅ Customers track (CustomerTracking + Socket.io)
- ✅ Billing works (Stripe)
- ✅ Compliance logged (OpenFGA + Temporal)
- ✅ Notifications sent (Novu)

**Timeline:** 2 weeks backend + 1 week testing = ready for customers by mid-August

### 7.2 First Customer Workflows
- Health clinic in Charlotte
- 5-10 pickups/day
- Standard + STAT priority
- Real-time tracking
- Weekly invoicing

**Revenue target:** $2K-3K first month → $10K+ by month 3

---

## Rollout Checklist

- [ ] Docker services running locally (OSRM, Temporal, Redis, OpenFGA, Novu)
- [ ] PostgreSQL migrations applied (pickups, drivers, compliance_logs)
- [ ] Laravel routes + services built (Routing, Workflow, Notification, Permission)
- [ ] React pages updated (BookPickup, DispatcherMap, CustomerTracking)
- [ ] Socket.io wired for real-time updates
- [ ] Stripe + Novu credentials configured
- [ ] Employee onboarding (dispatcher training)
- [ ] First customer onboarding
- [ ] Go live

---

**Next Steps:** Build Laravel backend (2 weeks) → Deploy services → Update 14 pages → Testing → Customer launch
