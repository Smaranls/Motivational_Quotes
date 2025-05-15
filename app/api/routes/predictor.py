import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.quote import Quote

router = APIRouter()


@router.get("/", response_model=Quote)
async def get_motivational_quote():
    url = "https://zenquotes.io/api/random"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # raise error for bad status
            data = response.json()
            # ZenQuotes returns a list of quotes, take the first one
            quote_text = data[0]["q"]
            author = data[0]["a"]
            return Quote(quote=quote_text, author=author)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching quote")