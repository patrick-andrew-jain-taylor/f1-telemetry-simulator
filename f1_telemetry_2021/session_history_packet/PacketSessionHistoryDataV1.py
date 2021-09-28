import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from LapHistoryDataV1 import LapHistoryDataV1


class PacketSessionHistoryDataV1(PackedLittleEndianStructure):
    """
    This packet contains lap times and tyre usage for the session.

    This packet works slightly differently to other packets. To reduce CPU and bandwidth, each packet relates to a
    specific vehicle and is sent every 1/20 s, and the vehicle being sent is cycled through. Therefore in a 20 car
    race you should receive an update for each vehicle at least once per second.

    Note that at the end of the race, after the final classification packet has been sent, a final bulk update of all
    the session histories for the vehicles in that session will be sent.

    Frequency: 20 per second but cycling through cars
    Size: 1155 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('carIdx', ctypes.c_uint8),  # Index of the car this lap data relates to
        ('numLaps', ctypes.c_uint8),  # Num laps in the data (including current partial lap)
        ('numTyreStints', ctypes.c_uint8),  # Number of tyre stints in the data
        ('bestLapTimeLapNum', ctypes.c_uint8),  # Lap the best lap time was achieved on
        ('bestSector1LapNum', ctypes.c_uint8),  # Lap the best Sector 1 time was achieved on
        ('bestSector2LapNum', ctypes.c_uint8),  # Lap the best Sector 2 time was achieved on
        ('bestSector3LapNum', ctypes.c_uint8),  # Lap the best Sector 3 time was achieved on,
        ('lapHistoryData', LapHistoryDataV1 * 100),  # 100 laps of data max
        ('100 laps of data max', TyreStintHistoryDataV1 * 8)
    ]
