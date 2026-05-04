import os 
import redis 
from fastapi import HTTPException, Depends, status 
from auth.auth import get_api_key 

redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

RATE_LIMIT = 10 
WINDOW_SECONDS = 60

def check_rate_limit(api_key: str = Depends(get_api_key)) -> str:
    key = f"rate_limit:{api_key}"
    current = redis_client.get(key)

    if current and int(current) >= RATE_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS, 
            detail=f"Rate limit exceeded. Max {RATE_LIMIT} requests per {WINDOW_SECONDS} seconds."
        )

    pipe = redis_client.pipeline()
    pipe.incr(key)
    pipe.expire(key, WINDOW_SECONDS)
    pipe.execute()

    return api_key
     
