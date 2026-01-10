# 🚀 AI Marketing Automation System (CrewAI)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![LiteLLM](https://img.shields.io/badge/LiteLLM-LLM%20Proxy-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

An **AI-powered marketing automation platform** that uses **CrewAI multi-agent collaboration** to generate **end-to-end marketing assets** such as strategies, content calendars, social media posts, blogs, and reel ideas through an interactive **Streamlit web interface**.

---

## 🚀 Project Overview

Marketing planning and content creation are time-consuming and repetitive tasks.  
This project provides a **fully automated AI-driven solution** that enables users to input basic product details and instantly receive **professionally structured marketing assets**.

The system is designed to be:

- ✅ Intelligent  
- ✅ Scalable  
- ✅ Production-ready  
- ✅ Docker & Cloud ready  

---

## 🧠 Key Features

- 🤖 Multi-agent collaboration using **CrewAI**
- 📊 Automated marketing strategy generation
- 🗓 Content calendar planning
- 📱 Social media post drafts
- 📝 Blog research & drafting
- 🎥 Short-form video / reel ideas
- 📂 Downloadable `.md` marketing assets
- 🛑 Prevents accidental re-runs & token waste
- 🐳 Fully Dockerized with proxy-safe LLM setup

---

## 🏗️ Tech Stack

Layer | Technology 
-----|-----------
 Programming Language | Python 3.11 
 Multi-Agent Framework | CrewAI 
 LLM Orchestration | LiteLLM 
 Frontend UI | Streamlit 
 Search & Tools | Tavily, Web Scraping 
 Containerization | Docker 
 Deployment | Docker Hub, Cloud Ready 

---

## 📂 Project Structure

```text
crewai-marketing-app/
│
├── app.py                     # Streamlit frontend
├── marketing_crew.py          # CrewAI agents & tasks
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── resources/
│   └── drafts/
│       ├── strategy.md
│       ├── calendar.md
│       ├── posts/
│       ├── blogs/
│       └── reels/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── screenshots/
│   ├── home.png
│   └── output.png
└── README.md
```

## 🔄 Application Workflow

1. User enters product details (name, description, audience, budget)
2. Clicks Run Crew
3. CrewAI orchestrates multiple specialized agents
4. Agents collaborate using LLM reasoning
5. Marketing assets are generated and saved as .md files
6. User downloads assets directly from the UI

## 🖥️ Application Screenshots
🔹 Product Input & Dashboard
🔹 Generated Marketing Assets

## ⚙️ Run Locally (Without Docker)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Run Using Docker

##Build Image
```bash
docker build -t crewai-marketing-app .
```

## Run Container
```bash
docker run -p 8501:8501 crewai-marketing-app
```

## 🌐 Access Application
- Streamlit UI → http://localhost:8501

## 🐳 Docker Image
The application is available as a pre-built Docker image on Docker Hub.

👉 Docker Hub Repository:
https://hub.docker.com/r/aravindvojjala/crewai-marketing-app

## Pull Image
```bash
docker pull aravindvojjala/crewai-marketing-app
```
## Run Image
```bash
docker run -p 8501:8501 aravindvojjala/crewai-marketing-app
```

## Stop Container
```bash
docker ps
docker stop <container_id>
```
