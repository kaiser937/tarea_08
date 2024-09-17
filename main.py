from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    Prenda: str

@app.post("/")
async def create_item(item: Item):
    return {"Respuesta": f"Prenda agregada: {item.Prenda}"}