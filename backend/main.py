from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import bedrock_api
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    response : str

@app.post("/input")
async def request(item: Item):
    feedback = bedrock_api.run_chatbot(item.response)
    return {"message": feedback}





