import logging
import time
from fastapi import Request
from fastapi.responses import Response 


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

async def log_and_time_requests(request: Request, call_next) -> Response:
    start_time = time.time()

    response = await call_next(request)

    duration_ms = round((time.time() - start_time) * 1000, 2)

    logger.info(
        f"{request.method} {request.url.path} | "
        f"status={response.status_code} | "
        f"duration={duration_ms}ms | "
        f"client={request.client.host}"
    )
    
    return response