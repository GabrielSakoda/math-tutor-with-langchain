from math_tutor_langserve import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="Math Tutor API", description="API for Math Tutor")

add_routes(app, chain, path="/math_tutor")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)