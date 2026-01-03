# AI Receptionist API Integration Tutorial for Developers

**Meta Title:** AI Receptionist API Tutorial: Build Custom Integrations 2025

**Meta Description:** Build custom AI phone integrations with HTTP webhooks. Authenticate with API keys, handle real-time events, implement CRM sync and SMS follow-up.

**Key Takeaways:**

- Build custom integrations with NextPhone's HTTP webhook system
- Authenticate securely using API keys and Bearer tokens
- Handle real-time call events with POST webhooks to your endpoints
- Support common patterns: CRM sync, email automation, SMS follow-up
- Implement proper error handling, retries, and logging for production reliability

## Build Custom Integrations for AI Phone Systems

You're building a custom workflow: When customers call requesting product demos, you want to automatically:

1. Create a lead in your CRM
2. Send confirmation email
3. Add them to a Slack channel
4. Trigger a custom notification to your sales team

Most AI receptionist platforms force you through Zapier or limited pre-built integrations. NextPhone gives developers direct HTTP webhook access to build whatever you need.

This tutorial shows how to integrate an AI receptionist API with your custom systems using webhooks, proper authentication, and production-ready error handling.

## API Authentication

NextPhone uses API keys for authentication. Every webhook request includes an authorization header that your endpoint should verify.

### Getting Your API Key

Log into NextPhone dashboard � Settings � API Keys � Generate New Key.

You'll get an API key in this format:

```
np_live_abc123def456ghi789jkl012mno345
```

Store this securelytreat it like a password. Never commit it to public repos.

### Authenticating Incoming Webhooks

When NextPhone sends webhook requests to your endpoint, it includes:

```http
Authorization: Bearer np_live_abc123def456ghi789jkl012mno345
X-NextPhone-Signature: sha256=...
```

**Verify the signature** to ensure requests actually come from NextPhone and haven't been tampered with.

**Example verification (Node.js):**

```javascript
const crypto = require('crypto');

function verifyNextPhoneSignature(req, secret) {
  const signature = req.headers['x-nextphone-signature'];
  const payload = JSON.stringify(req.body);

  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  return `sha256=${expectedSignature}` === signature;
}

// In your webhook handler
app.post('/webhook/nextphone', (req, res) => {
  if (!verifyNextPhoneSignature(req, process.env.NEXTPHONE_SECRET)) {
    return res.status(401).send('Invalid signature');
  }

  // Process webhook...
});
```

This prevents attackers from sending fake webhook requests to your endpoint.

### Authenticating Outbound API Calls

If you're calling NextPhone's API (to create calls, update settings, etc.), include your API key:

```http
GET /api/v1/calls
Authorization: Bearer np_live_abc123def456ghi789jkl012mno345
```

**Example (Python):**

```python
import requests

API_KEY = 'np_live_abc123def456ghi789jkl012mno345'
headers = {'Authorization': f'Bearer {API_KEY}'}

response = requests.get(
    'https://api.getnextphone.com/v1/calls',
    headers=headers
)
```

## Webhook Setup

Webhooks let NextPhone send real-time call data to your server as events happen.

### Creating a Webhook Endpoint

Your server needs an HTTPS endpoint that accepts POST requests.

**Example endpoint (Express.js):**

```javascript
const express = require('express');
const app = express();

app.use(express.json());

app.post('/webhook/nextphone', async (req, res) => {
  const { event, data } = req.body;

  try {
    switch (event) {
      case 'call.ended':
        await handleCallEnded(data);
        break;
      case 'call.answered':
        await handleCallAnswered(data);
        break;
      case 'message.collected':
        await handleMessage(data);
        break;
      default:
        console.log(`Unknown event: ${event}`);
    }

    // Always respond 200 OK quickly
    res.status(200).send('OK');
  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).send('Error');
  }
});

app.listen(3000);
```

**Important:** Return `200 OK` within 5 seconds. Do heavy processing asynchronously.

### Webhook Payload Structure

When a call ends, NextPhone sends:

```json
{
  "event": "call.ended",
  "timestamp": "2026-01-02T15:30:00Z",
  "data": {
    "call_id": "call_abc123",
    "caller": {
      "phone": "+15551234567",
      "name": "John Doe",
      "email": "john@example.com"
    },
    "call_type": "quote_request",
    "duration_seconds": 180,
    "transcript": "Full conversation transcript...",
    "ai_summary": "Customer requested quote for kitchen remodel...",
    "custom_fields": {
      "service_type": "remodeling",
      "budget": "$15,000-$20,000",
      "timeline": "next 3 months"
    }
  }
}
```

Your code parses this JSON and takes action.

### Configuring Webhooks in NextPhone

In NextPhone dashboard:

1. Go to Integrations � Webhooks � Add Webhook
2. **Name:** "CRM Lead Sync"
3. **URL:** `https://yourdomain.com/webhook/nextphone`
4. **Events:** Select which events trigger this webhook:
   - `call.answered` - When call connects
   - `call.ended` - When call completes
   - `message.collected` - When voicemail/message left
   - `data.collected` - When AI collects specific info
5. **Method:** POST
6. **Headers:** (Optional) Add custom headers like API keys for your endpoint
7. **Test:** Send test webhook to verify connection

Save and activate.

## Common Integration Patterns

### Pattern 1: CRM Lead Creation

**Goal:** Every call creates a lead in your CRM (Salesforce, HubSpot, custom CRM).

**Implementation:**

```javascript
async function handleCallEnded(callData) {
  // Only create leads for quote requests
  if (callData.call_type !== 'quote_request') return;

  const lead = {
    firstName: callData.caller.name.split(' ')[0],
    lastName: callData.caller.name.split(' ')[1],
    phone: callData.caller.phone,
    email: callData.caller.email,
    source: 'Phone Call',
    notes: callData.ai_summary,
    customFields: {
      serviceType: callData.custom_fields.service_type,
      budget: callData.custom_fields.budget
    }
  };

  // POST to your CRM API
  await axios.post('https://api.yourcrm.com/leads', lead, {
    headers: { 'Authorization': `Bearer ${CRM_API_KEY}` }
  });

  console.log(`Lead created for ${callData.caller.name}`);
}
```

### Pattern 2: Email Automation Trigger

**Goal:** Send automated email after call based on call type.

**Implementation:**

```python
import smtplib
from email.mime.text import MIMEText

def handle_call_ended(call_data):
    caller_email = call_data['caller']['email']
    call_type = call_data['call_type']

    if call_type == 'quote_request':
        subject = "Thanks for your quote request"
        body = f"""
        Hi {call_data['caller']['name']},

        Thanks for calling about {call_data['custom_fields']['service_type']}.

        We'll send you a detailed quote within 24 hours.

        - Your Team
        """
    elif call_type == 'emergency':
        subject = "Emergency service confirmation"
        body = f"Technician dispatched, ETA 20 minutes."
    else:
        return  # No email for other types

    send_email(caller_email, subject, body)

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'noreply@yourdomain.com'
    msg['To'] = to

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.send_message(msg)
    smtp.quit()
```

### Pattern 3: Multi-System Sync

**Goal:** One call triggers updates to multiple systems.

**Implementation:**

```javascript
async function handleCallEnded(callData) {
  // Run integrations in parallel
  await Promise.all([
    createCRMLead(callData),
    sendConfirmationEmail(callData),
    postToSlack(callData),
    updateGoogleSheets(callData),
    logToAnalytics(callData)
  ]);
}

async function postToSlack(callData) {
  const message = {
    text: `New ${callData.call_type} call from ${callData.caller.name}`,
    blocks: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `*${callData.caller.name}* called\nPhone: ${callData.caller.phone}\nType: ${callData.call_type}\nSummary: ${callData.ai_summary}`
        }
      }
    ]
  };

  await axios.post(SLACK_WEBHOOK_URL, message);
}
```

## Error Handling

Production webhooks need robust error handling.

### Retry Logic

NextPhone automatically retries failed webhooks (3 attempts with exponential backoff). Your endpoint should be idempotentprocessing the same webhook twice shouldn't cause problems.

**Idempotency key pattern:**

```javascript
const processedCalls = new Set();  // Or use database

app.post('/webhook/nextphone', async (req, res) => {
  const callId = req.body.data.call_id;

  // Check if already processed
  if (processedCalls.has(callId)) {
    console.log(`Call ${callId} already processed`);
    return res.status(200).send('OK');
  }

  try {
    await handleCallEnded(req.body.data);
    processedCalls.add(callId);
    res.status(200).send('OK');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error');
  }
});
```

### Timeout Handling

Set timeouts for external API calls:

```javascript
async function createCRMLead(callData) {
  try {
    const response = await axios.post(CRM_API_URL, callData, {
      timeout: 5000  // 5 second timeout
    });
    return response.data;
  } catch (error) {
    if (error.code === 'ECONNABORTED') {
      console.error('CRM API timeout');
      // Queue for retry or alert admin
    } else {
      console.error('CRM API error:', error.message);
    }
    throw error;
  }
}
```

### Logging & Monitoring

Log all webhook activity:

```javascript
app.post('/webhook/nextphone', async (req, res) => {
  const { event, data } = req.body;

  console.log(JSON.stringify({
    timestamp: new Date().toISOString(),
    event,
    callId: data.call_id,
    caller: data.caller.phone,
    status: 'received'
  }));

  try {
    await processWebhook(event, data);

    console.log(JSON.stringify({
      timestamp: new Date().toISOString(),
      callId: data.call_id,
      status: 'processed'
    }));

    res.status(200).send('OK');
  } catch (error) {
    console.error(JSON.stringify({
      timestamp: new Date().toISOString(),
      callId: data.call_id,
      status: 'error',
      error: error.message
    }));

    res.status(500).send('Error');
  }
});
```

Use a logging service (Logtail, Datadog, CloudWatch) to monitor and alert on failures.

## Testing & Debugging

### Local Testing with ngrok

Webhooks need public HTTPS URLs. For local development, use [ngrok](https://ngrok.com/):

```bash
# Run your local server
node server.js

# In another terminal, expose it
ngrok http 3000
```

ngrok gives you a public URL like `https://abc123.ngrok.io`. Use that in NextPhone webhook settings during development.

### Test Webhook Manually

Send test payloads with curl:

```bash
curl -X POST https://yourdomain.com/webhook/nextphone \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "event": "call.ended",
    "data": {
      "call_id": "test_call_123",
      "caller": {
        "phone": "+15551234567",
        "name": "Test User",
        "email": "test@example.com"
      },
      "call_type": "quote_request",
      "duration_seconds": 120
    }
  }'
```

### Debug Common Issues

**Webhook not firing?**
- Check webhook is activated in NextPhone dashboard
- Verify URL is correct and publicly accessible
- Check event type matches what you selected

**Receiving webhooks but processing fails?**
- Add detailed logging
- Verify signature authentication isn't rejecting valid requests
- Check external API credentials are correct

**Timeouts?**
- Respond 200 OK within 5 seconds
- Move slow operations (CRM calls, emails) to async queue

## Best Practices

### Security

- **Never expose API keys** in client-side code or public repos
- **Verify webhook signatures** to prevent fake requests
- **Use HTTPS** for all endpoints
- **Rotate API keys** periodically

### Performance

- **Respond quickly** (<5 seconds) to acknowledge webhook receipt
- **Process async** via queue (Redis, RabbitMQ, AWS SQS)
- **Batch operations** when creating multiple records
- **Cache** frequently accessed data

### Reliability

- **Make endpoints idempotent** (safe to process same webhook twice)
- **Log everything** for debugging and auditing
- **Monitor** webhook success/failure rates
- **Set up alerts** for webhook failures

### Code Organization

```
project/
   handlers/
      call_ended.js
      call_answered.js
      message_collected.js
   integrations/
      crm.js
      email.js
      slack.js
   utils/
      auth.js
      logging.js
   server.js
```

Separate concerns for maintainability.

## NextPhone API Features for Developers

### Webhook Events

- `call.answered` - Call connected
- `call.ended` - Call completed
- `call.transferred` - Call transferred to human
- `message.collected` - Voicemail left
- `data.collected` - Custom field collected during call
- `transcript.ready` - Full transcript available

### Custom Data Collection

Configure AI to collect any data you need:

```json
{
  "data_to_collect": [
    {
      "field": "budget",
      "question": "What's your budget range?",
      "type": "string"
    },
    {
      "field": "timeline",
      "question": "When do you need this done?",
      "type": "string"
    }
  ]
}
```

Data appears in webhook payload's `custom_fields`.

### API Rate Limits

- **Webhooks:** Unlimited (but respect 5-second response timeout)
- **API calls:** 1,000 requests/hour per API key
- **Burst:** Up to 50 requests/second

If you hit limits, implement exponential backoff and retry.

## Frequently Asked Questions

### Can I call NextPhone's API to trigger outbound calls?

Yes. POST to `/v1/calls` with destination phone and script. Useful for appointment reminders, follow-ups, etc.

### How do I handle multiple phone numbers with one webhook?

Include phone number identifier in webhook payload. Route logic based on which number received the call.

### Can I modify the AI's response mid-call based on external data?

Yes, use "data.collected" event to trigger real-time lookups (check inventory, pull CRM data) and dynamically update AI responses.

### What happens if my webhook endpoint is down?

NextPhone retries 3 times (5 min, 15 min, 1 hour intervals). After that, webhook is marked failed. Check dashboard for failed webhooks and manually retry if needed.

## Start Building Custom Integrations

NextPhone's HTTP webhook system gives developers full control over call data. Build exactly the integration your business needsno limitations of pre-built connectors.

Authenticate securely, handle errors properly, and your custom integration will be production-ready.

[Start your free 14-day trial of NextPhone](https://getnextphone.com/trial) and build your first integration today.

---

**URL Slug:** `/blog/ai-receptionist-api-integration-tutorial`
