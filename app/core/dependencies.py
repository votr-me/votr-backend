from fastapi import BackgroundTasks

from app.core.config import config
from app.services import (
    GeocodioAsyncAPIClient,
)


async def get_geocodio_client(
    background_tasks: BackgroundTasks,
) -> GeocodioAsyncAPIClient:
    client = GeocodioAsyncAPIClient(
        api_key=config.GEOCODIO_API_KEY,
    )
    background_tasks.add_task(client.close)
    return client