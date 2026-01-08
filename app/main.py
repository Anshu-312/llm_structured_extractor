import json
import traceback
from fastapi import FastAPI, HTTPException
from app.schemas.models import TicketExtraction
from app.services.llm_client import extract_ticket_fields

app = FastAPI(title="Ticket Field Extraction API")

@app.post("/extract_fields", response_model=TicketExtraction)
async def extract_fields(text: str):
    try:
        raw = extract_ticket_fields(text)
        parsed = json.loads(raw)
        return TicketExtraction(**parsed)
    
    except Exception as e:
        #No silent failures
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="str(e)")
    
@app.get("/")
async def root():
    return {"Ticket Field Extraction API is operational."}