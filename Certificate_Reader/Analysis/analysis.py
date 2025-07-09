from langchain_openai import ChatOpenAi
import os
from dotenv import load_dotenv
import fitz


#load API key from .env
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPEN_API_KEY")

llm = ChatOpenAI(model"gpt-4o-mini", api_key=OPENAI_API_KEY)

def read_pdf(filename):
    with fitz.open(filename) as doc:
        return "\n".join([page.get_text() for page in doc]) 
    
    text = read_pdf("example.pdf")

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