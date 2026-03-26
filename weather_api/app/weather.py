import httpx
import json
import redis
from os import getenv
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status, Request
import re
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

load_dotenv('.env')

API_KEY = getenv("WEATHER_API_KEY")
REDIS_HOST = getenv("REDIS_HOST")
REDIS_PORT = getenv("REDIS_PORT")
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
CACHE_TTL = 43200  # 12 hours

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

def normalise_string(string: str) -> str:
    return re.sub(r'\s+', ' ', string.strip()).lower()

def get_redis():
    r = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT), decode_responses=True)
    try:
        yield r
    finally:
        r.close()

@app.get("/weather/{city}")
@limiter.limit("10/minute")
def get_weather_data(request: Request, city: str = Depends(normalise_string), r = Depends(get_redis)):
    cache_key = f"weather:{city}"
    cached = r.get(cache_key)

    if cached is not None:
        print(f"Returning cached data for {city} : {cached}")
        return json.loads(cached)

    print(f"Cache miss for {city}, fetching from API")

    response = httpx.get(
        f"{BASE_URL}/{city}",
        params={
            "unitGroup": "metric",
            "key": API_KEY,
            "contentType": "json",
            "include": "current",
        }
    )

    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == status.HTTP_400_BAD_REQUEST:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"City '{city}' not found")
        else:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="Weather API error")
        
    weather_data = response.json()
            
    r.set(cache_key, json.dumps(weather_data), ex=CACHE_TTL) 
    return weather_data

    