from openrouter import OpenRouter
from app.core.config import settings
from app.utils.prompts import SYSTEM_PROMPT

client = OpenRouter(api_key=settings.openrouter_api_key)
base_url= settings.openrouter_base_url



def extract_ticket_fields(text: str) -> str:
    response = client.chat.send(
        model=settings.openrouter_model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=0,
        max_tokens= 200,
    )

    return response.choices[0].message.content
