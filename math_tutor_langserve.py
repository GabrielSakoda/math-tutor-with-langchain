from dotenv import load_dotenv
import os
import re
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initializes the Groq LLaMA model
model = ChatGroq(model="llama3-8b-8192")
parser = StrOutputParser()

# Virtual teacher template
template_message = ChatPromptTemplate.from_messages([
    ("system", "Solve the following mathematical question in a clear and explanatory way, returning in PT-BR"),
    ("human", "{question}"),
])

# List of keywords and mathematical symbols for validation
math_keywords = [
    "soma", "subtração", "multiplicação", "divisão", "derivada", "integral",
    "equação", "álgebra", "geometria", "cálculo", "logaritmo", "matriz",
    "determinante", "trigonometria", "raiz quadrada", "potência", "fatoração",
    "número primo"
]
math_symbols = r"[\d\+\-\*/\^=()]"

# Input validation function
def is_math_question(question: str) -> bool:
    # Checks whether the question contains mathematical terms or symbols
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in math_keywords) or bool(re.search(math_symbols, question))

# Function for processing mathematical questions
def virtual_math_teacher(question: str) -> str:
    # If the question is related to mathematics, send it to the model
    if not is_math_question(question):
        return "Desculpe, só posso responder perguntas relacionadas à matemática."
        
    # Send to the model
    chain = template_message | model | parser
    response = chain.invoke({"question": question})
    return response


# Creating chain for langserve
chain = RunnableLambda(virtual_math_teacher)