from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import fitz
from Identifier import AnalyzeFile


#load API key from .env
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPEN_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

#Test
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.normpath(os.path.join(current_dir, "..", "testdata", "docx1.docx"))
    text = AnalyzeFile(filepath)

#Prompt
PROMPT_TEMPLATE = """
You are an assistant for question-answering tasks.
User gave the following job certificate:

{context}

---

Answer the following questions:
1. What were the employees duties?
2. When did the work take place?
3. In what company did they work at?

Answer in a structured manner.
Use the given data to answer the question. If you don't know the answer, say you don't know.
Don't make up anything.
"""

prompt = PROMPT_TEMPLATE.format(context=text)
response = llm.invoke(prompt)

print(response.content)