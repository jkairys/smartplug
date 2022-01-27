import os
from smartplug.model.plug import Plug
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

EMAIL = os.environ.get('MEROSS_EMAIL')
PASSWORD = os.environ.get('MEROSS_PASSWORD')


async def list_all_plugs(manager: MerossManager, http_api_client: MerossHttpClient, device_type="mss310"):
    # Retrieve all the MSS310 devices that are registered on this account
    await manager.async_device_discovery()
    plugs = manager.find_devices(device_type=device_type)

    if len(plugs) < 1:
        return []

    ret = []
    for p in plugs:
        await p.async_update()
        ret.append(p)

    await http_api_client.async_logout()

    return ret