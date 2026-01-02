# Samsara + NextPhone: Fleet Management Integration

**Key Takeaways:**

- Route emergency calls to the nearest available technician using Samsara GPS data
- AI checks technician locations and availability before dispatching
- Reduce response times by sending the closest truck instead of random assignment
- Track which technician took which call for better fleet coordination
- Integrate call data with Samsara's fleet management dashboard

## Dispatch Smarter with GPS-Based Call Routing

Customer calls with an emergency HVAC repair. You have five technicians in the field. Who do you send?

Without fleet data, you guess. "Let me check who's available..." You call or text each tech. Five minutes later, you assign someone who's 30 minutes awaywhen another tech was 10 minutes from the customer.

[Samsara](https://www.samsara.com/) tracks your fleet in real-timeGPS locations, route status, job completion. But that data doesn't automatically connect to your incoming calls.

With NextPhone + Samsara integration, emergency calls can trigger smart routing: AI checks which technicians are nearby, idle, and available, then dispatches the closest one. Faster response times, happier customers, more efficient fleet use.

## Why Integrate Your Phone System with Samsara

Fleet-based service businesses (HVAC, plumbing, electrical, landscaping) run on efficiency. Send the wrong truck, and you waste time and fuel.

### Route to Nearest Technician

Traditional dispatch:

- Call comes in for emergency repair
- Dispatcher looks at board or calls techs: "Where are you?"
- Guesses who's closest
- Assigns job
- Tech drives 25 minutes when another tech was 8 minutes away

With Samsara integration:

- Call comes in
- NextPhone queries Samsara API for tech locations
- Identifies nearest available tech via GPS
- Auto-assigns or suggests to dispatcher
- Tech gets job notification
- Customer gets accurate ETA

Result: Faster response, lower fuel costs, more jobs completed per day.

### Reduce Empty Drive Time

Every minute a tech spends driving between jobs is a minute they're not billing. GPS-based routing minimizes drive time.

Example: Tech finishes job at Location A. Call comes in from Location B (5 miles away) and Location C (18 miles away). Samsara knows Tech is at Location A. NextPhone routes Location B call to that tech, Location C to someone closer.

Over a month, this saves hours of drive time = more billable hours.

### Track Call-to-Job Pipeline

Samsara tracks job completion. NextPhone tracks calls. Integration connects them.

You can see:

- Which calls turned into jobs
- How long from call to dispatch
- Which techs handle which call types
- Response time metrics by technician

Data drives optimization. "Tech #3 has fastest response time on plumbing callsprioritize those for him."

## How NextPhone + Samsara Integration Works

Samsara has APIs for vehicle tracking, driver info, and route data. NextPhone queries this data when routing calls.

### The Integration Flow

1. Emergency call comes in ’ NextPhone AI answers
2. AI collects: Customer location, problem type, urgency
3. During or after call, webhook queries Samsara API: "Which techs are nearby and available?"
4. Samsara returns: GPS locations of all fleet vehicles, current status (en route, idle, on job)
5. NextPhone calculates: Drive time from each tech to customer location
6. AI or dispatcher assigns nearest tech
7. Notification sent to tech via Samsara device or SMS
8. Customer gets SMS: "Technician John is 12 minutes away"

All automated. No manual GPS checking.

### What Data Gets Shared

**From NextPhone to Samsara:**

- Call details (customer name, location, problem)
- Job priority (emergency vs routine)
- Timestamp

**From Samsara to NextPhone:**

- Vehicle locations (GPS coordinates)
- Driver/technician names
- Current status (available, busy, en route)
- Estimated drive times

This bidirectional data flow enables smart routing.

## Setup Guide: Connect NextPhone to Samsara

### Step 1: Get Samsara API Access

Log into Samsara dashboard ’ Admin ’ API Tokens. Generate a new API token with permissions:

- Read vehicle locations
- Read driver info
- Create jobs (if auto-dispatching)

Copy the API token.

### Step 2: Configure NextPhone to Query Samsara

In NextPhone ’ Integrations ’ Custom Functions ’ Add New.

**Function Name:** "Find Nearest Tech"

**Trigger:** "Before routing call"

**API Call:**

- **Method:** GET
- **URL:** `https://api.samsara.com/v1/fleet/vehicles/locations`
- **Headers:** `Authorization: Bearer YOUR_SAMSARA_API_TOKEN`

**Response Processing:** Parse GPS locations and calculate distances to customer location.

### Step 3: Set Up Call Routing Logic

Configure NextPhone's routing rules:

- **Emergency calls:** Auto-assign to nearest available tech
- **Routine calls:** Suggest 3 nearest techs, let dispatcher choose
- **Scheduled calls:** Add to queue for manual assignment

### Step 4: Test with Sample Call

Make test call with customer location. Check that NextPhone queries Samsara and identifies nearest tech correctly.

## Use Cases for Fleet-Based Businesses

### HVAC Companies with Multi-Truck Fleets

**Scenario:** 8 HVAC techs covering a metro area. Emergency call: "AC stopped working, 95-degree heat."

**Workflow:**

- AI answers, collects address
- Queries Samsara: Tech #4 is 6 minutes away and just finished a job
- Auto-assigns to Tech #4
- Customer gets SMS: "Technician arriving in 8 minutes"

**Benefit:** Fastest possible response = higher customer satisfaction = more reviews.

### Plumbing Services

**Scenario:** Burst pipe emergency, need immediate response.

**Workflow:**

- Call comes in with address
- Samsara shows 2 techs nearby
- Tech #1 is on another emergency (status: busy)
- Tech #2 is returning from supply run (status: available)
- Assigns Tech #2

**Benefit:** Correct tech assigned first try, no wasted calls checking availability.

### Electrical Contractors

**Scenario:** Multiple service calls throughout the day, need to optimize routing.

**Workflow:**

- As calls come in, they're queued
- System looks at all tech locations and pending jobs
- Assigns calls to minimize total drive time
- Techs complete more jobs per day

**Benefit:** 15-20% more billable hours per tech from better routing.

## Benefits of Samsara + Phone Integration

### Faster Response Times

Emergency service businesses compete on speed. Telling a customer "We'll be there in 15 minutes" vs "an hour or two" wins the job.

GPS routing ensures you can quote accurate, fast ETAs because you're sending the closest tech, not guessing.

### Lower Fuel Costs

Unnecessary drive time = wasted fuel. At $3.50/gallon and 15 MPG for work trucks, every 10 extra miles costs $2.33.

If you prevent just 100 unnecessary miles per week through better routing, that's $1,200/year in fuel savings.

### More Jobs Per Day

Techs spend less time driving between jobs, more time actually working. A tech who completes 4 jobs/day can complete 5 with optimized routing.

5 jobs/day × $200 average = $1,000/day per tech. Over a year, that's significant revenue increase.

### Better Fleet Utilization

See which techs are busiest, which trucks are underutilized, which routes are inefficient. Data from call logs + Samsara GPS = insights for fleet optimization.

## How NextPhone Makes Fleet Management Easier

### Real-Time GPS Queries

NextPhone queries Samsara in real-time during calls. No stale data. You get current locations, not where techs were 15 minutes ago.

### Smart Routing Algorithms

NextPhone calculates drive times using actual routes (not straight-line distance). Factors in traffic, road types, and current vehicle locations.

Result: Accurate ETA predictions, better dispatch decisions.

### Works with Your Existing Samsara Setup

No need to change how you use Samsara. NextPhone integrates via APIyour fleet tracking workflows stay the same.

At $199/month for NextPhone + Samsara's existing cost, you add smart call routing without expensive custom development.

## Frequently Asked Questions

### Does this work with Samsara's routing feature?

Yes. NextPhone handles incoming calls and initial routing. Samsara optimizes multi-stop routes throughout the day. They complement each other.

### Can I override automatic assignments?

Yes. Configure routing as "suggest nearest tech" instead of "auto-assign." Dispatcher sees the recommendation but can manually choose a different tech if needed (e.g., specific expertise required).

### What if no techs are nearby?

NextPhone can escalate:

- Show all techs ranked by distance
- Alert dispatcher to assign manually
- Offer callback scheduling if no one's available soon

You control the fallback logic.

## Start Routing Calls Smarter

Fleet management and phone calls shouldn't be separate systems. When a customer calls, you need to know where your techs are right nownot guess and call around.

Connect NextPhone to Samsara, and every incoming call becomes an opportunity for optimized dispatch. Nearest tech gets the job. Customer gets fastest ETA. You complete more jobs per day.

[Start your free 14-day trial of NextPhone](https://getnextphone.com/trial) and connect Samsara today.

---

**URL Slug:** `/blog/samsara-nextphone-integration`
