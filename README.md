# U-HEAR: Voice-First AI SRHR Platform

**Tagline:** Your voice, your health, your points. 🎙️🛡️💰

---

## 🌟 Overview

U-HEAR is a **revolutionary voice-first platform** designed to provide **Sexual and Reproductive Health & Rights (SRHR) education and guidance** to **youth in low-connectivity regions**. It works on **feature phones, basic phones, and smartphones**, combining **voice, SMS, AI reasoning, gamification, and cloud analytics** to create a safe, inclusive, and engaging experience.

---

## 🎯 Core Problem

- **Low smartphone penetration** → Apps inaccessible  
- **Low literacy rates** → Text-based content unusable  
- **High data costs** → Toll-free voice preferred  
- **Cultural stigma** → Need private, anonymous interactions  
- **Limited internet** → Offline-first capabilities required  

---

## 💡 Solution

U-HEAR leverages:

- **Voice-first interactions** (Twilio, Amazon Connect)  
- **Speech-to-text processing** (Google STT / Amazon Transcribe)  
- **AI reasoning & emotion detection** (Amazon Bedrock, SageMaker LLMs)  
- **AgentCore** decision engine for scenario progression  
- **Gamified rewards** via **NovaPoints**  
- **Backend storage & analytics** (PostgreSQL, Redis, S3, Fivetran → Redshift/Snowflake)  
- **Elastic dashboards** for visualization & monitoring  

---

## 📱 User Access Tiers

1. **Tier 1 – Voice-only**  
   - Feature phones  
   - Toll-free number  
   - Interactive voice scenarios  
   - Anonymous & private  

2. **Tier 2 – SMS + Voice Hybrid**  
   - Basic phones  
   - Keywords & callbacks  
   - Scenario-based learning  
   - Points tracking via SMS  

3. **Tier 3 – Smartphone App**  
   - Offline voice commands  
   - Gamified scenario dashboard  
   - NovaPoints & rewards  
   - Local resource mapping  

---

## 🏗️ 7 Modular Apps

### 1️⃣ UserAccess
- Handles **voice calls & SMS input**  
- Routes user actions to AI reasoning  
- Tracks scenario points  

### 2️⃣ VoiceTextProcessor
- Converts voice → text  
- Normalizes user input  
- Optional offline caching  

### 3️⃣ NLP_SentimentAnalyzer
- Detects user **emotion & intent**  
- Maps to scenario choices  

### 4️⃣ AIReasoningAdvisory
- Provides AI-driven advice  
- Calculates **NovaPoints**  
- Scenario branching logic  

### 5️⃣ AgentCoreDecisionEngine
- Enforces scenario rules  
- Pauses risky actions  
- Progresses scenarios  

### 6️⃣ BackendStorage
- Stores **user points, history, audio**  
- PostgreSQL + Redis + S3  
- Audio & content caching  

### 7️⃣ AnalyticsDashboard
- Visualizes **leaderboards & metrics**  
- ETL via Fivetran → Redshift/Snowflake  
- Elastic / Kibana dashboards  

---

## ⚙️ Technology Stack

| Layer | Technology / Service |
|-------|--------------------|
| Voice & SMS | Twilio, Amazon Connect, Africa’s Talking |
| Speech-to-Text | Google STT, Amazon Transcribe |
| AI Reasoning | Amazon Bedrock LLM, Amazon SageMaker |
| AgentCore | Decision engine & scenario logic |
| Gamification | NovaPoints, Transform, Nova Act SDK |
| Backend | Flask / Node.js, PostgreSQL, Redis, AWS Lambda, API Gateway |
| Storage | Amazon S3 |
| Analytics | Fivetran → Redshift / Snowflake, Elastic, Kibana |
| DevOps | Docker, AWS EC2, CI/CD pipelines |

---

## 🛡️ Privacy & Safety

- Anonymous interactions, **no PII stored**  
- Emergency exit commands: `"wrong number"`  
- 24/7 counselor access: press `0`  
- Discreet system naming to prevent stigma  
- Cultural localization & age-appropriate content  

---

## 🎮 Gamification – NovaPoints

| Action | Points |
|--------|-------|
| Daily call | +5 |
| Scenario complete | +10-20 |
| Correct choice | +15 |
| Refer a friend | +25 |
| Weekly streak | +50 |

**Rewards:**
- 100 pts → Mobile data (50MB)  
- 250 pts → Menstrual hygiene kit  
- 500 pts → Clinic voucher  
- 1000 pts → SRHR Champion Badge  

---

## 📊 Architecture


```
U-HEAR/
├── 1_UserAccess/
│   ├── app/
│   │   ├── main.py            # Flask API for IVR/SMS/mobile app endpoints
│   │   ├── twilio_integration.py
│   │   ├── sms_gateway.py
│   │   └── ui/
│   │       ├── index.html
│   │       └── voice_ui.js
│   ├── requirements.txt
│   └── README.md
│
├── 2_VoiceTextProcessor/
│   ├── app/
│   │   ├── transcribe.py       # Google STT / Amazon Transcribe calls
│   │   ├── normalize.py        # Clean text & metadata
│   │   └── queue_manager.py    # Handles batch processing
│   ├── requirements.txt
│   └── README.md
│
├── 3_NLP_SentimentAnalyzer/
│   ├── app/
│   │   ├── nlp_model.py        # SageMaker/Nova Act NLP model stub
│   │   ├── sentiment.py        # Emotion detection
│   │   └── intent_mapping.py   # Scenario intent mapper
│   ├── requirements.txt
│   └── README.md
│
├── 4_AIReasoningAdvisory/
│   ├── app/
│   │   ├── reasoning.py        # LLM integration stub (Amazon Bedrock)
│   │   ├── scenario_logic.py   # Generates next scenario step
│   │   └── points_allocation.py # NovaPoints rules
│   ├── requirements.txt
│   └── README.md
│
├── 5_AgentCoreDecisionEngine/
│   ├── app/
│   │   ├── agentcore.py        # AgentCore primitive integration
│   │   ├── decision_tree.py    # Scenario branching
│   │   ├── risk_assessment.py  # Pause risky actions
│   │   └── notifications.py    # Push alerts / callbacks
│   ├── requirements.txt
│   └── README.md
│
├── 6_BackendStorage/
│   ├── app/
│   │   ├── api.py              # Lambda/API Gateway integration
│   │   ├── database.py         # PostgreSQL connection
│   │   ├── cache.py            # Redis cache
│   │   ├── s3_storage.py       # Audio & content storage
│   │   └── transform.py        # Format data for analytics
│   ├── requirements.txt
│   └── README.md
│
├── 7_AnalyticsDashboard/
│   ├── app/
│   │   ├── dashboard.py        # Flask/React dashboard backend
│   │   ├── elastic_search.py   # Elastic/Kibana integration
│   │   ├── fivetran_etl.py     # Fivetran -> Redshift/Snowflake ETL
│   │   └── leaderboard.py      # NovaPoints leaderboard logic
│   ├── requirements.txt
│   └── README.md
│
└── README.md                   # Project-level documentation
```

---

## 🏗️ Functionality Breakdown

### 1️⃣ UserAccess
- Handles **voice calls, SMS, and mobile app inputs**  
- Routes inputs to **AI reasoning & AgentCore**  
- Tracks **NovaPoints**  
- **Front-end UI** for web/mobile preview  

### 2️⃣ VoiceTextProcessor
- Converts **voice → text** using **Google STT / Amazon Transcribe**  
- Normalizes and cleans user inputs  
- Handles **batch queueing for async processing**  

### 3️⃣ NLP_SentimentAnalyzer
- **Detects user emotion & intent**  
- Maps input to **scenario actions**  
- Supports **Liberian English NLP models** via SageMaker / Nova Act  

### 4️⃣ AIReasoningAdvisory
- Integrates **LLMs (Amazon Bedrock)** for scenario reasoning  
- Determines **next scenario steps**  
- Allocates **NovaPoints** based on choices  

### 5️⃣ AgentCoreDecisionEngine
- Implements **AgentCore primitives** for autonomous decision-making  
- **Scenario branching & risk assessment**  
- Sends **notifications & alerts**  

### 6️⃣ BackendStorage
- Connects to **PostgreSQL** for user data  
- Uses **Redis** for caching sessions  
- Stores **audio & content in S3**  
- Formats data for analytics (Transform)  

### 7️⃣ AnalyticsDashboard
- **Visualizes leaderboards & engagement metrics**  
- ETL pipelines via **Fivetran → Redshift / Snowflake**  
- Dashboard search & visualization with **Elastic / Kibana**  

---

## ⚙️ Technology Stack

| Layer | Service / Technology |
|-------|--------------------|
| Voice & SMS | Twilio, Amazon Connect, Africa’s Talking |
| Speech-to-Text | Google STT, Amazon Transcribe |
| AI & NLP | Amazon Bedrock LLM, SageMaker, Nova Act |
| Agent Engine | AgentCore |
| Gamification | NovaPoints, Transform |
| Backend | Flask / Node.js, Lambda, API Gateway |
| Storage | PostgreSQL, Redis, Amazon S3 |
| Analytics | Fivetran → Redshift / Snowflake, Elastic / Kibana |
| DevOps | Docker, AWS EC2, CI/CD pipelines |

---

## 🚀 Setup Instructions

1. **Clone Repo**
```bash
git clone https://github.com/username/u-hear.git
cd U-HEAR
```
### 2. Install Dependencies for Each Module

Each module has its own `requirements.txt`. Install dependencies separately for isolation and easier debugging.

#### 1_UserAccess
```bash
cd U-HEAR/1_UserAccess/
pip install -r requirements.txt
```
### 3. Configure AWS Credentials

- **IAM Roles**  
  Create and assign IAM roles for:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon S3
  - Amazon SageMaker

- **API Gateway**  
  - Set up endpoints for:
    - Voice input (Twilio/Amazon Connect integration)
    - SMS gateway

---

### 4. Database Setup

- **PostgreSQL**  
  Initialize the database schema with tables such as:
  - `users`
  - `points_history`
  - `scenarios`

- **Redis Cache**  
  - Configure Redis for session data caching
  - Ensure fast retrieval of user states and scenario progress

---

### 5. Run Development Server

- **For Flask/Backend Modules:**  
  Navigate to each module folder and run:

  ```bash
  cd 1_UserAccess/app
  python main.py
