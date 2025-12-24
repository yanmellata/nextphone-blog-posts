# Extraction Guidelines - Content Filters & Focus Areas

**Purpose:** Simple rules to filter extraction recommendations across all 24 research sources.

---

## ❌ EXCLUDE (Remove These Topics)

### Healthcare/Medical (Complete Exclusion)
- ❌ HIPAA compliance
- ❌ Medical practices
- ❌ Healthcare privacy
- ❌ Dental practices
- ❌ Veterinary clinics
- ❌ Patient intake/scheduling
- ❌ BAA (Business Associate Agreements)

### Enterprise Compliance (Not Our Focus)
- ❌ SOC 2 certification
- ❌ GDPR compliance
- ❌ Enterprise security frameworks

### Specific Platforms to Exclude
- ❌ ServiceTitan (field service software)
- ❌ Medical/healthcare-specific software

### Edge Cases to Avoid
- ❌ "Sync errors" troubleshooting (too technical, weird angle)
- ❌ Medical/healthcare industry workflows

---

## ✅ FOCUS AREAS (Prioritize These)

### Target Industries (Service Businesses)
- ✅ HVAC (heating, cooling, air conditioning)
- ✅ Plumbing
- ✅ Electrical contractors
- ✅ General contractors
- ✅ Roofing
- ✅ Locksmith services
- ✅ Legal practices (law firms)
- ✅ Real estate agencies
- ✅ Accounting firms
- ✅ Property management
- ✅ Auto repair shops
- ✅ Pest control
- ✅ Landscaping
- ✅ Cleaning services

### Integration Categories (HIGH PRIORITY)

**1. Calendar Integrations**
- ✅ Calendly
- ✅ Cal.com
- ✅ Google Calendar
- ✅ Apple Calendar (iCloud Calendar)
- ✅ Outlook Calendar
- ✅ Microsoft 365 Calendar

**2. CRM Integrations**
- ✅ HubSpot
- ✅ Pipedrive (explicitly requested as "sick")
- ✅ Salesforce
- ✅ Zoho CRM
- ✅ Monday.com
- ✅ Airtable (explicitly requested as "sick")
- ✅ Other business CRMs (non-medical)

**3. No-Code/Automation Platforms**
- ✅ Zapier (explicitly requested as "sick")
- ✅ Make.com
- ✅ n8n

**4. Website Platforms**
- ✅ Webflow
- ✅ WordPress
- ✅ Squarespace
- ✅ Wix
- ✅ Shopify (service-based products)

**5. IVR Integrations (NEW - HIGH PRIORITY)**
- ✅ IVR platforms that route to AI receptionist
- ✅ "AI receptionist as IVR branch" angle
- ✅ After-hours IVR → AI receptionist routing
- ✅ Multi-level IVR with AI fallback
- ✅ IVR best practices for call routing
- ✅ Specific IVR platform integrations

**6. Business Phone Systems (NEW - HIGH PRIORITY)**
- ✅ Verizon Business
- ✅ AT&T Business
- ✅ T-Mobile Business
- ✅ Twilio
- ✅ RingCentral
- ✅ Nextiva
- ✅ 8x8
- ✅ Other VoIP/business phone providers

**7. Field Service Software (Non-Medical)**
- ✅ Housecall Pro
- ✅ Jobber
- ✅ ServiceM8
- ✅ FieldEdge

### Content Angles (HIGH PRIORITY)

**Call Routing & Best Practices**
- ✅ Call routing best practices
- ✅ IVR configuration for after-hours
- ✅ Multi-location call routing
- ✅ Emergency vs. non-emergency routing
- ✅ Escalation workflows

**Setup & Migration**
- ✅ Phone number porting (explicitly requested as "great")
- ✅ Setup checklists
- ✅ Configuration guides
- ✅ Testing protocols

**Competitor Switching**
- ✅ Switching from Ruby Receptionists (explicitly requested as "makes sense")
- ✅ Switching from Smith.ai
- ✅ Switching from other competitors

---

## 🎯 NEW OPPORTUNITIES (Based on User Feedback)

### 1. IVR + AI Receptionist Angle
**Key Insight:** "One of the branches of an IVR should be an AI receptionist especially after hours"

**Blog Post Ideas:**
- "How to Route IVR to AI Receptionist After Hours"
- "IVR Best Practices: When to Use AI vs Human Routing"
- "Multi-Level IVR with AI Receptionist Fallback"
- "After-Hours Call Routing: IVR to AI Receptionist Setup"
- Platform-specific: "[IVR Platform] + NextPhone Integration Guide"

### 2. Calendar Integration Expansion
**Blog Post Ideas:**
- "Calendly AI Phone Booking Integration"
- "Google Calendar Sync for AI Receptionist"
- "Apple Calendar Integration for Service Businesses"
- "Outlook Calendar AI Appointment Scheduling"
- "Cal.com + AI Receptionist: Open-Source Scheduling"

### 3. Website Platform Integrations
**Blog Post Ideas:**
- "Webflow Click-to-Call AI Receptionist Integration"
- "WordPress Phone Answering Plugin Setup"
- "Squarespace AI Receptionist Widget Integration"
- "Add AI Receptionist to Your Website: Platform Guide"

### 4. Business Phone System Integrations
**Blog Post Ideas:**
- "Verizon Business + AI Receptionist Integration"
- "Twilio AI Receptionist API Setup Guide"
- "RingCentral to NextPhone Migration Guide"
- "Business Phone System Comparison: Which Works with AI?"

---

## 🚫 REMOVED FROM SAMPLE EXTRACTIONS (User Feedback)

### GAP_ANALYSIS_extraction.md - Removed Posts:
- #15: HIPAA Compliant AI Receptionist ❌
- #16: HIPAA Answering Service ❌
- #17: Healthcare Privacy ❌
- #18: Medical Practice Security ❌
- #21: Data Security (too enterprise/compliance-heavy) ❌
- #23: SOC 2 Compliance ❌
- #32: Medical Office Patient Intake ❌
- ServiceTitan integration ❌

### ruby_competitor_extraction.md - Removed Posts:
- All HIPAA-related posts ❌
- #9: SOC 2 Certification ❌
- #10: GDPR Compliance ❌
- #18: Dental Practice (healthcare) ❌

### integration_keywords_extraction.md - Removed Posts:
- #17-18: Sync errors troubleshooting (weird angle) ❌
- Any medical/healthcare-related integration keywords ❌

---

## ✅ EXPLICITLY APPROVED (User Feedback)

These are confirmed "sick" or "great":
- Pipedrive integration ✅
- Zapier integration ✅
- Airtable integration ✅
- Phone number porting ✅
- Setup checklist ✅
- Switching from Ruby Receptionists ✅

---

## 📋 Extraction Checklist (Use for Each File)

Before recommending a blog post, check:
1. ❌ Is it HIPAA/medical/healthcare-related? → REMOVE
2. ❌ Is it SOC 2/GDPR/enterprise compliance? → REMOVE
3. ❌ Is it ServiceTitan or excluded platform? → REMOVE
4. ✅ Does it target service businesses (HVAC, plumbing, legal, etc.)? → KEEP
5. ✅ Is it calendar/CRM/IVR/phone system integration? → HIGH PRIORITY
6. ✅ Does it focus on call routing best practices? → HIGH PRIORITY
7. ✅ Is it setup/migration/competitor switching? → KEEP

---

## 🎯 Priority Ranking (Updated Based on Feedback)

**Tier 1 (Highest Priority):**
1. Calendar integrations (Calendly, Google, Outlook, Apple, Cal.com)
2. IVR + AI receptionist routing (NEW - user emphasized)
3. Business phone system integrations (Verizon, Twilio, RingCentral)
4. CRM integrations (Pipedrive, HubSpot, Salesforce, Zoho, Airtable)
5. Call routing best practices

**Tier 2 (High Priority):**
1. Website platform integrations (Webflow, WordPress, Squarespace)
2. No-code automation (Zapier, Make)
3. Field service software (Housecall Pro, Jobber - non-medical)
4. Setup & onboarding guides
5. Phone number porting

**Tier 3 (Medium Priority):**
1. Competitor switching (Ruby, Smith.ai)
2. Industry-specific workflows (HVAC, plumbing, legal, real estate)
3. Seasonal content (HVAC summer surge, tax season, holidays)

---

## Notes

- **User Feedback Date:** 2025-12-21
- **Key Shift:** From healthcare/compliance focus → service business integrations + IVR/call routing
- **New High-Priority Angle:** IVR as gateway to AI receptionist (especially after-hours)
- **Approved Platforms:** Pipedrive, Zapier, Airtable (explicitly mentioned as "sick")
- **Keep It Simple:** Use this as a quick filter when extracting from remaining 21 files
