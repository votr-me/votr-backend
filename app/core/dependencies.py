from fastapi import BackgroundTasks
from app.services import (
    GeocodioAsyncAPIClient,
)
from app.core.config import config

async def get_geocodio_client(
    background_tasks: BackgroundTasks,
) -> GeocodioAsyncAPIClient:
    client = GeocodioAsyncAPIClient(
        api_key=config.GEOCODIO_API_KEY,
        service_name="geocodio",
        api_key_name="api_key",
    )
    background_tasks.add_task(client.close)
    return client