import json
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

# Initializes the Groq LLAMA model
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
    # Checks whether the question contains mathematical terms or symbols.
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in math_keywords) or bool(re.search(math_symbols, question))

# Function to process math questions and return JSON
def virtual_math_teacher(request_json: str) -> str:
    # Processes the received mathematical question in JSON format, validates whether it is a math question and returns the answer in JSON.
    try:
        # Decodes received JSON
        request_data = json.loads(request_json)
        question = request_data.get("pergunta", "").strip()

        if not question:
            return json.dumps({"erro": "A pergunta não pode estar vazia."})

        # Determine the category of the question
        if is_math_question(question):
            category = "Matemática"
            # Send to model
            chain = template_message | model | parser
            response = chain.invoke({"question": question})
        else:
            category = "Outros"
            response = "Desculpe, só posso responder perguntas relacionadas à matemática."

        return json.dumps({
            "pergunta": question,
            "categoria": category,
            "resposta": response
        }, ensure_ascii=False)

    except json.JSONDecodeError:
        return json.dumps({"erro": "Formato de JSON inválido."})
