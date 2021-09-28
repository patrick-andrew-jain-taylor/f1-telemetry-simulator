import ctypes

from f1_telemetry_2019 import PackedLittleEndianStructure


class LapDataV1(PackedLittleEndianStructure):
    """This type is used for the 20-element 'lapData' array of the PacketLapData_V1 type, defined below."""
    _fields_ = [

        ('lastLapTime', ctypes.c_float),  # Last lap time in seconds
        ('currentLapTime', ctypes.c_float),  # Current time around the lap in seconds
        ('bestLapTime', ctypes.c_float),  # Best lap time of the session in seconds
        ('sector1Time', ctypes.c_float),  # Sector 1 time in seconds
        ('sector2Time', ctypes.c_float),  # Sector 2 time in seconds
        ('lapDistance', ctypes.c_float),  # Distance vehicle is around current lap in metres – could
        # be negative if line hasn’t been crossed yet
        ('totalDistance', ctypes.c_float),  # Total distance travelled in session in metres – could
        # be negative if line hasn’t been crossed yet
        ('safetyCarDelta', ctypes.c_float),  # Delta in seconds for safety car
        ('carPosition', ctypes.c_uint8),  # Car race position
        ('currentLapNum', ctypes.c_uint8),  # Current lap number
        ('pitStatus', ctypes.c_uint8),  # 0 = none, 1 = pitting, 2 = in pit area
        ('sector', ctypes.c_uint8),  # 0 = sector1, 1 = sector2, 2 = sector3
        ('currentLapInvalid', ctypes.c_uint8),  # Current lap invalid - 0 = valid, 1 = invalid
        ('penalties', ctypes.c_uint8),  # Accumulated time penalties in seconds to be added
        ('gridPosition', ctypes.c_uint8),  # Grid position the vehicle started the race in
        ('driverStatus', ctypes.c_uint8),  # Status of driver - 0 = in garage, 1 = flying lap
        # 2 = in lap, 3 = out lap, 4 = on track
        ('resultStatus', ctypes.c_uint8)  # Result status - 0 = invalid, 1 = inactive, 2 = active
        # 3 = finished, 4 = disqualified, 5 = not classified
        # 6 = retired
    ]
