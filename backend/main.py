from fastapi import FastAPI
import titan

text = titan.response

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

print(text)