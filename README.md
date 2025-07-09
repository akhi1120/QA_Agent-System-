# QA_Agent-System-
# 🤖 QA Agent Task – Automated Test Generation from YouTube Videos

Automatically generates **Playwright test cases** from **YouTube video transcripts** using **AI (OpenAI / Hugging Face / Ollama)** and runs browser automation to validate app functionality.

---

## 🚀 Features

- 🎥 Extracts transcripts from YouTube videos automatically  
- 🧠 Generates structured test cases using AI (OpenAI or local models)  
- 🧪 Converts steps into executable Playwright test scripts  
- 🖥️ Executes browser-based automated tests and verifies expected results  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/your-username/QAAgent-Task-YourName.git
cd QAAgent-Task-YourName

📦 Python (for backend)
pip install -r requirements.txt

🌐 Node.js (for Playwright)
npm install @playwright/test

Set up environment variables
OPENAI_API_KEY=your_openai_key_here

# Step 1: Extract transcript from YouTube
python data_ingestion.py

# Step 2: Generate test cases using AI
python generate_test_cases.py

# Step 3: Convert test cases to Playwright code
python convert_to_playwright.py

# Step 4: Run tests using Playwright
npx playwright test

QA_Agent_Task/
├── tests/                     # ✅ Generated Playwright test scripts
├── data_ingestion.py          # 🎥 Pulls transcript from YouTube video
├── generate_test_cases.py     # 🧠 AI generates test cases (OpenAI/HF)
├── convert_to_playwright.py   # 🔁 Converts steps to Playwright code
├── test_cases.json            # 📄 Output test cases from AI
├── transcript.txt             # 📄 Raw video transcript
├── .env                       # 🔐 OpenAI API key
└── README.md                  # 📘 Project guide

