## Math tutor with LangChain
<p>This project implements a virtual math teacher using the LangChain library and the ChatGroq model to provide explanatory answers in portuguese to mathematical question with a simple validation.</p>

## Technologies
- Python: Main programming language used in the project.
- FastAPI: Modern and high-performance web framework for building APIs with Python.
- LangChain: Library for integration with language models, such as Groq LLAMA.
- Groq LLAMA: Model used to answer mathematical questions.
- dotenv: Library for loading environment variables from a .env file.
- Uvicorn: Fast ASGI server for running the FastAPI application.

## Main files 
- math_tutor.py (Contains the core logic for processing mathematical questions and returning answers in JSON format.)
- math_tutor_langserve.py (Similar to math_tutor.py, but configured to be used with LangServe)
- server_py (Implement the API using FastAPI and add routes to access the page for better viewing
- test_json.py (To verify tutor functionality via JSON input)

## Input Validation

The program checks if the question is related to mathematics through:

- Mathematical keywords in portuguese.

- Presence of mathematical symbols (+, -, *, /, ^, =).
  
If the question is not related to math, a warning will be returned that only questions related to mathematics are allowed and the question category will automatically be set to "others"

## Getting Started 
First, install the necessary dependencies:
```bash
pip install -r requirements.txt
```

# Usage examples

1. Testing the tutor running "test_json.py" (In the file there will be a question made especially to test the tutor, you can change it directly in the file)
   Example:
   ```bash
   entry_json = json.dumps({"question": "Solve the equation 2x+3=7"})
   ```
   Request example:
   ```bash
   {
    "question": "Solve the equation: 2x+3=7"
   }
   ```
   Output example:
   ```bash
   {
    "question": "Solve the equation: 2x+3=7",
    "category": "Mathematic",
    "answer": "The result of the 2x+3=7 is...:"
   }
   ```
   
2. Just run "server.py" and you will access localhost, more specifically via this route:
```bash
http://localhost:8000/math_tutor/playground/
```
On this page, you will be able to view an input to write the question and then receive a response from the tutor.

   

