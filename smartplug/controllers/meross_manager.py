from smartplug.model.plug import Plug
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager


async def login(email: str, password: str) -> MerossManager:
    # Setup the HTTP client API from user-password
    http_api_client = await MerossHttpClient.async_from_user_password(email=email, password=password)

    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    return manager, http_api_client
