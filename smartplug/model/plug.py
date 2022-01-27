from pydantic.dataclasses import dataclass
from meross_iot.controller.device import ChannelInfo
from typing import List


@dataclass()
class OnlineStatus:
    name: str
    value: int


@dataclass()
class ChannelInfo:
    index: int
    is_master_channel: bool
    is_usb: bool
    name: str


@dataclass()
class Plug:
    name: str
    channels: List[ChannelInfo]
    firmware_version: str
    hardware_version: str
    online_status: OnlineStatus