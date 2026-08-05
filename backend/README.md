# 🤖 AI Portfolio Assistant

This README documents the current behavior of [backend/portfolioCopilot.py](backend/portfolioCopilot.py) as a single-file Python prototype for an AI-powered portfolio assistant.

The script reads a resume, extracts structured information with an LLM, stores that information in Pydantic models, and then allows a recruiter-style chat loop to answer natural-language questions using two Python tools.

## ⚙️ What the script does

At runtime, the file performs the following sequence:

1. Loads environment variables from `.env`.
2. Reads the Groq API key from `GROQ_API_KEY`.
3. Initializes the Groq client and selects the model `openai/gpt-oss-120b`.
4. Loads a resume from the `resume/` directory.
5. Reads either a PDF or DOCX file into plain text.
6. Sends the raw resume text to the LLM with a strict JSON schema.
7. Parses the response into a validated `Resume` object using Pydantic.
8. Exposes two callable tools:
   - `search_resume(query)`
   - `get_link(query)`
9. Runs a terminal chat loop using `chat_with_resume()`.

## 🔄 Current execution flow

```text
Resume file (PDF or DOCX)
        |
        v
read_resume() -> read_pdf() / read_docx()
        |
        v
Raw text
        |
        v
extract_resume()
        |
        v
Structured Pydantic resume object
        |
        v
search_resume() and get_link()
        |
        v
LLM tool-calling conversation
```

## 📁 File responsibilities

### 📄 Resume ingestion

The script only accepts `.pdf` and `.docx` files.

- PDF support is handled by `pypdf`.
- DOCX support is handled by `python-docx`.

The parser builds a text blob from:

- PDF page text
- DOCX paragraphs
- DOCX table cell content

### 🧠 Structured extraction

The parsed resume is converted into a strongly typed schema through Pydantic models:

- `Contact`
- `Education`
- `Experience`
- `Project`
- `Resume`

The final structured shape contains:

- `name`
- `summary`
- `contact`
- `skills`
- `education`
- `experience`
- `projects`
- `certifications`

### 🔎 Tool-based querying

#### 🔍 `search_resume(query)`

This function searches the parsed resume object by topic. It is intended to answer questions related to:

- skills
- education
- experience
- projects
- contact details
- certifications
- summary

#### 🔗 `get_link(query)`

This function looks up portfolio-related URLs stored in the `METADATA` dictionary. It can return:

- portfolio URL
- GitHub profile
- LinkedIn profile
- project live links
- project repository links

## 💬 Chat loop behavior

The `chat_with_resume()` function starts an interactive terminal session.

The system prompt tells the assistant to:

- answer only questions about the person in the resume
- use tools when needed
- never invent facts
- answer concise and professionally
- return a short summary when the user asks for profile information

The chat loop:

1. receives a user question
2. sends it to the model with the available tools
3. decides whether a tool call is needed
4. runs `search_resume()` or `get_link()` if required
5. sends the tool result back into the conversation
6. returns the final answer

## ❓ Example user questions

The current assistant is designed to support questions like:

- "What are Kumar's skills?"
- "Tell me about his education."
- "Describe his projects."
- "Show me his GitHub profile."
- "Does he have certifications?"
- "Give me a professional summary."

## 🚀 Environment and execution

The script expects:

- a valid Groq API key in the environment
- a resume file available in the local `resume/` folder
- the Python dependencies installed in the backend environment

Run it with:

```bash
python portfolioCopilot.py
```

## ⚠️ Current prototype limitations

This file is best understood as a proof of concept rather than a production-ready service. The main limitations are:

- everything is concentrated in one script
- the resume path is hard-coded
- the runtime interface is terminal-based
- the assistant depends on the LLM to choose the correct tool call

## 🛠️ Refactoring direction

The next clean-up step would be to split the script into a clearer service structure, such as:

- resume readers
- parser and schema layer
- tool service layer
- chat orchestration
- API or frontend-facing integration

