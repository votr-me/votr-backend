from fastapi import BackgroundTasks
from app.services import (
    OpenSecretsAsyncAPIClient,
    GeocodioAsyncAPIClient,
    FECAsyncAPIClient,
    CongressAPIAsyncClient,
)
from app.core.config import config


async def get_opensecrets_client(
    background_tasks: BackgroundTasks,
) -> OpenSecretsAsyncAPIClient:
    client = OpenSecretsAsyncAPIClient(
        api_key=config.OPENSECRETS_API_KEY, service_name="opensecrets"
    )
    background_tasks.add_task(client.close)  # Only close the HTTP client
    return client


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


async def get_fec_client(
    background_tasks: BackgroundTasks,
) -> OpenSecretsAsyncAPIClient:
    client = FECAsyncAPIClient(api_key=config.FEC_API_KEY, service_name="fec")
    background_tasks.add_task(client.close)  # Only close the HTTP client
    return client


async def get_cdg_client(
    background_tasks: BackgroundTasks,
) -> CongressAPIAsyncClient:
    client = CongressAPIAsyncClient(
        api_key=config.CONGRESS_GOV_API_KEY,
        service_name="congress_dot_gov",
        api_key_name="X-Api-Key",
    )
    background_tasks.add_task(client.close)
    return client
