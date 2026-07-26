# 🤖 AI Portfolio Assistant

An AI-powered Resume Assistant that parses a resume into structured data using an LLM and allows recruiters to interact with it through natural language.

Instead of searching a resume manually, recruiters can ask questions like:

- "What are Kumar's skills?"
- "Tell me about his education."
- "Describe the FinSight project."
- "Show me his GitHub profile."
- "Does he have any certifications?"

The assistant uses **LLM Function Calling** to decide when to search the parsed resume or retrieve portfolio links.

---

## 🚀 Features

- 📄 Read PDF and DOCX resumes
- 🧠 Parse resumes into structured JSON using an LLM
- ✅ Validate extracted data with Pydantic
- 🔍 Search resume information using Python (no repeated LLM calls)
- 🔗 Retrieve GitHub, LinkedIn, Portfolio, and Project links
- 🤖 LLM Function Calling (Tool Calling)
- 💬 Interactive chatbot interface
- 🛡️ Prevents hallucinations by answering only from parsed data

---

## 🛠️ Tech Stack

- Python 3.11+
- Groq API
- GPT-OSS-120B
- Pydantic
- PyPDF
- python-docx
- python-dotenv

---

## 📂 Project Structure

```
AI-Portfolio-Assistant/
│
├── resume/
│   └── kumargaurav.pdf
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🏗️ Architecture

```
                Resume (PDF / DOCX)
                        │
                        ▼
              Resume Reader (PyPDF)
                        │
                        ▼
                  Raw Resume Text
                        │
                        ▼
                LLM Resume Parser
                        │
                        ▼
             Structured Resume (Pydantic)
                        │
      ┌─────────────────┴──────────────────┐
      ▼                                    ▼
search_resume()                     get_link()
      │                                    │
      └──────────────┬─────────────────────┘
                     ▼
             LLM Function Calling
                     │
                     ▼
            AI Portfolio Assistant
```

---

## 📋 Resume Schema

The resume is converted into a structured format using **Pydantic**.

```python
Resume
│
├── name
├── summary
├── contact
│   ├── email
│   └── phone
├── skills
├── education
├── experience
├── projects
└── certifications
```

---

## 🔧 Available Tools

### search_resume(query)

Searches structured resume information including:

- Skills
- Education
- Experience
- Projects
- Contact Information
- Certifications

Example:

```
User:
What technologies does Kumar know?
```

```
Tool:
search_resume("technologies")
```

---

### get_link(query)

Returns useful portfolio links.

Supports:

- GitHub
- LinkedIn
- Portfolio
- Live Demo
- Project Repository

Example:

```
User:
Show me the GitHub repository for FinSight.
```

```
Tool:
get_link("finsight github")
```

---

## 🧠 How It Works

### Step 1

Read the resume.

```
PDF
   │
   ▼
Raw Text
```

---

### Step 2

Parse the resume using GPT-OSS-120B.

```
Raw Text
      │
      ▼
Structured Resume
```

---

### Step 3

Store the parsed resume as a Pydantic object.

```
Resume Object
```

---

### Step 4

The LLM decides whether a tool is needed.

```
User Question
        │
        ▼
       LLM
        │
        ▼
Tool Selection
```

---

### Step 5

Execute the appropriate Python tool.

```
search_resume()

or

get_link()
```

---

### Step 6

The tool result is sent back to the LLM to generate the final response.

```
Tool Result
      │
      ▼
LLM
      │
      ▼
Final Answer
```

---

## 💬 Example Questions

```
What are Kumar's skills?

Tell me about his education.

Describe the FinSight project.

Show me his portfolio.

Give me his LinkedIn profile.

Does Kumar have any certifications?

What technologies does he know?

What is his phone number?
```

---

## ▶️ Installation

Clone the repository.

```bash
git clone https://github.com/Kumar24Gaurav/AI-Portfolio-Assistant.git
```

Move into the project directory.

```bash
cd AI-Portfolio-Assistant
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key_here
```

Run the project.

```bash
python main.py
```

---

## 📌 Future Improvements

- React Frontend
- Persistent resume JSON cache
- Multi-resume support
- Semantic search using embeddings
- Conversation memory
- Voice interaction
- Resume upload through UI

---

## 🎯 Learning Outcomes

This project demonstrates:

- LLM Function Calling
- AI Agent Workflow
- Resume Parsing with LLMs
- Structured Outputs
- Pydantic Data Validation
- Prompt Engineering
- Tool Calling
- Python Application Architecture

---

## 👨‍💻 Author

**Kumar Gaurav**

- GitHub: https://github.com/Kumar24Gaurav
- LinkedIn: https://www.linkedin.com/in/kumar-gaurav-814a58299
- Portfolio: https://kumargaurav-portfolio.vercel.app
