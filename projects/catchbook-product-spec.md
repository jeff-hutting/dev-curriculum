# Catchbook — Product Specification Document

**Version:** 1.0  
**Created:** 2025-12-01  
**Owner:** Jeff Hutting  
**Project Type:** Portfolio + Market Product  
**Development Timeline:** 9-12 months (spans Phases P1-P28 of dev-curriculum)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Product Vision](#product-vision)
3. [User Personas](#user-personas)
4. [Market Analysis](#market-analysis)
5. [Core Features](#core-features)
6. [User Stories & Acceptance Criteria](#user-stories--acceptance-criteria)
7. [Technical Architecture](#technical-architecture)
8. [Data Models](#data-models)
9. [API Design](#api-design)
10. [AI/ML Integration Points](#aiml-integration-points)
11. [External API Dependencies](#external-api-dependencies)
12. [Mobile-First Design](#mobile-first-design)
13. [Monetization Strategy](#monetization-strategy)
14. [Success Metrics](#success-metrics)
15. [Go-to-Market Strategy](#go-to-market-strategy)
16. [Development Roadmap](#development-roadmap)
17. [Risk Assessment](#risk-assessment)
18. [Appendices](#appendices)

---

## Executive Summary

**Problem:** Existing fishing apps require excessive manual data entry, making it tedious to log catches consistently. Anglers want rich data (species, location, weather, tides, solunar periods) but don't want to type it all in after a long day on the water.

**Solution:** Catchbook is an AI-powered fishing journal that uses photo capture + EXIF data + computer vision to auto-populate 90% of catch data. The app acts as an intelligent fishing caddy, learning from your patterns to predict optimal conditions and suggest gear/locations.

**Target User:** Kayak anglers (primary), with expansion to all recreational anglers.

**Unique Value Proposition:**
- Snap a photo → AI handles the rest (species, size, location, conditions)
- Predictive intelligence: "Based on your history, tomorrow morning at Delta Coves has 85% success probability"
- Equipment integration: Track which lures work when/where
- Zero friction logging: 10 seconds per catch vs. 3-5 minutes in competing apps

**Business Model:** Freemium with Pro tier for predictions, advanced analytics, and unlimited catch history.

---

## Product Vision

### Mission Statement
Make fishing data collection effortless so anglers can focus on fishing, not forms—while building the most intelligent fishing assistant on the market.

### Long-term Vision (3-5 years)
1. **The Personal Fishing AI:** Every angler has a pocket caddy that knows their patterns better than they do
2. **Community Intelligence:** Aggregate anonymized data to provide real-time local conditions ("5 largemouth bass caught at this lake in the last 2 hours")
3. **Ecosystem Integration:** Partner with tackle manufacturers, marine electronics brands, and conservation organizations
4. **Predictive Leadership:** Best-in-class machine learning models that actually improve catch rates

### Core Principles
- **Friction elimination:** Every feature must reduce cognitive load
- **Accuracy over aesthetics:** Data quality is paramount
- **Privacy first:** User data is never sold, anonymization is opt-in
- **Respect the sport:** No gamification that encourages unethical fishing
- **Real utility:** Every feature must pass the "would I use this on the water?" test

---

## User Personas

### Primary Persona: Jeff (The Kayak Tournament Angler)

**Demographics:**
- Age: 35-55
- Location: California (Delta, SF Bay, coastal estuaries)
- Experience: Intermediate to advanced kayak fisherman
- Tech comfort: High (uses GPS, fish finders, action cameras)
- Annual fishing trips: 40-60

**Goals:**
- Identify patterns in successful catches (tide, moon phase, lure color)
- Remember exact locations of productive spots
- Track equipment effectiveness over time
- Prepare for tournaments with historical data

**Pain Points:**
- Can't remember which lure worked 3 months ago at this spot
- Too tired/wet to type detailed notes after a long paddle
- Existing apps are clunky and require too much input
- No way to correlate weather/tides with success
- Fishing journals are analog and get lost/damaged

**Technology:**
- iPhone 14+ (primary device on water)
- Uses Navionics for navigation
- GoPro for action footage
- Apple Watch for fitness tracking

**Behavior:**
- Launches at sunrise, fishes 4-6 hours
- Takes photos of notable catches only
- Checks weather/tide apps before every trip
- Active in local kayak fishing Facebook groups
- Competitive but conservation-minded (catch and release)

---

### Secondary Persona: Maria (The Weekend Warrior)

**Demographics:**
- Age: 28-45
- Location: Suburban/urban proximity to water
- Experience: Beginner to intermediate
- Tech comfort: Moderate
- Annual fishing trips: 12-20

**Goals:**
- Build fishing confidence through documented success
- Share catches with friends/family on social media
- Learn what works in local waters
- Track personal bests

**Pain Points:**
- Doesn't know species identification
- Forgets where the good spots are between trips
- Overwhelmed by too much technical data
- Wants simple "when should I go?" recommendations

**Technology:**
- iPhone or Android
- Uses social media actively (Instagram, Facebook)
- Casual app user (not power user)

**Behavior:**
- Fishes 2-3 times per month
- Photos almost every catch for memories
- Relies on YouTube for learning
- Values ease of use over feature depth

---

### Tertiary Persona: Dave (The Data-Driven Guide)

**Demographics:**
- Age: 45-65
- Location: Operates near popular fishing destinations
- Experience: Expert (professional guide)
- Tech comfort: Moderate to high
- Annual guided trips: 100-200

**Goals:**
- Track client success rates by season/condition
- Demonstrate value to potential clients with data
- Optimize trip timing and technique recommendations
- Build a professional reputation with verifiable results

**Pain Points:**
- Manual logbooks are time-consuming
- Can't easily share patterns with clients
- No way to prove expertise with data
- Competitor guides use "secret" techniques he wants to reverse-engineer

**Technology:**
- iPad or smartphone (weather-protected case)
- Professional marine electronics
- Action cameras for client memories

**Behavior:**
- Logs every trip, often with multiple anglers
- Needs quick input during active guiding
- Values historical trend analysis
- Willing to pay for professional-grade tools

---

## Market Analysis

### Competitive Landscape

#### Direct Competitors

| App | Strengths | Weaknesses | Differentiation Opportunity |
|-----|-----------|------------|----------------------------|
| **Fishbrain** | Large user base (10M+), social features, species ID | Manual entry required, cluttered UI, ads-heavy freemium | Better AI auto-population, cleaner UX |
| **Anglr** | Hardware integration (tracker device), automatic logging | Requires $100+ device, limited species recognition | Pure software approach, better AI |
| **FishAngler** | Comprehensive features, weather integration | Complex interface, steep learning curve | Simpler onboarding, smarter defaults |
| **MyFishingAdvisor** | Strong solunar data, location-based tips | No photo logging, outdated UI | Modern design, photo-first workflow |
| **FishDonkey** | Good for tournament anglers, team features | Weak species ID, minimal automation | Superior AI, better predictive models |

#### Indirect Competitors
- **Analog logbooks:** Moleskine-style fishing journals (still popular with traditionalists)
- **Spreadsheets:** DIY Google Sheets/Excel trackers (power users)
- **General notes apps:** Evernote, Notion (low friction but no structure)

### Market Size

**Total Addressable Market (TAM):**
- 50 million recreational anglers in US (US Fish & Wildlife Service, 2023)
- ~15 million use smartphones while fishing
- **TAM:** $450M annually (assuming $30 average annual revenue per digital angler)

**Serviceable Addressable Market (SAM):**
- Tech-comfortable anglers willing to pay for apps: ~5 million
- **SAM:** $150M annually

**Serviceable Obtainable Market (SOM):**
- Target 1% of SAM in Year 1: 50,000 users
- Conversion to paid (20%): 10,000 paying users
- **Year 1 Revenue Target:** $300K (at $30/year avg)

### Market Trends
1. **Mobile-first fishing:** 78% of anglers use smartphones on the water (2023 survey)
2. **AI adoption:** Consumers expect smart features (Google Lens, ChatGPT)
3. **Subscription fatigue:** Users consolidating to fewer, higher-value subscriptions
4. **Privacy concerns:** Growing awareness of data usage, want control
5. **Conservation focus:** Younger anglers prioritize sustainability

---

## Core Features

### MVP (Phase 1: Months 1-4)

#### 1. Photo Capture & Auto-Population
**Description:** Snap a photo of the catch → AI extracts and pre-fills all data fields.

**Functionality:**
- Camera integration with EXIF data capture
- GPS coordinates from EXIF → map location
- Timestamp → date/time, moon phase, solunar period
- Photo analysis → species identification (ML model)
- Weather API → conditions at time/location
- Tide API → tide state (if applicable)

**User Flow:**
1. User opens app → taps "New Catch"
2. Camera opens → snap photo
3. Processing screen (2-3 seconds)
4. Review screen shows pre-filled form:
   - Species: "Largemouth Bass" (editable dropdown)
   - Location: "Sherman Island, CA" (map pin, editable)
   - Date/Time: "Nov 29, 2025, 7:15 AM"
   - Weather: "Partly cloudy, 58°F, Wind 5mph NE"
   - Tide: "Incoming, 2.1ft"
   - Moon Phase: "Waning Gibbous (68%)"
5. User confirms or edits → saves catch

**Acceptance Criteria:**
- Species ID accuracy >80% for top 50 species
- Location accuracy within 50 meters
- Weather data matches NOAA at timestamp
- Processing completes in <5 seconds on 4G
- User can override any auto-populated field

---

#### 2. Catch Log & Timeline
**Description:** View all catches in chronological feed with key details.

**Functionality:**
- Reverse-chronological list of catches
- Thumbnail image + species + date + location
- Filter by date range, species, location
- Search by keyword (location name, notes)
- Tap to expand full catch details

**User Flow:**
1. User opens app → lands on Catch Log tab
2. Scrollable list of recent catches
3. Pull-to-refresh updates
4. Tap any catch → detail view
5. Swipe to delete (with confirmation)

**Acceptance Criteria:**
- Loads 50 catches in <2 seconds
- Images load lazily (scroll performance)
- Filters apply without full reload
- Detail view shows all logged data + weather/tide/moon
- Edit button on detail view

---

#### 3. Species Library
**Description:** Reference guide with photos and info for AI training and manual lookup.

**Functionality:**
- Searchable list of 100+ common freshwater/saltwater species
- Each entry: photo, scientific name, identifying features, range map
- Linked to NOAA FishWatch for conservation status
- User can submit new species requests

**User Flow:**
1. User taps "Species" tab
2. Scrollable grid of species thumbnails + names
3. Search bar filters results
4. Tap species → detail page with ID tips
5. "Report a Catch" button from species page

**Acceptance Criteria:**
- Initial library: 100 species (50 freshwater, 50 saltwater)
- Search by common or scientific name
- Detail page loads images from Wikimedia Commons (licensed)
- Links to conservation resources (NOAA, state agencies)

---

#### 4. Basic Analytics
**Description:** Simple stats on catch patterns (frequency, species breakdown).

**Functionality:**
- Total catches logged
- Species distribution (pie chart)
- Monthly activity (bar chart)
- Most successful location (map)

**User Flow:**
1. User taps "Stats" tab
2. Dashboard with 4 tiles:
   - Total Catches: 47
   - Top Species: Largemouth Bass (18)
   - Best Month: June (12 catches)
   - Favorite Spot: Delta Coves
3. Tap any tile → drill-down view

**Acceptance Criteria:**
- Charts render in <1 second
- Data updates in real-time after new catch
- Export data as CSV (Pro feature)

---

### Phase 2: Expansion (Months 5-8)

#### 5. Equipment Catalog
**Description:** Track rods, reels, lures, baits, and correlate with catch success.

**Functionality:**
- Equipment library (user-created entries)
- Categories: Rods, Reels, Lures, Lines, Baits, Vessels
- Link equipment to catches ("Caught on...")
- Analytics: "Which lure has highest success rate?"

**User Flow:**
1. User taps "Gear" tab
2. Lists all equipment by category
3. Tap "Add New" → form:
   - Name: "Senko Worm - Watermelon"
   - Category: Lure
   - Photo (optional)
   - Brand: "Gary Yamamoto"
   - Color: "Watermelon"
   - Notes: "5-inch, rigged Texas-style"
4. Save → equipment appears in catalog
5. When logging catch, select from equipment list

**Acceptance Criteria:**
- CRUD operations for all equipment
- Photo upload (optional)
- Success rate calculation: (catches with gear) / (trips gear was used)
- Analytics view: "Top 10 Most Effective Lures"

---

#### 6. Trip Planning & Predictions
**Description:** AI recommends best times/locations based on historical success and current conditions.

**Functionality:**
- "When should I fish?" feature
- Inputs: target species, preferred location(s), date range
- Outputs: ranked recommendations with probability scores
- Factors: historical catch data, weather forecast, tides, moon phase, seasonal patterns

**User Flow:**
1. User taps "Plan" tab
2. Form:
   - Target Species: "Largemouth Bass" (dropdown)
   - Location: "Sherman Island" (from saved spots)
   - Date Range: "This weekend" (picker)
3. Tap "Get Recommendations"
4. Results screen:
   - Saturday 6:00-9:00 AM: **85% success probability**
     - Incoming tide, overcast, waning gibbous
   - Sunday 5:30-8:30 AM: **72% success probability**
     - High tide, light wind, cooler temps
5. Save trip plan → adds to calendar

**Acceptance Criteria:**
- Predictions improve over time (minimum 10 catches for meaningful patterns)
- Success probability based on: user's historical catch rate + current conditions similarity score
- Transparency: show "Why this recommendation?" explanation
- Integration with Apple Calendar / Google Calendar

---

#### 7. Social Sharing
**Description:** Share catches to social media or with other Catchbook users.

**Functionality:**
- One-tap share to Instagram, Facebook, Twitter
- Optional: share to Catchbook community feed
- Privacy controls: public / friends-only / private
- Formatted share card with photo + stats overlay

**User Flow:**
1. User in catch detail view → taps "Share"
2. Preview screen shows formatted image:
   - Photo with overlay:
     - Species name
     - Location (optional, user toggle)
     - Date
     - "Logged with Catchbook"
3. Select platforms (Instagram, Facebook, etc.)
4. Post button → opens platform share sheet

**Acceptance Criteria:**
- Share card renders in 1920x1080 (suitable for IG/FB)
- User can toggle which data appears on card
- Watermark is subtle (not obtrusive)
- Privacy: location can be hidden or generalized ("Northern California")

---

### Phase 3: Advanced Features (Months 9-12)

#### 8. Weather & Tide Overlays
**Description:** In-app weather/tide viewer for trip planning without leaving app.

**Functionality:**
- 7-day weather forecast for saved locations
- Hourly tides (if coastal/tidal water)
- Solunar calendar overlay
- Historical weather conditions for past catches

**User Flow:**
1. User taps "Conditions" tab
2. Select location from saved spots
3. View tabs:
   - Weather: 7-day forecast
   - Tides: Tide chart with major/minor periods
   - Solunar: Best feeding times (major/minor periods)
4. Scroll timeline → see predicted fishing quality

**Acceptance Criteria:**
- Weather data from OpenWeatherMap or NOAA API
- Tide data from NOAA Tides & Currents API
- Solunar calculations accurate (based on moon position)
- Data updates every 6 hours

---

#### 9. Offline Mode
**Description:** Log catches without internet, sync when back online.

**Functionality:**
- Core features work offline (camera, manual entry)
- Queue catches for upload when connectivity returns
- Downloaded map tiles for saved locations
- Species library cached locally

**User Flow:**
1. User loses connectivity on the water
2. App shows "Offline Mode" indicator
3. User logs catches as normal
4. Catches saved locally with "pending sync" badge
5. When back online → auto-sync to cloud
6. Notification: "3 catches synced"

**Acceptance Criteria:**
- All core CRUD operations work offline
- No data loss if app crashes during offline session
- Sync queue prioritizes most recent catches
- Conflict resolution: always prefer local version

---

#### 10. Pro Analytics Dashboard
**Description:** Advanced visualizations and export for power users.

**Functionality:**
- Heatmaps: catch density by location
- Time-series charts: catch rates over time
- Conditions correlation: "You catch 40% more bass when wind is <10mph"
- CSV/JSON export for external analysis
- Compare seasons year-over-year

**User Flow:**
1. User (Pro subscriber) taps "Analytics" tab
2. Dashboard with interactive charts:
   - Heatmap: pins on map sized by catch frequency
   - Line chart: catches per month (multi-year)
   - Scatter plot: catch size vs. water temp
   - Insights panel: "Your best days are overcast with incoming tide"
3. Export button → select format (CSV / JSON)
4. Share or download file

**Acceptance Criteria:**
- Charts interactive (zoom, filter, hover tooltips)
- Export includes all catch data + conditions
- Insights use statistical significance (p < 0.05 for claims)
- Pro-only (paywall for free users with teaser)

---

## User Stories & Acceptance Criteria

### Epic 1: Photo Capture & Auto-Population

**US-001: As an angler, I want to snap a photo and have my catch details auto-filled so I can log catches quickly without typing.**

**Acceptance Criteria:**
- Photo taken via in-app camera includes EXIF GPS + timestamp
- Species identified with >80% accuracy for top 50 species
- Location reverse-geocoded to human-readable name
- Weather fetched from API (temp, conditions, wind)
- Tide state calculated from NOAA API (if location is tidal)
- Moon phase calculated from date
- All fields editable before saving
- Processing completes in <5 seconds on 4G

**Priority:** P0 (MVP Critical)

---

**US-002: As an angler, I want the app to suggest the correct species when the AI is uncertain so I can quickly confirm without typing.**

**Acceptance Criteria:**
- If AI confidence <70%, show top 3 species suggestions
- Tapping suggestion auto-fills species field
- "Not Listed" option opens species search
- User selection trains model (feedback loop)

**Priority:** P1 (MVP Enhancement)

---

**US-003: As an angler, I want to manually log a catch when I don't have a photo so I can maintain complete records.**

**Acceptance Criteria:**
- "Log Without Photo" button on new catch screen
- Form shows same fields as auto-populated version
- GPS location captured even without photo
- Species dropdown searchable
- Save button validates required fields

**Priority:** P1 (MVP Enhancement)

---

### Epic 2: Catch Log & History

**US-004: As an angler, I want to view all my catches in a timeline so I can review my history at a glance.**

**Acceptance Criteria:**
- Catches listed reverse-chronologically
- Each item shows: thumbnail, species, date, location
- Infinite scroll pagination (load 50 at a time)
- Pull-to-refresh updates list
- Tap opens detail view

**Priority:** P0 (MVP Critical)

---

**US-005: As an angler, I want to filter my catches by species or date so I can analyze patterns.**

**Acceptance Criteria:**
- Filter button opens modal
- Filters: species (multi-select), date range, location
- Apply filters without reloading entire list
- Clear filters button resets to all catches
- Active filters shown as chips

**Priority:** P1 (MVP Enhancement)

---

**US-006: As an angler, I want to edit or delete catches so I can correct mistakes.**

**Acceptance Criteria:**
- Edit button on detail view opens form with current values
- Save edits updates catch in database
- Delete button shows confirmation dialog
- Deleted catches not recoverable (or move to trash for 30 days)

**Priority:** P1 (MVP Enhancement)

---

### Epic 3: Equipment Tracking

**US-007: As an angler, I want to catalog my fishing gear so I can remember what I used for each catch.**

**Acceptance Criteria:**
- Gear library with categories: Rods, Reels, Lures, Lines, Baits, Vessels
- Add new gear: name, category, brand, color, notes, photo
- Edit/delete gear entries
- Search gear by name

**Priority:** P2 (Phase 2)

---

**US-008: As an angler, I want to link gear to my catches so I can see which equipment is most effective.**

**Acceptance Criteria:**
- When logging catch, optional "Gear Used" section
- Multi-select gear items (e.g., rod + reel + lure)
- Gear success rate calculated: catches / uses
- Analytics view: "Top 10 Effective Lures" ranked by success rate

**Priority:** P2 (Phase 2)

---

### Epic 4: Predictions & Recommendations

**US-009: As an angler, I want the app to recommend when and where to fish so I can improve my success rate.**

**Acceptance Criteria:**
- Input: target species, location, date range
- Output: ranked time slots with success probability
- Explanation: "Based on 12 past catches in similar conditions"
- Save trip plan to calendar
- Minimum 10 catches required for predictions

**Priority:** P2 (Phase 2)

---

**US-010: As an angler, I want the app to notify me when conditions match my best fishing days so I don't miss opportunities.**

**Acceptance Criteria:**
- Opt-in push notifications
- Alert: "Conditions at Delta Coves match your top days (85% similarity)"
- Notification leads to trip planning screen
- User can disable notifications per location

**Priority:** P3 (Phase 3)

---

### Epic 5: Social & Sharing

**US-011: As an angler, I want to share my catches on social media so I can celebrate with friends.**

**Acceptance Criteria:**
- Share button on catch detail view
- Formatted image with photo + stats overlay
- Privacy: toggle location visibility (exact / general / hidden)
- One-tap share to Instagram, Facebook, Twitter
- Copy image to clipboard

**Priority:** P2 (Phase 2)

---

**US-012: As an angler, I want to see what others are catching nearby so I can learn from the community.**

**Acceptance Criteria:**
- Opt-in community feed (anonymous or named)
- Nearby catches (within 50 miles)
- Filter by species, date range
- No exact location pins (privacy)
- "Catch of the Day" feature

**Priority:** P3 (Phase 3, Community Features)

---

### Epic 6: Offline & Sync

**US-013: As an angler, I want to log catches without internet so I can use the app anywhere.**

**Acceptance Criteria:**
- Core features work offline (camera, manual entry, view cached catches)
- Catches queued for sync when online
- No data loss if app closes during offline session
- Sync indicator shows pending uploads

**Priority:** P3 (Phase 3)

---

## Technical Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Mobile App (React Native)                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   Camera    │  │  Catch Log  │  │  Analytics / Stats  │ │
│  │   Capture   │  │   Timeline  │  │     Dashboard       │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   Species   │  │  Equipment  │  │  Trip Planning /    │ │
│  │   Library   │  │   Catalog   │  │   Predictions       │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└──────────────────────────┬──────────────────────────────────┘
                           │ REST API (HTTPS)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   API Gateway (FastAPI)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   Auth       │  │   Catches    │  │   Predictions    │  │
│  │   Service    │  │   Service    │  │   Service        │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   Species    │  │   Equipment  │  │   Analytics      │  │
│  │   Service    │  │   Service    │  │   Service        │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
    ┌──────────────┐  ┌─────────┐  ┌─────────────┐
    │  PostgreSQL  │  │  Redis  │  │     S3      │
    │  (Catches,   │  │ (Cache) │  │   (Images)  │
    │  Users, Gear)│  │         │  │             │
    └──────────────┘  └─────────┘  └─────────────┘
            │
            ▼
    ┌─────────────────────────────────────────┐
    │        AI/ML Services                    │
    │  ┌──────────────┐  ┌─────────────────┐  │
    │  │   Species    │  │   Prediction    │  │
    │  │   ID Model   │  │   Engine        │  │
    │  │  (TensorFlow)│  │   (scikit)      │  │
    │  └──────────────┘  └─────────────────┘  │
    └─────────────────────────────────────────┘
            │
            ▼
    ┌─────────────────────────────────────────┐
    │        External APIs                     │
    │  ┌──────────────┐  ┌─────────────────┐  │
    │  │ OpenWeather  │  │  NOAA Tides &   │  │
    │  │     API      │  │  Currents API   │  │
    │  └──────────────┘  └─────────────────┘  │
    │  ┌──────────────┐  ┌─────────────────┐  │
    │  │  Solunar     │  │  Google Maps    │  │
    │  │  Calculator  │  │  Geocoding API  │  │
    │  └──────────────┘  └─────────────────┘  │
    └─────────────────────────────────────────┘
```

### Technology Stack

#### Frontend (Mobile App)
- **Framework:** React Native (cross-platform iOS/Android)
  - **Alternative:** SwiftUI (iOS-first, expand to Android later)
- **State Management:** Zustand or Redux Toolkit
- **Routing:** React Navigation
- **UI Components:** React Native Paper (Material Design) or NativeBase
- **Camera:** react-native-camera or expo-camera
- **Maps:** react-native-maps (Google Maps on Android, Apple Maps on iOS)
- **Offline Storage:** WatermelonDB or SQLite
- **Image Processing:** react-native-image-picker + EXIF extraction library

**Rationale:** React Native enables faster iteration with single codebase. Jeff's JS/TS proficiency aligns well. If performance becomes critical (e.g., real-time camera ML), consider SwiftUI for iOS first.

---

#### Backend (API)
- **Framework:** FastAPI (Python)
  - **Alternatives:** Django REST Framework (more batteries included but heavier)
- **Authentication:** JWT tokens (Auth0 or custom)
- **Rate Limiting:** slowapi (FastAPI middleware)
- **Background Tasks:** Celery + Redis (for async ML inference, email)
- **File Upload:** Direct S3 upload with pre-signed URLs (avoid API bottleneck)

**Rationale:** FastAPI chosen for speed, modern async support, and automatic OpenAPI docs. Python aligns with ML ecosystem (TensorFlow, scikit-learn).

---

#### Database
- **Primary:** PostgreSQL 15+
  - **Tables:** users, catches, species, equipment, trips, locations
  - **Extensions:** PostGIS (geospatial queries for location-based features)
- **Cache:** Redis (session tokens, API rate limits, prediction results)
- **Search:** PostgreSQL full-text search (Phase 1), Elasticsearch (Phase 3 if needed)

**Rationale:** Postgres robust, mature, excellent geospatial support via PostGIS. Redis for fast caching and job queue.

---

#### Storage
- **Images:** AWS S3 or Cloudflare R2 (cheaper egress)
- **CDN:** CloudFront or Cloudflare CDN (image delivery)
- **Backup:** S3 versioning + automated RDS snapshots

**Rationale:** S3 industry standard, reliable. R2 considered if cost becomes issue.

---

#### AI/ML Services
- **Species Identification:**
  - **Model:** Transfer learning with MobileNetV2 (TensorFlow/Keras)
  - **Training Data:** iNaturalist fish dataset + custom labeled data
  - **Inference:** TensorFlow Serving or hosted on Hugging Face
  - **Fallback:** Google Cloud Vision API (for species not in custom model)
- **Prediction Engine:**
  - **Approach:** Gradient Boosting (XGBoost or LightGBM)
  - **Features:** weather, tide, moon phase, time of day, historical catch rate
  - **Training:** scikit-learn pipeline, retrain monthly
- **Hosting:** AWS SageMaker or Hugging Face Inference Endpoints

**Rationale:** Transfer learning leverages existing fish classification models. MobileNetV2 optimized for mobile/edge. XGBoost proven for tabular data predictions.

---

#### DevOps & Hosting
- **Hosting:** AWS (primary) or Railway (simpler for MVP)
  - **API:** EC2 or ECS (containerized FastAPI)
  - **Database:** RDS PostgreSQL
  - **Storage:** S3
- **CI/CD:** GitHub Actions
  - Lint/test on PRs
  - Auto-deploy to staging on merge to `develop`
  - Manual deploy to production from `main`
- **Monitoring:** Sentry (errors), Datadog or New Relic (performance)
- **Logging:** CloudWatch or Logtail

**Rationale:** AWS scalable long-term. Railway simpler for early iterations. GitHub Actions free for public repos.

---

#### External APIs
- **Weather:** OpenWeatherMap (free tier: 1000 calls/day) or NOAA API
- **Tides:** NOAA Tides & Currents API (free, unlimited)
- **Geocoding:** Google Maps Geocoding API (reverse lat/lng → address)
- **Solunar:** Custom calculation (open-source algorithms, no API needed)
- **Maps:** Google Maps SDK (mobile) or Mapbox (if Google costs too high)

**Rationale:** NOAA APIs free and reliable. OpenWeatherMap freemium model fits MVP. Google Maps familiar UX.

---

### System Design Decisions

#### 1. Photo Upload Strategy
**Decision:** Direct S3 upload with pre-signed URLs (client-side upload).

**Why:**
- Reduces API server load (no proxy)
- Faster for user (parallel upload while processing EXIF)
- Lower bandwidth costs

**Flow:**
1. Client requests pre-signed URL from API
2. Client uploads image directly to S3
3. Client sends catch data + S3 URL to API
4. API creates catch record with image reference

---

#### 2. Species Identification Approach
**Decision:** Hybrid model (custom ML + fallback to cloud API).

**Why:**
- Custom model for common species (fast, offline-capable)
- Cloud API for rare/edge cases (cost-effective, high accuracy)
- Gradual improvement via user feedback

**Flow:**
1. Client sends image to API (or runs model on-device if possible)
2. API runs custom model inference
3. If confidence >70%, return result
4. If confidence <70%, call Google Cloud Vision API
5. Return top 3 suggestions, user confirms
6. User confirmation trains model (store correct label)

---

#### 3. Offline Sync Strategy
**Decision:** Last-write-wins with client timestamp for conflict resolution.

**Why:**
- Simplest to implement for MVP
- Low conflict probability (single user editing own data)
- User expectation: device state is "truth"

**Flow:**
1. User edits catch offline
2. Local DB updated, marked "pending sync"
3. When online, client sends catch data + timestamp
4. Server checks if server-side timestamp is newer
5. If server newer, conflict modal: "Server has newer data, overwrite?"
6. If client newer or no conflict, server accepts update

---

#### 4. Prediction Model Training
**Decision:** Batch training (monthly retraining on aggregated data).

**Why:**
- Real-time training unnecessary for fishing predictions (slow-changing patterns)
- Monthly cadence balances model freshness with cost
- Sufficient user data accumulates over weeks

**Flow:**
1. Cron job runs 1st of each month
2. Extract features from all catches (weather, tide, moon, catch success)
3. Train XGBoost model, evaluate on holdout set
4. If accuracy improves, deploy new model to production
5. Rollback if accuracy degrades

---

## Data Models

### Database Schema (PostgreSQL)

#### Table: `users`
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    profile_photo_url TEXT,
    subscription_tier VARCHAR(20) DEFAULT 'free', -- 'free', 'pro'
    subscription_expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    last_login_at TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
```

---

#### Table: `catches`
```sql
CREATE TABLE catches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    species_id UUID REFERENCES species(id),
    photo_url TEXT NOT NULL,
    
    -- Location
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    location_name VARCHAR(255), -- e.g., "Sherman Island, CA"
    
    -- Catch details
    caught_at TIMESTAMP NOT NULL,
    length_inches DECIMAL(5, 2),
    weight_pounds DECIMAL(6, 2),
    
    -- Conditions (auto-populated)
    weather_temp_f INT,
    weather_conditions VARCHAR(100), -- e.g., "Partly Cloudy"
    wind_speed_mph INT,
    wind_direction VARCHAR(10), -- e.g., "NE"
    tide_state VARCHAR(20), -- e.g., "Incoming"
    tide_height_ft DECIMAL(4, 2),
    moon_phase VARCHAR(50), -- e.g., "Waning Gibbous"
    moon_illumination_percent INT,
    
    -- User notes
    notes TEXT,
    catch_and_release BOOLEAN DEFAULT true,
    
    -- Equipment (many-to-many via junction table)
    
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_catches_user_id ON catches(user_id);
CREATE INDEX idx_catches_species_id ON catches(species_id);
CREATE INDEX idx_catches_caught_at ON catches(caught_at);
CREATE INDEX idx_catches_location ON catches USING GIST (ST_Point(longitude, latitude)); -- PostGIS
```

---

#### Table: `species`
```sql
CREATE TABLE species (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    common_name VARCHAR(255) NOT NULL,
    scientific_name VARCHAR(255),
    description TEXT,
    thumbnail_url TEXT,
    habitat VARCHAR(100), -- 'freshwater', 'saltwater', 'brackish'
    conservation_status VARCHAR(50), -- e.g., "Least Concern"
    noaa_fishwatch_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_species_common_name ON species(common_name);
```

---

#### Table: `equipment`
```sql
CREATE TABLE equipment (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    category VARCHAR(50) NOT NULL, -- 'rod', 'reel', 'lure', 'line', 'bait', 'vessel'
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255),
    color VARCHAR(100),
    photo_url TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_equipment_user_id ON equipment(user_id);
CREATE INDEX idx_equipment_category ON equipment(category);
```

---

#### Table: `catch_equipment` (Junction Table)
```sql
CREATE TABLE catch_equipment (
    catch_id UUID NOT NULL REFERENCES catches(id) ON DELETE CASCADE,
    equipment_id UUID NOT NULL REFERENCES equipment(id) ON DELETE CASCADE,
    PRIMARY KEY (catch_id, equipment_id)
);
```

---

#### Table: `trips`
```sql
CREATE TABLE trips (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    planned_at TIMESTAMP NOT NULL,
    location_name VARCHAR(255),
    target_species_id UUID REFERENCES species(id),
    predicted_success_probability DECIMAL(3, 2), -- e.g., 0.85 for 85%
    notes TEXT,
    status VARCHAR(20) DEFAULT 'planned', -- 'planned', 'completed', 'cancelled'
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_trips_user_id ON trips(user_id);
CREATE INDEX idx_trips_planned_at ON trips(planned_at);
```

---

#### Table: `locations` (Saved Spots)
```sql
CREATE TABLE locations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    description TEXT,
    is_public BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_locations_user_id ON locations(user_id);
```

---

### JSON Data Structures (API Responses)

#### Catch Object
```json
{
  "id": "a3f2b8c9-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
  "userId": "user-uuid",
  "species": {
    "id": "species-uuid",
    "commonName": "Largemouth Bass",
    "scientificName": "Micropterus salmoides"
  },
  "photoUrl": "https://cdn.catchbook.app/catches/abc123.jpg",
  "location": {
    "latitude": 38.0522,
    "longitude": -121.8052,
    "name": "Sherman Island, CA"
  },
  "caughtAt": "2025-11-29T07:15:00Z",
  "lengthInches": 18.5,
  "weightPounds": 3.2,
  "conditions": {
    "weatherTempF": 58,
    "weatherConditions": "Partly Cloudy",
    "windSpeedMph": 5,
    "windDirection": "NE",
    "tideState": "Incoming",
    "tideHeightFt": 2.1,
    "moonPhase": "Waning Gibbous",
    "moonIlluminationPercent": 68
  },
  "notes": "Caught on watermelon Senko, Texas-rigged. Great fight!",
  "catchAndRelease": true,
  "equipment": [
    {
      "id": "gear-uuid-1",
      "name": "Senko Worm - Watermelon",
      "category": "lure"
    },
    {
      "id": "gear-uuid-2",
      "name": "Shimano Curado K",
      "category": "reel"
    }
  ],
  "createdAt": "2025-11-29T07:20:00Z",
  "updatedAt": "2025-11-29T07:20:00Z"
}
```

---

## API Design

### RESTful API Endpoints

**Base URL:** `https://api.catchbook.app/v1`

#### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Create new user account |
| POST | `/auth/login` | Login (returns JWT token) |
| POST | `/auth/refresh` | Refresh JWT token |
| POST | `/auth/logout` | Invalidate token |
| POST | `/auth/forgot-password` | Request password reset |
| POST | `/auth/reset-password` | Reset password with token |

**Example: Login**
```http
POST /v1/auth/login
Content-Type: application/json

{
  "email": "jeff@example.com",
  "password": "securepassword123"
}

Response:
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refreshToken": "refresh-token-here",
  "expiresIn": 3600,
  "user": {
    "id": "user-uuid",
    "email": "jeff@example.com",
    "fullName": "Jeff Hutting",
    "subscriptionTier": "pro"
  }
}
```

---

#### Catches

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/catches` | List all catches (paginated, filtered) |
| GET | `/catches/{id}` | Get single catch by ID |
| POST | `/catches` | Create new catch |
| PUT | `/catches/{id}` | Update catch |
| DELETE | `/catches/{id}` | Delete catch |
| POST | `/catches/upload` | Request pre-signed S3 URL for photo upload |

**Example: Create Catch**
```http
POST /v1/catches
Authorization: Bearer {jwt-token}
Content-Type: application/json

{
  "photoUrl": "https://s3.amazonaws.com/catchbook/uploads/abc123.jpg",
  "caughtAt": "2025-11-29T07:15:00Z",
  "latitude": 38.0522,
  "longitude": -121.8052,
  "speciesId": "species-uuid", // from species ID endpoint
  "lengthInches": 18.5,
  "weightPounds": 3.2,
  "notes": "Great catch on Senko!",
  "catchAndRelease": true,
  "equipmentIds": ["gear-uuid-1", "gear-uuid-2"]
}

Response:
{
  "id": "catch-uuid",
  "userId": "user-uuid",
  "species": { ... },
  "photoUrl": "https://cdn.catchbook.app/catches/abc123.jpg",
  "location": {
    "latitude": 38.0522,
    "longitude": -121.8052,
    "name": "Sherman Island, CA"
  },
  "caughtAt": "2025-11-29T07:15:00Z",
  "conditions": {
    "weatherTempF": 58,
    "weatherConditions": "Partly Cloudy",
    "windSpeedMph": 5,
    "windDirection": "NE",
    "tideState": "Incoming",
    "tideHeightFt": 2.1,
    "moonPhase": "Waning Gibbous",
    "moonIlluminationPercent": 68
  },
  "lengthInches": 18.5,
  "weightPounds": 3.2,
  "notes": "Great catch on Senko!",
  "catchAndRelease": true,
  "equipment": [ ... ],
  "createdAt": "2025-11-29T07:20:00Z",
  "updatedAt": "2025-11-29T07:20:00Z"
}
```

---

#### Species

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/species` | List all species (filterable by habitat) |
| GET | `/species/{id}` | Get single species by ID |
| POST | `/species/identify` | Identify species from photo (AI) |

**Example: Species Identification**
```http
POST /v1/species/identify
Authorization: Bearer {jwt-token}
Content-Type: multipart/form-data

{
  "photo": (binary image data)
}

Response:
{
  "suggestions": [
    {
      "speciesId": "species-uuid-1",
      "commonName": "Largemouth Bass",
      "confidence": 0.87
    },
    {
      "speciesId": "species-uuid-2",
      "commonName": "Smallmouth Bass",
      "confidence": 0.11
    }
  ],
  "topMatch": {
    "speciesId": "species-uuid-1",
    "commonName": "Largemouth Bass",
    "confidence": 0.87
  }
}
```

---

#### Equipment

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/equipment` | List user's equipment |
| GET | `/equipment/{id}` | Get single equipment item |
| POST | `/equipment` | Create equipment |
| PUT | `/equipment/{id}` | Update equipment |
| DELETE | `/equipment/{id}` | Delete equipment |

---

#### Analytics

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/analytics/summary` | Overall stats (total catches, species breakdown) |
| GET | `/analytics/success-rate` | Catch rate by condition |
| GET | `/analytics/equipment-effectiveness` | Top-performing gear |
| GET | `/analytics/heatmap` | Catch density by location (Pro) |

**Example: Summary**
```http
GET /v1/analytics/summary
Authorization: Bearer {jwt-token}

Response:
{
  "totalCatches": 47,
  "topSpecies": {
    "speciesId": "species-uuid",
    "commonName": "Largemouth Bass",
    "count": 18
  },
  "bestMonth": {
    "month": "June",
    "year": 2025,
    "count": 12
  },
  "favoriteLocation": {
    "name": "Delta Coves",
    "count": 9
  }
}
```

---

#### Predictions

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/predictions/recommend` | Get trip recommendations |
| GET | `/predictions/conditions` | Current conditions for location |

**Example: Trip Recommendation**
```http
POST /v1/predictions/recommend
Authorization: Bearer {jwt-token}
Content-Type: application/json

{
  "targetSpeciesId": "species-uuid",
  "locationName": "Sherman Island",
  "dateRange": {
    "start": "2025-12-07",
    "end": "2025-12-08"
  }
}

Response:
{
  "recommendations": [
    {
      "date": "2025-12-07",
      "timeRange": "06:00-09:00",
      "successProbability": 0.85,
      "reasoning": "Based on 12 past catches in similar conditions",
      "conditions": {
        "weather": "Overcast, 55°F",
        "tide": "Incoming",
        "moon": "Waning Gibbous"
      }
    },
    {
      "date": "2025-12-08",
      "timeRange": "05:30-08:30",
      "successProbability": 0.72,
      "reasoning": "High tide, cooler temps match top 20% of your catches",
      "conditions": {
        "weather": "Clear, 50°F",
        "tide": "High",
        "moon": "Waning Gibbous"
      }
    }
  ]
}
```

---

#### Trips (Phase 2)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/trips` | List planned trips |
| GET | `/trips/{id}` | Get single trip |
| POST | `/trips` | Create trip plan |
| PUT | `/trips/{id}` | Update trip |
| DELETE | `/trips/{id}` | Delete trip |

---

## AI/ML Integration Points

### 1. Species Identification

**Technology:** Transfer Learning with MobileNetV2 (TensorFlow)

**Training Data:**
- iNaturalist Fish Dataset: 10,000+ labeled images
- FishBase: Scientific database with species images
- User-submitted photos (with confirmed labels)

**Training Pipeline:**
1. Start with pre-trained MobileNetV2 (ImageNet weights)
2. Fine-tune top layers on fish dataset
3. Data augmentation: rotation, brightness, zoom (fish often in varying light/angles)
4. Train/validation split: 80/20
5. Target: >85% top-1 accuracy, >95% top-3 accuracy

**Inference:**
- Client sends image → API endpoint
- Image preprocessed (resize 224x224, normalize)
- Model inference (TensorFlow Serving)
- Return top 3 predictions with confidence scores
- If top confidence <70%, fallback to Google Cloud Vision API

**Continuous Improvement:**
- User confirms species → store (image, correct_label)
- Weekly batch retraining on new labeled data
- A/B test new models before deployment

---

### 2. Catch Prediction Engine

**Technology:** Gradient Boosting (XGBoost or LightGBM)

**Features (Input):**
- **Environmental:**
  - Temperature (°F)
  - Wind speed (mph)
  - Wind direction (categorical: N, NE, E, SE, S, SW, W, NW)
  - Cloud cover (percentage)
  - Precipitation (binary: yes/no)
  - Tide state (categorical: high, incoming, low, outgoing)
  - Tide height (feet)
  - Moon phase (categorical: new, waxing crescent, first quarter, waxing gibbous, full, waning gibbous, last quarter, waning crescent)
  - Moon illumination (percentage)
- **Temporal:**
  - Time of day (hour)
  - Day of week (categorical)
  - Month (categorical)
  - Season (categorical: spring, summer, fall, winter)
- **Historical:**
  - User's catch rate at location (catches per trip)
  - Species prevalence in season (percentage of catches)
- **User Preferences:**
  - Target species (categorical)
  - Preferred location (categorical)

**Target (Output):**
- Catch success (binary: 0 = no catch, 1 = catch)
- Success probability (regression: 0.0 to 1.0)

**Training Pipeline:**
1. Extract features from all catches + non-catch trips (if user logs unsuccessful trips)
2. Merge with historical weather/tide data (NOAA APIs)
3. Split: 70% train, 15% validation, 15% test
4. Train XGBoost classifier:
   - Objective: binary:logistic
   - Evaluation metric: AUC-ROC
5. Hyperparameter tuning (learning rate, max_depth, n_estimators)
6. Deploy model if AUC >0.75

**Inference:**
- User requests recommendation → API calls prediction service
- Fetch weather forecast for next 7 days
- For each date/time slot, compute features
- Predict success probability for each slot
- Rank slots by probability
- Return top 5 recommendations with explanations

**Continuous Improvement:**
- Monthly retraining on new catch data
- Feature importance analysis → drop weak features
- A/B test model versions (10% traffic to new model)

---

### 3. Condition Similarity Search (Optional Phase 3)

**Use Case:** "Find other catches with similar conditions to today."

**Technology:** K-Nearest Neighbors (KNN) or cosine similarity

**Approach:**
1. Represent each catch as feature vector (weather, tide, moon, time)
2. Normalize features (standard scaling)
3. For query conditions, compute distance to all catches
4. Return top 10 most similar catches

**Purpose:**
- Show user: "You caught 3 bass on days like this"
- Power predictions: "Users with similar patterns succeeded here"

---

## External API Dependencies

### 1. Weather API
**Provider:** OpenWeatherMap or NOAA Weather API

**Endpoints Used:**
- Current weather: `/weather?lat={lat}&lon={lon}`
- Historical weather: `/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}`
- 7-day forecast: `/forecast?lat={lat}&lon={lon}`

**Rate Limits:**
- Free tier: 1,000 calls/day (OpenWeatherMap)
- Caching strategy: Cache current weather for 30 minutes, forecast for 6 hours

**Data Extracted:**
- Temperature (°F)
- Conditions (clear, cloudy, rainy, etc.)
- Wind speed/direction
- Cloud cover percentage
- Precipitation

---

### 2. Tide API
**Provider:** NOAA Tides & Currents API

**Endpoints Used:**
- Tide predictions: `/api/datagetter?product=predictions&station={station_id}&date={date}`
- Nearest station: `/mdapi/v1.0/webapi/stations?type=tidepredictions&lat={lat}&lon={lon}`

**Rate Limits:**
- Unlimited (NOAA is government, free)
- Caching: Cache tide data for 24 hours (predictions don't change)

**Data Extracted:**
- Tide state (high, low, incoming, outgoing)
- Tide height (feet)
- Next high/low tide times

---

### 3. Geocoding API
**Provider:** Google Maps Geocoding API

**Endpoints Used:**
- Reverse geocoding: `/maps/api/geocode/json?latlng={lat},{lon}`

**Rate Limits:**
- Free tier: $200/month credit (~28,000 requests)
- Caching: Cache location names for 30 days (rarely change)

**Data Extracted:**
- Human-readable address: "Sherman Island, CA"
- Locality, state, country

---

### 4. Solunar Calculator
**Provider:** Custom implementation (no API needed)

**Algorithm:**
- Based on moon position and sun position
- Major periods: Moon overhead or underfoot (2 hours)
- Minor periods: Moon rising or setting (1 hour)
- Calculate from lat/lon + date/time

**Libraries:**
- Python: `ephem` or `astral` (astronomical calculations)
- JavaScript: `suncalc` or `lunarphase-js`

**Data Returned:**
- Major period times: ["06:15-08:15", "18:30-20:30"]
- Minor period times: ["00:45-01:45", "12:15-13:15"]
- Moon phase and illumination percentage

---

### 5. Image Storage & CDN
**Provider:** AWS S3 + CloudFront or Cloudflare R2 + CDN

**Flow:**
1. Client requests pre-signed URL from API
2. Client uploads image directly to S3
3. CloudFront serves images via CDN (fast global delivery)

**Cost:**
- S3 storage: ~$0.023/GB/month
- CloudFront: ~$0.085/GB transfer (first 10TB)
- Budget: 10,000 users, 2 photos/month avg, 2MB/photo = 40GB/month = ~$1/month storage + $3.40/month CDN = ~$4.40/month

---

## Mobile-First Design

### Design Principles

1. **Thumb-Friendly Navigation:**
   - Bottom tab bar (Home, Catch, Stats, Gear, Profile)
   - Primary actions at bottom (e.g., "New Catch" floating action button)
   - Avoid top-left hamburger menus (hard to reach one-handed)

2. **Minimal Cognitive Load:**
   - One primary action per screen
   - Progressive disclosure (advanced features in "More" section)
   - Smart defaults (auto-detect location, pre-fill species)

3. **Offline-First:**
   - Core features work without internet (camera, view cached catches)
   - Clear offline indicator (yellow banner: "Offline Mode")
   - Auto-sync when connectivity returns

4. **Fast Data Entry:**
   - Photo capture = 1 tap
   - Species confirmation = 1 tap (from AI suggestions)
   - Save catch = 1 tap (if user doesn't edit)
   - Target: <10 seconds from catch to logged

5. **Glove-Friendly Targets:**
   - Minimum tap target: 44x44pt (iOS) / 48x48dp (Android)
   - High contrast buttons (fishing often in bright sun)
   - Simple forms with large inputs

---

### Screen Hierarchy

#### Home Screen (Tab 1)
- **Header:** User greeting + weather widget for current location
- **Body:**
  - Quick actions: "New Catch" (large button), "Start Trip"
  - Recent catches (last 5, scrollable horizontally)
  - Tip of the day (random fishing insight)
- **Navigation:** Bottom tab bar

#### Catch Log (Tab 2)
- **Header:** Search bar + filter icon
- **Body:**
  - Vertical list of catches (infinite scroll)
  - Each card: thumbnail, species, date, location
  - Pull-to-refresh
- **Navigation:** Tap card → detail view

#### Stats (Tab 3)
- **Header:** Date range picker (default: last 30 days)
- **Body:**
  - 4 stat tiles: Total Catches, Top Species, Best Month, Favorite Spot
  - Charts: Species pie chart, monthly bar chart
  - Pro upsell banner (if free user)
- **Navigation:** Tap tile → drill-down view

#### Gear (Tab 4)
- **Header:** Search bar + "Add Gear" button
- **Body:**
  - Segmented control: All / Rods / Reels / Lures / Lines / Baits / Vessels
  - Grid of gear items (photo + name)
- **Navigation:** Tap item → detail view

#### Profile (Tab 5)
- **Header:** Profile photo + name + subscription badge
- **Body:**
  - Settings: Account, Notifications, Privacy, Units (metric/imperial)
  - About: Help, Terms, Privacy Policy
  - Subscription: Upgrade to Pro (if free)
  - Logout
- **Navigation:** Tap setting → detail screen

---

### Key User Flows

#### Flow 1: Log a Catch (Happy Path)
1. User taps "New Catch" button
2. Camera opens
3. User snaps photo
4. Processing screen (spinner): "Identifying species..."
5. Review screen appears with pre-filled data:
   - Photo preview
   - Species: "Largemouth Bass" (dropdown, editable)
   - Location: "Sherman Island, CA" (map, editable)
   - Date/Time: "Nov 29, 2025, 7:15 AM" (editable)
   - Length: [Input field, optional]
   - Weight: [Input field, optional]
   - Gear: [Multi-select, optional]
   - Notes: [Text area, optional]
   - Catch & Release toggle (default: ON)
6. User taps "Save"
7. Success toast: "Catch logged!"
8. Redirects to catch detail view

**Time to complete:** <10 seconds if no edits.

---

#### Flow 2: Plan a Trip
1. User taps "Plan" from Home screen
2. Form screen:
   - Target Species: [Dropdown]
   - Location: [Saved spots dropdown or "Use Current Location"]
   - Date Range: [Date picker, default: this weekend]
3. User taps "Get Recommendations"
4. Loading spinner (3-5 seconds)
5. Results screen:
   - List of recommended time slots (ranked by probability)
   - Each slot: Date/time, success %, conditions summary
6. User taps slot → detail view with weather/tide breakdown
7. User taps "Save Trip"
8. Trip added to calendar (iOS Calendar / Google Calendar)

---

#### Flow 3: View Analytics
1. User taps "Stats" tab
2. Dashboard loads (1-2 seconds)
3. User sees 4 stat tiles + 2 charts
4. User taps "Top Species" tile
5. Drill-down view: List of all species with catch counts + percentages
6. User taps "Largemouth Bass"
7. Species detail view: All catches of this species, success rate by month, top locations

---

### Accessibility Considerations
- **VoiceOver / TalkBack support:** All images have alt text, buttons have labels
- **Dark mode:** Full support (fishing often early morning/late evening)
- **Colorblind-friendly:** Don't rely on color alone (use icons + text)
- **Font scaling:** Respect system font size preferences

---

## Monetization Strategy

### Freemium Model

#### Free Tier
**Features:**
- Unlimited catch logging
- Species identification (AI)
- Basic analytics (total catches, species breakdown)
- Equipment catalog
- 1 saved location
- Basic map view

**Limitations:**
- Catch history limited to last 6 months
- No predictions/recommendations
- No heatmaps or advanced analytics
- Ads (non-intrusive banner at bottom of some screens)
- Export to CSV limited to 50 catches

**Goal:** Hook users with core value (effortless logging), upsell to Pro for intelligence features.

---

#### Pro Tier ($4.99/month or $39.99/year)
**Features:**
- Everything in Free
- **Unlimited catch history**
- **Trip predictions & recommendations** (AI-powered)
- **Advanced analytics:**
  - Heatmaps (catch density by location)
  - Condition correlation ("You catch 40% more when...")
  - Year-over-year comparisons
  - Equipment effectiveness rankings
- **Unlimited saved locations**
- **Offline mode** (full functionality without internet)
- **Export to CSV/JSON** (unlimited)
- **Priority support**
- **Ad-free experience**
- **Early access to new features**

**Target:** 20% conversion rate from free to Pro (industry standard for fishing apps: 10-25%).

---

### Pricing Rationale

**Monthly:** $4.99
- Competitive with Fishbrain ($4.99), Anglr ($9.99 for hardware + subscription)
- Below premium tier of other apps ($9.99-14.99)
- Psychological threshold: <$5 impulse buy

**Annual:** $39.99 (saves $20/year, 33% discount)
- Encourages long-term commitment
- Reduces churn (annual subscribers 50% less likely to cancel)
- Upfront cash flow for development

---

### Revenue Projections

**Year 1 (Months 1-12):**
- Target users: 5,000 (conservative)
- Free: 4,000 (80%)
- Pro: 1,000 (20%)
- Average subscription value: $3/user/month (mix of monthly/annual)
- **MRR:** $3,000/month
- **ARR:** $36,000

**Year 2 (Months 13-24):**
- Target users: 25,000 (5x growth via marketing)
- Free: 20,000 (80%)
- Pro: 5,000 (20%)
- **MRR:** $15,000/month
- **ARR:** $180,000

**Year 3 (Months 25-36):**
- Target users: 100,000 (4x growth)
- Free: 80,000 (80%)
- Pro: 20,000 (20%)
- **MRR:** $60,000/month
- **ARR:** $720,000

---

### Alternative Revenue Streams (Future)

1. **Affiliate Partnerships:**
   - Tackle manufacturers: "Buy this lure" link (5-10% commission)
   - Boat/kayak brands: Referral program
   - Fishing guides: Booking integration (10% commission)

2. **Sponsored Content (Non-Intrusive):**
   - "Tip of the Day" sponsored by brand (e.g., "Tip from Rapala")
   - Native ads in community feed (clearly labeled)

3. **Data Licensing (Anonymized):**
   - Sell aggregated catch data to conservation orgs, fishery managers
   - Example: "Heatmap of bass populations in California Delta"
   - Privacy-first: Opt-in only, fully anonymized

4. **Premium Hardware Integrations:**
   - Bluetooth fish scale: Auto-log weight (sell hardware or partner with Berkley, Rapala)
   - Smart rod holders: Track bites/strikes
   - Partner with Garmin, Lowrance for marine electronics sync

---

## Success Metrics

### North Star Metric
**Weekly Active Loggers (WAL):** Number of users logging at least 1 catch per week.

**Why:** Indicates product-market fit. If users log consistently, they find value.

**Target:**
- Month 3: 200 WAL
- Month 6: 500 WAL
- Month 12: 2,000 WAL

---

### Primary Metrics (KPIs)

#### 1. User Acquisition
- **New signups per week**
  - Target: 100/week by Month 6
- **Signup source breakdown** (organic, social, referral, ads)
- **Cost per acquisition (CPA)** (if paid ads used)
  - Target: <$5 CPA

#### 2. Engagement
- **Daily Active Users (DAU)**
  - Target: 30% of Monthly Active Users (MAU)
- **Catches logged per user per month**
  - Target: 4 catches/user/month (1 catch per week for active users)
- **Session duration**
  - Target: 5 minutes avg (enough time to log + browse)
- **Features adopted** (% users who use equipment catalog, analytics, predictions)
  - Target: 50% use equipment, 30% use analytics, 10% use predictions (free users)

#### 3. Retention
- **Day 1, Day 7, Day 30 retention**
  - Target: Day 1: 60%, Day 7: 40%, Day 30: 25%
- **Churn rate (monthly)**
  - Target: <5% monthly churn for Pro subscribers

#### 4. Monetization
- **Free-to-Pro conversion rate**
  - Target: 20% within 90 days of signup
- **Monthly Recurring Revenue (MRR)**
  - See projections above
- **Average Revenue Per User (ARPU)**
  - Target: $3/user/month (blended free + Pro)
- **Customer Lifetime Value (LTV)**
  - Target: $50 (assuming 1.5 years avg subscription duration)

#### 5. Product Quality
- **Species ID accuracy** (user confirmations vs. AI predictions)
  - Target: >85% top-1 accuracy, >95% top-3
- **App crash rate**
  - Target: <1% of sessions
- **API error rate**
  - Target: <0.5% of requests
- **Time to log catch** (photo to save)
  - Target: <10 seconds avg

---

### Secondary Metrics

- **Community engagement** (if community feed launched):
  - Posts per week
  - Likes/comments per post
- **Referral rate:**
  - % users who invite friends
  - Referrals per user
- **Net Promoter Score (NPS):**
  - Survey: "How likely are you to recommend Catchbook?" (0-10)
  - Target: NPS >50 (promoters - detractors)
- **Customer support tickets:**
  - Volume per week
  - Resolution time
  - Common issues (prioritize bug fixes)

---

### Instrumentation (Analytics Tools)

- **Mixpanel or Amplitude:** Event tracking (catch logged, species identified, Pro upgrade, etc.)
- **Google Analytics 4:** Web landing page + blog traffic
- **App Store / Google Play Console:** Download stats, reviews, ratings
- **Stripe / RevenueCat:** Subscription metrics (MRR, churn, cohort analysis)
- **Sentry:** Error tracking and performance monitoring
- **Hotjar / FullStory:** Session replays (understand user friction points)

---

## Go-to-Market Strategy

### Pre-Launch (Months 1-3: Development Phase)

#### 1. Build Landing Page
- **Goal:** Collect email signups for beta access
- **Content:**
  - Hero: "Log Your Catches in Seconds, Not Minutes"
  - Problem statement: "Tired of typing every detail after a long day fishing?"
  - Solution: "Catchbook uses AI to auto-fill your catch data from photos."
  - Features: Photo capture, species ID, predictions, equipment tracking
  - Call-to-action: "Join the Beta Waitlist"
- **Tech:** Next.js + Vercel (simple, fast deployment)
- **SEO:** Target keywords: "fishing journal app", "catch logging app", "AI fishing assistant"

#### 2. Build Social Presence
- **Instagram:** Post fishing tips, teaser videos of app features
  - Goal: 500 followers by launch
- **YouTube:** Short tutorials (how to use app, fishing tips)
  - Goal: 100 subscribers, 5 videos published
- **Facebook Group:** "Catchbook Beta Testers" (private group)
  - Goal: 200 members by beta launch
- **Reddit:** Engage in r/kayakfishing, r/bassfishing (no spam, add value first)

#### 3. Beta Testing
- **Recruit:** 50-100 beta testers from waitlist + personal network
- **Tools:** TestFlight (iOS), Google Play Console (Android)
- **Feedback:** Weekly surveys, in-app feedback button, Slack/Discord channel
- **Incentive:** Lifetime Pro subscription for early adopters

---

### Launch (Month 4)

#### 1. App Store Optimization (ASO)
- **App Name:** Catchbook: AI Fishing Journal
- **Subtitle:** Effortless Catch Logging & Smart Predictions
- **Keywords:** fishing journal, catch log, species ID, fishing diary, fish tracker, AI fishing, kayak fishing
- **Screenshots:** Show key features (photo capture, auto-population, analytics)
- **Preview Video:** 15-30 seconds showing log-a-catch flow

#### 2. Press & Media
- **Press Release:** Distribute via PRWeb, EIN Presswire
  - Angle: "New AI-Powered App Eliminates Fishing Logbook Drudgery"
- **Pitch to fishing media:**
  - Bassmaster Magazine, Field & Stream, In-Fisherman, Kayak Angler Magazine
  - Offer free 6-month Pro access to journalists for review
- **Tech media (if AI angle compelling):**
  - TechCrunch, Product Hunt, Hacker News (Show HN)

#### 3. Product Hunt Launch
- **Goal:** Top 5 Product of the Day
- **Strategy:**
  - Post on Tuesday-Thursday (best engagement)
  - Prepare GIFs/videos showing app in action
  - Engage with commenters all day
  - Ask beta testers to upvote/comment
- **Outcome:** Drive 500-1,000 signups from Product Hunt

#### 4. Influencer Partnerships
- **Target:** YouTube fishing channels (10k-100k subscribers)
  - Offer free Pro subscription + affiliate link (10% commission)
  - Example: "1Rod1ReelFishing", "TacticalBassin"
- **Ask:** Review video or mention in "Top Fishing Apps" roundup

---

### Post-Launch Growth (Months 5-12)

#### 1. Content Marketing
- **Blog:** catchbook.app/blog
  - SEO articles: "How to Identify Bass Species", "Best Lures for Kayak Fishing", "Solunar Calendar Explained"
  - Target long-tail keywords: "how to log fishing catches", "best fishing journal apps"
- **Frequency:** 2 articles/month
- **Goal:** Organic traffic: 1,000 visits/month by Month 12

#### 2. Paid Ads (if budget allows)
- **Platforms:** Facebook Ads, Google Ads
- **Budget:** $500-1,000/month
- **Targeting:**
  - Facebook: Interest-based (fishing, kayaking, outdoor recreation)
  - Google: Search ads for "fishing app", "catch tracker"
- **Goal:** CPA <$5, 200 signups/month from paid

#### 3. Referral Program
- **Incentive:** "Invite 3 friends → Get 1 month Pro free"
- **Mechanism:** Unique referral link, track signups
- **Goal:** 10% of users refer at least 1 friend

#### 4. Community Building
- **Launch community feed** (opt-in, Phase 2)
  - "Catch of the Day" feature
  - Leaderboards (most catches, biggest fish by species)
  - User-generated content: fishing reports, hot spots
- **Host virtual events:**
  - "Catchbook Challenge" (most catches logged in a month)
  - Live Q&A with fishing guides/experts

#### 5. Partnerships
- **Tackle shops:** Display QR code in stores → download app
- **Fishing tournaments:** Sponsor local kayak tournaments, offer free Pro to participants
- **Conservation orgs:** Partner with Trout Unlimited, Bass Federation → promote catch-and-release logging

---

### Metrics for Go-to-Market Success

| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|
| Landing page live | Month 1 | 100 email signups |
| Beta launch | Month 3 | 50 active testers, 500 catches logged |
| App Store launch | Month 4 | 500 downloads in Week 1 |
| Product Hunt | Month 4 | Top 10 Product of the Day |
| First 1,000 users | Month 5 | 1,000 signups |
| First $1,000 MRR | Month 6 | 200 Pro subscribers |
| 5,000 users | Month 9 | 5,000 signups, 1,000 WAL |
| $3,000 MRR | Month 12 | 600 Pro subscribers |

---

## Development Roadmap

### Phase 1: MVP (Months 1-4)

**Goal:** Ship core product with photo capture, species ID, catch logging.

| Week | Milestone | Deliverables |
|------|-----------|--------------|
| 1-2 | Project setup | GitHub repo, CI/CD, dev environment, architecture decisions |
| 3-4 | Database & API foundation | Postgres schema, FastAPI skeleton, auth endpoints |
| 5-6 | Photo capture + S3 upload | React Native camera integration, pre-signed URLs |
| 7-8 | Species ID (ML model) | Train initial model, deploy API endpoint |
| 9-10 | Catch logging CRUD | Create/read/update/delete catches, detail views |
| 11-12 | Conditions auto-population | Weather/tide/moon APIs, background jobs |
| 13-14 | Basic analytics | Stats dashboard, charts (species breakdown, monthly activity) |
| 15-16 | Beta testing & iteration | Fix bugs, refine UX, collect feedback |

**Deliverables:**
- iOS app (TestFlight)
- Android app (Google Play Console beta track)
- API (hosted on Railway or AWS)
- Database (Postgres on Railway or RDS)
- 50+ beta testers actively logging

---

### Phase 2: Expansion (Months 5-8)

**Goal:** Add equipment tracking, predictions, social sharing.

| Week | Milestone | Deliverables |
|------|-----------|--------------|
| 17-18 | Equipment catalog | CRUD for gear, link to catches |
| 19-20 | Equipment analytics | Success rate calculations, top gear rankings |
| 21-22 | Prediction engine (v1) | Train XGBoost model, API endpoint |
| 23-24 | Trip planning UI | Recommendations screen, save trips |
| 25-26 | Social sharing | Share cards, Instagram/Facebook integration |
| 27-28 | Offline mode (basic) | Local DB (WatermelonDB), sync queue |
| 29-30 | Pro tier launch | Paywall, Stripe integration, subscription management |
| 31-32 | Marketing push | Content, ads, influencer outreach |

**Deliverables:**
- Equipment features live
- Predictions live (Pro only)
- Pro subscriptions enabled
- 1,000+ active users
- $1,000 MRR

---

### Phase 3: Advanced Features (Months 9-12)

**Goal:** Polish product, add community features, scale infrastructure.

| Week | Milestone | Deliverables |
|------|-----------|--------------|
| 33-34 | Advanced analytics | Heatmaps, condition correlation, year-over-year |
| 35-36 | Offline mode (full) | All CRUD operations, cached maps |
| 37-38 | Community feed | Opt-in sharing, nearby catches, "Catch of the Day" |
| 39-40 | Push notifications | Condition alerts, trip reminders |
| 41-42 | Performance optimization | Database indexing, caching, CDN tuning |
| 43-44 | Accessibility & polish | VoiceOver, dark mode, edge case fixes |
| 45-46 | Scale infrastructure | Move to AWS (if on Railway), load testing |
| 47-48 | Year-end marketing push | Holiday promo, annual subscription discount |

**Deliverables:**
- Full feature set live
- Community features launched
- 5,000+ active users
- $3,000 MRR
- Stable, scalable infrastructure

---

### Post-Launch (Year 2+)

**Priorities:**
1. **Mobile-first optimizations:** Improve species ID accuracy, faster sync, better offline UX
2. **Web app:** Dashboard for Pro users (desktop experience for deep analytics)
3. **Hardware integrations:** Bluetooth fish scale, smartwatch app (Apple Watch, Garmin)
4. **International expansion:** Translate app (Spanish, Portuguese), add species for international waters
5. **Partnerships:** Integrate with Garmin, Lowrance, Humminbird (marine electronics)
6. **Community growth:** Leaderboards, challenges, local fishing reports

---

## Risk Assessment

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Species ID accuracy below 80%** | Medium | High | Start with limited species set (top 50), use Google Vision API as fallback, continuous training |
| **API rate limits exceeded** (weather, geocoding) | Low | Medium | Aggressive caching (30 min weather, 24hr tides), request pooling, upgrade to paid tiers if needed |
| **S3 costs spiral** (many photos) | Low | Medium | Image compression (reduce to 1MB max), lazy loading, CloudFront caching, monitor usage |
| **Offline sync conflicts** | Medium | Low | Last-write-wins strategy, conflict resolution UI for rare cases, educate users |
| **Database performance degrades** (10k+ users) | Medium | High | Indexing, query optimization, read replicas, caching (Redis), sharding if needed |

---

### Product Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Low user adoption** (market too niche) | Medium | High | Start with kayak anglers (tight community, passionate), expand to all anglers, validate PMF with beta |
| **Low free-to-Pro conversion** (<10%) | Medium | High | Strong Pro value prop (predictions are killer feature), in-app messaging, limited-time offers |
| **Competitors copy features** (Fishbrain, Anglr) | High | Medium | Speed to market, superior AI, community, brand loyalty, continuous innovation |
| **Users don't trust AI** (species ID errors) | Low | Medium | Transparency (show confidence scores), easy corrections, feedback loop improves model |
| **Privacy concerns** (location tracking) | Low | Medium | Clear privacy policy, location opt-in, anonymization options, no data selling |

---

### Business Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Run out of funding** (9-12 month runway) | Low | Critical | Bootstrap (Jeff's savings), control costs (Railway < AWS for MVP), seek angel funding if traction |
| **Burnout** (solo developer) | Medium | High | Set sustainable pace (20 hrs/week), use curriculum structure for pacing, automate where possible |
| **Legal issues** (NOAA data use, privacy) | Low | High | Review NOAA ToS (public domain), GDPR compliance (EU users), consult lawyer for ToS/Privacy Policy |
| **Market timing** (economic downturn) | Medium | Low | Fishing is recession-resistant (low-cost hobby), freemium model accessible |

---

### Mitigation Summary
- **Start small:** Kayak anglers first, expand later
- **Validate early:** Beta test with real users before full launch
- **Build in public:** Share progress on Twitter/LinkedIn, get feedback
- **Control costs:** Use free tiers, optimize caching, monitor usage
- **Continuous improvement:** Monthly model retraining, weekly feature iterations
- **Focus on retention:** Core value (effortless logging) must be exceptional

---

## Appendices

### Appendix A: Competitor Feature Matrix

| Feature | Catchbook | Fishbrain | Anglr | FishAngler | MyFishingAdvisor |
|---------|-----------|-----------|-------|------------|------------------|
| Photo logging | ✅ AI auto-fill | ✅ Manual | ✅ Auto (hardware) | ✅ Manual | ❌ |
| Species ID (AI) | ✅ Custom model | ✅ Cloud API | ✅ Limited | ✅ Community-driven | ❌ |
| Equipment tracking | ✅ Full catalog | ❌ | ✅ Basic | ✅ Basic | ❌ |
| Predictions | ✅ ML-based | ❌ | ✅ Basic | ❌ | ✅ Solunar only |
| Offline mode | ✅ Full CRUD | ✅ Read-only | ✅ (hardware) | ❌ | ❌ |
| Social features | ✅ (Phase 3) | ✅ Strong | ❌ | ✅ Strong | ❌ |
| Free tier | ✅ Generous | ✅ Limited | ❌ Hardware cost | ✅ Ads-heavy | ✅ |
| Pro pricing | $4.99/mo | $4.99/mo | $9.99/mo | $9.99/mo | $4.99/mo |

---

### Appendix B: User Interview Findings

**Interviews Conducted:** 15 kayak anglers (10 in-person, 5 remote)

**Key Findings:**
1. **Pain Point Consensus:** 100% agree manual data entry is tedious
2. **Photo Habit:** 87% already take photos of notable catches
3. **Data Desired:** Top 5: Species, Location, Weather, Lure Used, Size
4. **Current Solutions:** 40% use analog journals, 33% use spreadsheets, 27% use existing apps (dissatisfied)
5. **Willingness to Pay:** 67% would pay $5/month for predictions + advanced analytics
6. **Most Requested Feature:** "Tell me when to go fishing" (predictive recommendations)
7. **Privacy Concern:** 20% worried about exact locations being public (solution: generalized sharing)

---

### Appendix C: Technical References

**AI/ML Resources:**
- [iNaturalist Fish Dataset](https://www.inaturalist.org/taxa/47178-Actinopterygii)
- [TensorFlow Transfer Learning Guide](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [MobileNetV2 Paper](https://arxiv.org/abs/1801.04381)

**External APIs:**
- [NOAA Tides & Currents API](https://api.tidesandcurrents.noaa.gov/api/prod/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding)

**Mobile Development:**
- [React Native Docs](https://reactnative.dev/docs/getting-started)
- [React Native Camera](https://github.com/react-native-camera/react-native-camera)
- [WatermelonDB (Offline)](https://github.com/Nozbe/WatermelonDB)

**Backend:**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PostgreSQL + PostGIS](https://postgis.net/)

---

### Appendix D: Glossary

- **EXIF:** Exchangeable Image File Format, metadata embedded in photos (GPS, timestamp, camera settings)
- **Solunar Period:** Times of day when fish are most active (based on moon/sun position)
- **Tide State:** Current phase of tide (high, low, incoming, outgoing)
- **Transfer Learning:** ML technique using pre-trained models as starting point for new tasks
- **MobileNetV2:** Efficient CNN architecture optimized for mobile devices
- **XGBoost:** Gradient boosting library for tabular data predictions
- **PostGIS:** PostgreSQL extension for geospatial data
- **CDN:** Content Delivery Network (fast global image serving)
- **Pre-signed URL:** Temporary URL for direct S3 upload/download without API proxy

---

### Appendix E: Contact & Feedback

**Project Owner:** Jeff Hutting  
**Email:** jeff@catchbook.app (placeholder)  
**GitHub:** github.com/jeff-hutting/catchbook (private repo)

**Feedback Channels:**
- In-app feedback button (links to email or form)
- Discord/Slack beta community
- Email: support@catchbook.app
- Twitter: @CatchbookApp

---

## Document Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-01 | Jeff Hutting | Initial comprehensive spec |

---

## Next Steps

1. **Review this spec with Advisor role** to align with curriculum phases
2. **Create GitHub project board** with issues for each milestone
3. **Begin Phase 1: Week 1-2** (Project setup, architecture decisions)
4. **Set up landing page** to collect beta signups
5. **Build social media presence** (Instagram, YouTube)

---

**End of Catchbook Product Specification Document**