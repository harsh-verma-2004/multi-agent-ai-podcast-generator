🎙️ AI Podcast Generator (CrewAI + Hugging Face + FastAPI)

An end-to-end AI-powered podcast generation system that takes a topic as input, performs autonomous research using multiple AI agents, writes a structured podcast script, and generates spoken audio — all fully automated.

Built using CrewAI multi-agent orchestration, Hugging Face LLaMA models, FastAPI, and local Text-to-Speech (TTS).

🚀 Key Features

🔁 Multi-Agent AI Workflow (CrewAI)

Research Agent → Analysis Agent → Script Writer Agent

🧠 LLM-powered content generation using Hugging Face (LLaMA-3-8B-Instruct)

📝 Automatically generates:

Research summary

Detailed report

Podcast script with speaker dialogue

🔊 Audio podcast generation using local TTS (pyttsx3)

🌐 FastAPI backend to generate podcasts via API request

💯 Fully free & open-source stack (no paid API required)

🏗️ System Architecture
User Topic
   ↓
Research Agent (LLM)
   ↓
Reporting Agent (LLM)
   ↓
Scriptwriter Agent (LLM)
   ↓
Text-to-Speech Tool (Local)
   ↓
Podcast Audio (.wav)

🛠️ Tech Stack

Python 3.10+

CrewAI – Multi-agent orchestration

Hugging Face (LLaMA-3-8B-Instruct) – LLM inference

FastAPI – API layer

pyttsx3 – Offline text-to-speech

Uvicorn – ASGI server

📂 Project Structure
podcaster_crew-production/
│
├── src/
│   └── podcaster/
│       ├── crew.py
│       ├── main.py
│       ├── tools/
│       │   └── custom_tool.py
│       └── config/
│           ├── agents.yaml
│           └── tasks.yaml
│
├── api.py                # FastAPI entry point
├── requirements.txt
├── README.md
├── .gitignore
└── outputs/              # Generated scripts & audio (gitignored)

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/<your-username>/ai-podcast-generator-crewai.git
cd ai-podcast-generator-crewai

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Environment variables

Create a .env file in root (⚠️ do NOT commit this):

HUGGINGFACE_API_KEY=your_hf_key_here
SERPER_API_KEY=your_serper_key_here


🔐 .env is ignored via .gitignore

▶️ Running the Project (CLI)
python src/podcaster/main.py


This will:

Research the topic

Generate report & script

Create podcast audio in outputs/

🌐 Running via FastAPI
Start API server:
uvicorn api:app --reload

Open browser:
http://127.0.0.1:8000/docs

API Endpoint
POST /generate-podcast


Request Body

{
  "topic": "Future of Cybersecurity"
}


Response

{
  "message": "Podcast generated successfully",
  "audio_file": "outputs/podcast-20260203-154200.wav"
}

🎧 Output

📄 Research summary

📄 Podcast script

🔊 Audio podcast (.wav)

All stored inside the outputs/ directory.

🧠 Engineering Challenges Solved

Handled LLM context-length limits

Managed tool failures and retries

Implemented local TTS fallback to avoid paid APIs

Designed agent coordination without infinite loops

Secured secrets using .env & .gitignore

📌 Resume Description (Short)

Built an AI-driven podcast generation system using CrewAI multi-agent architecture and Hugging Face LLMs, automating research, scriptwriting, and audio generation via FastAPI.

🧪 Future Enhancements

Streaming audio generation

Topic scheduling & history

Cloud TTS integration

Frontend UI (React)

👨‍💻 Author

Harsh Verma
Computer Science Graduate
AI | Backend | Multi-Agent Systems

⭐ If you like this project

Give it a ⭐ on GitHub — it really helps!
