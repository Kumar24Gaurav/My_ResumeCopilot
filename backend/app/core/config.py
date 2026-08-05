import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

env_path = Path(__file__).parent.parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError ("api error")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"