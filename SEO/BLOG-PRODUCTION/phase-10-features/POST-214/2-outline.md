# OUTLINE: "SMS Follow-Up After Calls: Timing, Sequences & Message Templates"

**Target:** 1,700-1,900 words

## Complete Structure:

### Key Takeaways (100 words)
- 6-7 bullets covering SMS benefits, timing strategies, automation capabilities
- Include 98% SMS open rate stat
- Reference 25.4% callback request capture opportunity
- Highlight template variables and automation

### Introduction (200 words)
- Hook: Customer calls, AI answers, appointment bookedwhat happens next determines if they show up
- Problem: Calls without SMS follow-up = higher no-show rates, missed revenue
- Solution: Automated post-call SMS with proper timing and templates
- Preview: Timing strategies, message templates, NextPhone automation
- Natural CTA: See SMS automation in action

### SECTION 1: Why SMS Follow-Up Matters (250 words)
- 98% open rate vs 20% email, read within 3 minutes average
- Customer expectations have changed (expect text confirmations)
- Reduces no-shows by 30-40% with reminder sequences
- Captures the 25.4% who request callbacks but might forget
- Multi-channel reinforcement (call + SMS + email) improves conversion
- Modern business communication standard

### SECTION 2: Optimal Timing for Post-Call SMS (350 words)

**Immediate (0-60 seconds):**
- Appointment confirmations
- Emergency acknowledgments
- Booking URLs and next steps
- Why it works: Strike while iron is hot, customer still focused

**Short Delay (5-30 minutes):**
- Callback commitment reminders
- Estimate follow-ups with links
- Resource sharing (how-to guides, FAQs)
- Why it works: Gives customer time to finish call-related tasks

**Scheduled Follow-Up (Hours to Days Later):**
- Day-before appointment reminders (24 hours prior)
- Day-of reminders (2-4 hours before)
- Post-service satisfaction surveys (24 hours after)
- Payment reminders (if applicable)
- Why it works: Catches customers before they forget or double-book

**Timing Best Practices:**
- Business hours vs after-hours considerations
- Time zone awareness for multi-location businesses
- Frequency limits (don't spam)

### SECTION 3: SMS Sequence Strategies (400 words)

**Single Touch Approach:**
- One confirmation immediately after call
- Best for: Simple scenarios, emergency acknowledgments
- Example flow for emergency call

**Multi-Touch Sequences:**
- Booking confirmation (immediate)
- Reminder (24 hours before)
- Day-of reminder (2-4 hours before)
- Best for: Appointments, scheduled services
- Example 4-touch sequence for routine appointment

**Abandoned/Missed Call Follow-Up:**
- Auto-SMS when caller hangs up before AI answers
- "Sorry we missed you" message with callback options
- Captures 25.4% who would request callbacks
- Example template and expected response rate

**Context-Based Sequences:**
- Emergency vs routine cadences (emergencies = fewer messages, routine = full sequence)
- New customer vs returning customer (returning = shorter messages)
- High-value vs standard appointments (VIP treatment)

**Personalization Strategies:**
- Use call transcription data to customize messages
- Reference specific service requested
- Include technician name for day-of reminder
- Dynamic urgency level based on customer need

### SECTION 4: Message Templates by Scenario (500 words)

**Template Structure Breakdown:**
- Keep under 160 characters when possible (single SMS)
- Clear action items
- Include business name for context
- Provide opt-out option
- Use template variables for personalization

**Appointment Confirmation Template:**
```
Hi {{customer_name}}! Your {{service_type}} appointment with {{business_name}} is confirmed for {{date}} at {{time}}. We'll see you at {{address}}. Questions? Call us at {{phone}}. Reply STOP to opt out.
```

**Callback Commitment Template:**
```
Thanks for contacting {{business_name}}! We'll call you back {{callback_time}} regarding your {{service_request}}. - {{owner_name}}
```

**Emergency Acknowledgment Template:**
```
EMERGENCY CONFIRMED: {{business_name}} received your {{emergency_type}} call. Our tech {{tech_name}} will arrive within {{eta}} minutes at {{address}}.
```

**Appointment Reminder (24 hours before):**
```
Reminder: Your {{service_type}} appointment with {{business_name}} is tomorrow at {{time}}. Reply CONFIRM or call {{phone}} to reschedule.
```

**Day-Of Reminder:**
```
{{customer_name}}, {{tech_name}} is heading to your appointment today at {{time}}. Running on schedule. See you soon!
```

**Resource/Link Sharing:**
```
Hi {{customer_name}}! Here's the {{resource_type}} we discussed: {{booking_url}}. Questions? Text back or call {{phone}}.
```

**Post-Service Follow-Up:**
```
Thanks for choosing {{business_name}}! How was your experience with {{tech_name}}? Reply with feedback or review us here: {{review_url}}
```

**Payment Reminder:**
```
{{customer_name}}, your {{service_type}} invoice of ${{amount}} is ready. Pay online: {{payment_url}} or call {{phone}}. Thanks!
```

### SECTION 5: NextPhone SMS Automation (350 words)

**How It Works:**
- AI analyzes call context and outcome
- Automatically triggers appropriate SMS template
- Twilio API integration for reliable delivery
- No manual intervention required

**Template Variables Available:**
- {{caller_number}} - Customer phone number
- {{receiving_number}} - Your business number
- {{message}} - Call summary/transcription excerpt
- {{owner_name}} - Business owner/rep name
- {{booking_url}} - Link to scheduling page
- Custom variables based on your setup

**Automation Triggers:**
- Appointment scheduled ’ Send confirmation immediately
- Callback requested ’ Send commitment within 5 minutes
- Emergency handled ’ Send acknowledgment with ETA
- Estimate requested ’ Send follow-up with quote link
- Call unanswered ’ Send "sorry we missed you" message

**Setup Process:**
- Configure templates in dashboard (15 minutes)
- Map triggers to templates (10 minutes)
- Test with sample calls (5 minutes)
- Go live with automation

**Use Case Examples:**
- HVAC: Emergency call at 2 AM ’ Auto-SMS confirms tech dispatch
- Dental: Appointment booked ’ Immediate confirmation + day-before reminder
- Plumbing: Estimate requested ’ SMS with booking link in 10 minutes
- Legal: Consultation scheduled ’ Multi-touch reminder sequence

**Benefits Over Manual SMS:**
- Instant delivery (no delay waiting for staff)
- 100% consistency (never forget to send)
- Personalization at scale (variables auto-populate)
- Works 24/7 (after-hours calls get SMS too)

### SECTION 6: TCPA Compliance & Best Practices (250 words)

**Consent Requirements:**
- Express written consent for marketing messages
- Transactional messages (confirmations) less restrictive
- Consent can be obtained during call or via website
- NextPhone: AI can request SMS opt-in during conversation

**Required Elements:**
- Opt-out mechanism in every message ("Reply STOP to opt out")
- Respect opt-outs immediately
- Business identification in message
- Clear purpose of message

**Do-Not-Disturb Hours:**
- Federal: No calls/texts before 8 AM or after 9 PM (recipient's local time)
- State variations (some stricter)
- Emergency exceptions may apply
- NextPhone: Auto-scheduling respects time zones

**Record Keeping:**
- Log consent date/time/method
- Track opt-outs
- Maintain for 4+ years
- NextPhone: Automatic compliance logging

**Safe Automation Practices:**
- Use transactional templates for confirmations/reminders
- Limit marketing messages without explicit opt-in
- Frequency caps (max 1-2 per day unless critical)
- Monitor complaint rates

### SECTION 7: Multi-Channel Strategy (200 words)

**When to Use Each Channel:**
- **Phone Call:** Complex questions, emergencies, sales conversations
- **SMS:** Confirmations, reminders, quick updates, time-sensitive info
- **Email:** Detailed information, invoices, long-form content, documentation

**Multi-Channel Sequences:**
- Appointment booking: Call (initial) ’ SMS (immediate confirmation) ’ Email (detailed info) ’ SMS (reminder)
- Emergency: Call (routing) ’ SMS (acknowledgment) ’ Email (invoice after service)
- Estimate request: Call (qualify) ’ Email (detailed quote) ’ SMS (follow-up 24 hours later)

**Why Multi-Channel Works:**
- Reinforcement through repetition (people see message 3x vs 1x)
- Reach customers on preferred channel
- Different channels serve different purposes
- Data: 3X higher conversion with multi-channel vs single channel

**NextPhone Integration:**
- Call transcription feeds email summaries
- SMS confirmations auto-trigger from call outcome
- Email and SMS work together seamlessly
- All tracked in unified dashboard

### SECTION 8: Measuring SMS Performance (150 words)

**Key Metrics:**
- **Delivery rate:** % of SMS successfully delivered (should be 95%+)
- **Response rate:** % who reply to messages (varies by type)
- **Appointment show-up rate:** Compare with/without SMS reminders (expect 30-40% improvement)
- **Click-through rate:** For messages with links (booking URLs, payment links)
- **Opt-out rate:** Should be under 1% (higher indicates bad content/frequency)

**Tracking in NextPhone:**
- SMS sent/delivered dashboard
- Response tracking per template
- A/B testing different message variations
- ROI calculation: (Revenue from SMS-confirmed appointments - SMS cost) / SMS cost

**Optimization:**
- Test different send times
- Refine template wording
- Adjust sequence frequency
- Personalization impact analysis

### Conclusion (150 words)
- Recap: SMS follow-up transforms post-call experience
- Key takeaways: Timing matters, automation scales, templates personalize, compliance protects
- Data: 25.4% callback requests + 74.1% unanswered calls = massive opportunity
- NextPhone automation: Set up once, runs 24/7, captures every opportunity
- Next step: Configure SMS templates and let AI handle the rest
- Final CTA: Start capturing more customers with automated SMS

**Total: ~1,850 words**

## Visuals to Include:
- Timeline graphic: Immediate vs delayed vs scheduled SMS timing
- SMS sequence flowchart: Multi-touch appointment reminder sequence
- Template anatomy: Annotated SMS showing variable placement
- Multi-channel diagram: Call + SMS + Email workflow

## CTAs:
- Soft: After intro (See SMS automation in action)
- Mid: After Section 5 (Try NextPhone's SMS automation free for 14 days)
- Hard: Conclusion (Configure your SMS follow-up system today)

## Internal Links (if available):
- AI receptionist features
- Call handling automation
- Appointment scheduling
- Customer communication best practices

## Ready for Draft
