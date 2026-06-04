import time
import uuid

from fastapi import Request

from app.logger import logger


async def log_requests(
    request: Request,
    call_next
):

    trace_id = str(
        uuid.uuid4()
    )[:8]

    start = time.time()

    response = await call_next(
        request
    )

    latency = round(
        (
            time.time()
            -
            start
        ) * 1000,
        2
    )

    logger.info(

        f"trace_id={trace_id} "
        f"path={request.url.path} "
        f"method={request.method} "
        f"status={response.status_code} "
        f"latency_ms={latency}"

    )

    return response