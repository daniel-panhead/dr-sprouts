from fastapi import FastAPI
import bedrock_api
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    response : str

@app.post("/input")
async def request(item: Item):
    feedback = bedrock_api.run_chatbot(item.response)
    return {"message": feedback}





