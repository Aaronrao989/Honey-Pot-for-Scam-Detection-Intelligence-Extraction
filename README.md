<div align="center">

# 🛡️ Agentic Honey-Pot
### AI-Powered Scam Detection & Intelligence Extraction System

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq%20AI-orange.svg)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Built for GUVI – HCL India AI Impact Buildathon** 🏆

[Features](#-key-features) • [Architecture](#-system-architecture) • [Setup](#️-quick-start) • [API Docs](#-api-documentation) • [Deployment](#-deployment)

</div>

---

## 🎯 Mission Statement

An **intelligent, stateful honeypot API** that doesn't just detect scams—it engages scammers in realistic multi-turn conversations, extracts actionable intelligence (UPI IDs, phishing links, phone numbers, bank accounts), and reports findings to the GUVI evaluation endpoint.

> **Think of it as:** A digital undercover agent that thinks, adapts, and learns from scammers in real-time.

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🎭 **Realistic Human Persona**
- Behaves like a genuine Indian user
- Natural question patterns
- Emotional responses (confused, scared, obedient)
- Multi-turn contextual awareness

</td>
<td width="50%">

### 🧠 **Intelligent Detection**
- Real-time scam pattern recognition
- Adaptive conversation strategies
- Context-aware response generation
- Session-based memory management

</td>
</tr>
<tr>
<td width="50%">

### 🔍 **Intelligence Extraction**
- UPI IDs & Bank Accounts
- Phishing URLs & Domains
- Phone Numbers
- Suspicious Keywords
- Automated pattern matching

</td>
<td width="50%">

### 📡 **Automated Reporting**
- GUVI callback integration
- Structured intelligence reports
- Engagement metrics tracking
- Production-ready API

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Incoming Message                          │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
                    ┌────────────────┐
                    │ Scam Detector  │ ← AI-powered analysis
                    └────────┬───────┘
                             ↓
                    ┌────────────────┐
                    │Strategy Engine │ ← Adaptive tactics
                    └────────┬───────┘
                             ↓
                    ┌────────────────┐
                    │  Agent Brain   │ ← Groq LLM Persona
                    │  (Llama-3 70B) │
                    └────────┬───────┘
                             ↓
                    ┌────────────────┐
                    │  Memory Store  │ ← Session context
                    └────────┬───────┘
                             ↓
                    ┌────────────────┐
                    │   Intelligence │ ← Regex extraction
                    │    Extractor   │
                    └────────┬───────┘
                             ↓
                    ┌────────────────┐
                    │ GUVI Callback  │ ← Automated reporting
                    └────────┬───────┘
                             ↓
              ┌──────────────────────────┐
              │ Structured JSON Response │
              └──────────────────────────┘
```

> **This is a stateful agentic system, not just a scam classifier.**

---

## 📂 Project Structure

```
honeypot-ai/
│
├── 📁 app/
│   ├── 📁 api/
│   │   └── routes.py              # API endpoints
│   ├── 📁 core/
│   │   ├── scam_detector.py       # Scam detection logic
│   │   ├── agent_brain.py         # LLM persona engine
│   │   ├── strategy_engine.py     # Adaptive strategies
│   │   ├── memory_store.py        # Session management
│   │   └── intelligence_extractor.py  # Data extraction
│   ├── 📁 services/
│   │   ├── conversation_manager.py     # Conversation flow
│   │   └── guvi_callback.py            # Reporting service
│   ├── 📁 models/
│   │   └── schemas.py             # Pydantic models
│   ├── 📁 utils/
│   │   └── regex_patterns.py      # Pattern matching
│   ├── config.py                  # Configuration
│   └── main.py                    # Application entry
│
├── requirements.txt
├── .env                           # Environment variables
├── start.sh                       # Startup script
└── README.md
```

---

## ⚡️ Quick Start

### **1️⃣ Clone Repository**

```bash
git clone <your-repo-url>
cd honeypot-ai
```

### **2️⃣ Create Virtual Environment**

```bash
python -m venv .venv

# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Environment**

Create a `.env` file in the root directory:

```env
API_KEY=your_api_key_for_guvi
GROQ_API_KEY=your_groq_key_here
MODEL_NAME=llama3-70b-8192
```

### **5️⃣ Launch Server**

```bash
uvicorn app.main:app --reload
```

🎉 **Success!** Navigate to: [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)

---

## 📚 API Documentation

### 🔐 **Authentication**

All requests require authentication header:

```http
x-api-key: <your_API_KEY_from_.env>
```

---

### 📥 **POST** `/honeypot`

**Description:** Process incoming messages and engage scammers

#### **Request Schema**

```json
{
  "sessionId": "test-session-1",
  "message": {
    "sender": "scammer",
    "text": "Verify now at http://fake-bank.com and share your UPI ID",
    "timestamp": "2026-01-21T10:15:30Z"
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}
```

#### **Response Schema**

```json
{
  "status": "success",
  "scamDetected": true,
  "engagementMetrics": {
    "engagementDurationSeconds": 40,
    "totalMessagesExchanged": 4
  },
  "extractedIntelligence": {
    "bankAccounts": [],
    "upiIds": ["scammer@upi"],
    "phishingLinks": ["http://fake-bank.com"],
    "phoneNumbers": [],
    "suspiciousKeywords": ["verify now"]
  },
  "agentNotes": "Scam intent detected | Strategy used: obedient"
}
```

---

## 🤖 Agent Behavior

Powered by **Llama-3 70B** via Groq API, the agent:

| Capability | Description |
|------------|-------------|
| 🎭 **Persona Simulation** | Mimics a typical Indian user with realistic responses |
| 💬 **Natural Dialogue** | Asks contextually relevant questions |
| 😰 **Emotional States** | Displays confusion, fear, or compliance |
| 🕵️ **Covert Extraction** | Gathers intelligence without revealing detection |
| 🧠 **Context Retention** | Maintains multi-turn conversation memory |

---

## 🔍 Intelligence Extraction

Regex-powered extraction targeting:

| Type | Examples | Pattern Matching |
|------|----------|------------------|
| 💳 **UPI IDs** | `user@paytm`, `9876543210@ybl` | Email-like patterns |
| 🏦 **Bank Accounts** | `1234567890` (10-18 digits) | Numeric sequences |
| 📱 **Phone Numbers** | `+91-9876543210`, `9876543210` | Indian mobile formats |
| 🔗 **Phishing Links** | `http://fake-bank.com` | URL patterns |
| ⚠️ **Suspicious Keywords** | `verify`, `urgent`, `account blocked` | Keyword database |

---

## 🧠 Memory System

**Session-based in-memory architecture:**

- ✅ Tracks complete conversation history
- ✅ Monitors extracted intelligence
- ✅ Records engagement metrics
- ✅ Prevents duplicate extractions
- ✅ Controls callback lifecycle

---

## 📡 GUVI Integration

**Automated reporting to evaluation endpoint:**

```http
POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult
```

**Trigger Conditions:**
- ✓ Sufficient engagement duration
- ✓ Intelligence successfully extracted
- ✓ Conversation naturally concluded

> ⚠️ **Required for evaluation scoring**

---

## 🌐 Deployment

### **Render Deployment**

**Start Command:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

**Environment Variables:**
Configure in Render dashboard:
- `API_KEY`
- `GROQ_API_KEY`
- `MODEL_NAME`

**Public Endpoint:**
```
https://your-app.onrender.com/honeypot
```

---

## 🧪 Testing Guide

### **Postman Configuration**

| Setting | Value |
|---------|-------|
| **Method** | `POST` |
| **URL** | `http://127.0.0.1:8000/honeypot` |
| **Headers** | `x-api-key: <your_key>` |
| | `Content-Type: application/json` |
| **Body** | Use sample request from [API Docs](#-api-documentation) |

---

## ✅ Evaluation Checklist

- [ ] 🎯 High scam detection accuracy
- [ ] 💬 Effective multi-turn engagement
- [ ] 🔍 Comprehensive intelligence extraction
- [ ] 📋 Correct JSON response format
- [ ] 📡 Successful GUVI callback
- [ ] 🌐 Stable public endpoint
- [ ] ⚡ Low latency (<3s response time)
- [ ] 🛡️ Robust error handling

---

## 🎓 Technology Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Backend** | FastAPI, Python 3.9+ |
| **AI Engine** | Groq (Llama-3 70B) |
| **Data Processing** | Regex, Pydantic |
| **Deployment** | Render, Uvicorn |
| **Testing** | Postman, Pytest |

</div>

---

## 🏆 Project Highlights

This project demonstrates:

✨ **Agentic AI System Design** – Autonomous decision-making and adaptive behavior  
✨ **Stateful Conversation Handling** – Multi-turn context retention  
✨ **Real-time Intelligence Extraction** – Pattern recognition and data mining  
✨ **Ethical Scam Engagement** – Responsible honeypot methodology  
✨ **Production-Grade Architecture** – Scalable, maintainable, and testable

---

<div align="center">

### 🚀 Designed to Meet and Exceed Agentic Honey-Pot Challenge Expectations

**Built with ❤️ for GUVI – HCL India AI Impact Buildathon**

---

[![GitHub Stars](https://img.shields.io/github/stars/yourusername/honeypot-ai?style=social)](https://github.com/yourusername/honeypot-ai)
[![GitHub Forks](https://img.shields.io/github/forks/yourusername/honeypot-ai?style=social)](https://github.com/yourusername/honeypot-ai)

[Report Bug](https://github.com/yourusername/honeypot-ai/issues) • [Request Feature](https://github.com/yourusername/honeypot-ai/issues) • [Documentation](https://github.com/yourusername/honeypot-ai/wiki)

</div>