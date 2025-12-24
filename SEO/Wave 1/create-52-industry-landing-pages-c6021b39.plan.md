<!-- c6021b39-ae5e-44f9-badc-59f229d2ea06 1db033df-7365-4c1c-81b6-4240c7865f64 -->
# Fix Current 52 + Add 50+ New Landing Pages

## PART 1: Fix Current 52 Pages

### 1.1 Remove Compliance Claims (5 industries)

**Medical Offices, Therapists, Clinics, Telemedicine, Schools**

- Remove "HIPAA-compliant" and "FERPA-compliant" claims
- Change badges, headlines, meta tags
- Update stats: "HIPAA Compliant" → "Secure & Private"
- Update FAQs: "How do you handle patient/student privacy?" with focus on security

### 1.2 Remove Fake Social Proof Numbers (all 52 pages)

Change: "Trusted by 500+ law firms" → "Trusted by businesses nationwide"

### 1.3 Increase Dollar Values by 10x (all 52 pages)

- $2,400 → $24,000
- $300 → $3,000
- $450 → $4,500
- Update ALL stats and pricingContext calculations

### 1.4 Rename Industries (4 industries)

1. Home Remodeling → Home Remodelers (slug: remodeling → remodelers)
2. Handyman Services → Handymen
3. Towing Services → Towing Companies
4. Cleaning Services → Cleaning Companies

Update: `src/data/landing-pages.ts`, `src/data/industries-categories.ts`, rename folder `ai-receptionist-for-remodeling` → `ai-receptionist-for-remodelers`

---

## PART 2: Add 50+ New Industries (Volume-Based)

### 2.1 Mega Volume Industries (>100K searches) - 8 industries

1. Urgent Care - 2.24M/mo
2. Daycare/Childcare - 823K/mo
3. Pet Grooming - 673K/mo
4. Junk Removal - 550K/mo
5. Movers - 246K/mo
6. Wedding Planners - 246K/mo
7. Car Wash - 100K+/mo
8. Cafes/Coffee Shops - 100K+/mo

### 2.2 Very High Volume (50K-100K) - 10 industries

9. Yoga Studios - 90K/mo
10. Travel Agencies - 74K/mo
11. Dermatology - 60K/mo
12. Chimney Sweeps - 60K/mo
13. Oil Change - 50K/mo
14. Bakeries - 50K+/mo
15. Florists - 50K+/mo
16. Nail Salons - 50K+/mo
17. Home Inspectors - 50K/mo
18. Tattoo Shops - 40K+/mo

### 2.3 High Volume (20K-50K) - 9 industries

19. Spas - 40K/mo
20. Architects - 40K/mo
21. Lawn Care - 40K/mo
22. Massage Therapy - 20K/mo
23. Catering - 20K/mo
24. Bookstores - 20K/mo
25. Dry Cleaning - 20K/mo
26. Optometry - 20K/mo
27. Meal Prep Services - 8K/mo

### 2.4 Solid Volume (10K-20K) - 13 industries

28. Photographers - 15K/mo
29. Computer Repair - 15K/mo (high CPC)
30. Physical Therapy - 12K/mo
31. Auto Detailing - 12K/mo
32. Smartphone Repair - 10K/mo (high CPC)
33. Tree Services - 10-15K/mo
34. Tutoring - 10K/mo
35. Pet Boarding - 10K/mo
36. Bowling Alleys - 10K+/mo
37. Marketing Agencies - 10K+/mo
38. Orthodontics - 10K/mo
39. Breweries - 10K/mo
40. Print Shops - 10K/mo

### 2.5 Good Volume (5K-10K) - 12 industries

41. Interior Designers - 8K/mo
42. Storage Facilities - 8K/mo
43. Notary Services - 6K/mo (HIGH CPC $116)
44. Carpet Cleaning - 6K/mo
45. Driving Schools - 6K/mo
46. Mini Golf - 6K/mo
47. Event Planners - 5K/mo
48. Acupuncture - 5K/mo
49. Dog Walking - 5K/mo
50. Escape Rooms - 5K/mo
51. Dance Studios - 5K/mo
52. Butcher Shops - 6K/mo

**Total New: 52 industries**
**Combined Volume: 7+ million searches/month**

---

## Implementation Steps

### Step 1: Fix Current 52 Pages

- Update `src/data/landing-pages.ts` with fixes
- Rename remodeling folder
- Update industries-categories.ts

### Step 2: Add 52 New Industries

- Add to `src/data/landing-pages.ts` (following same pattern)
- Create 52 new page folders
- Update `src/data/industries-categories.ts` with new categories

### Step 3: Verify & Test

- Check for linting errors
- Verify all pages compile
- Test sample pages

---

## Result

**104 total landing pages** covering 7+ million monthly searches across all major service industries.

## Files to Update

- `src/data/landing-pages.ts`
- `src/data/industries-categories.ts`  
- Create 52 new page directories
- Rename 1 directory (remodeling → remodelers)