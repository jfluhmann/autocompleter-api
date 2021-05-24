from fastapi import FastAPI
from app.common.autocomplete import Autocomplete

app = FastAPI()

@app.get('/')
def root():
    """Test endpoint"""

    return {"ping": "pong"}

@app.get('/words/{word}')
async def words(word: str):
    """Return a list of autocomplete suggestions"""

    wordlist = Autocomplete.match(word)
    return {"words": wordlist}
