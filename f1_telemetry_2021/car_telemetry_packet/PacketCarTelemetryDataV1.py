import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from CarTelemetryDataV1 import CarTelemetryDataV1


class PacketCarTelemetryDataV1(PackedLittleEndianStructure):
    """This packet details telemetry for all the cars in the race.

    It details various values that would be recorded on the car such as speed, throttle application, DRS etc.

    Frequency: Rate as specified in menus
    Size: 1347 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('carTelemetryData', CarTelemetryDataV1 * 22),
        ('mfdPanelIndex', ctypes.c_uint8),  # Index of MFD panel open - 255 = MFD closed Single player, race – 0 =
        # Car setup, 1 = Pits 2 = Damage, 3 =  Engine, 4 = Temperatures May vary depending on game mode
        ('mfdPanelIndexSecondaryPlayer', ctypes.c_uint8),  # See aboveBit flags specifying which buttons are being
        ('suggestedGear', ctypes.c_uint32)  # Suggested gear for the player (1-8) 0 if no gear suggested
    ]
