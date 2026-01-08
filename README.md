# llm_structured_extractor

Extract structured ticket fields from free-form text using an LLM (via OpenRouter) with strict schema enforcement.

**Why this exists**

Many LLM outputs are free-form and hard to consume downstream. This project demonstrates a minimal, safe pattern for extracting a fixed JSON schema from text by combining a strict system prompt with a small FastAPI wrapper and the OpenRouter SDK.

**Highlights**

- Minimal FastAPI service that returns a typed `TicketExtraction` model.
- Strict system prompt that forces the model to output only the required fields as JSON.
- Uses `openrouter` SDK for model access; environment-driven configuration.

**Features**

- Extracts: `name`, `order_id`, `issue_type`, and `phone`.
- Returns `null` for missing values and never invents fields.
- Low-entropy (temperature=0) requests to minimize hallucination.

**Quickstart**

Prerequisites: Python 3.10+, an OpenRouter API key, and an OpenRouter model/base URL.

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Set environment variables (example `.env`):

```
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=your_model_here
OPENROUTER_BASE_URL=https://api.openrouter.ai
DEBUG=true
```

3. Run the API:

```bash
uvicorn app.main:app --reload --port 8000
```

4. Call the extraction endpoint:

```bash
curl -s -X POST "http://localhost:8000/extract_fields" \
	-H "Content-Type: application/json" \
	-d '{"text":"Order 12345: Customer John Doe, phone 555-1234. Issue: delayed shipment."}'
```

Sample response:

```json
{
	"name": "John Doe",
	"order_id": "12345",
	"issue_type": "delayed shipment",
	"phone": "555-1234"
}
```

**Schema**

The API returns a `TicketExtraction` model with the following optional fields (string or null):

- `name`
- `order_id`
- `issue_type`
- `phone`

See the model in [app/schemas/models.py](app/schemas/models.py).

**How it works**

- `app/services/llm_client.py` calls OpenRouter with a strict system prompt (`app/utils/prompts.py`).
- The system prompt enforces a JSON schema and instructs the model to return `null` for missing fields.
- `app/main.py` exposes a single POST endpoint `/extract_fields` which returns a Pydantic `TicketExtraction`.

**Modify the prompt**

To change extraction rules or add fields, update the schema and prompt in [app/utils/prompts.py](app/utils/prompts.py).

**Development**

- Follow the code style in `pyproject.toml` (Black, mypy settings).
- For local iterations, run the API with uvicorn and test with `curl` or Postman.

**License**

This repository includes a `LICENSE` file. See it for licensing details.

---

If you'd like, I can: add example unit tests, expand the schema, or add an OpenAPI client example.