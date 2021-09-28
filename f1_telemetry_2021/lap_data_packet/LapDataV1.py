import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class LapDataV1(PackedLittleEndianStructure):
    """This type is used for the 20-element 'lapData' array of the PacketLapData_V1 type, defined below."""
    _fields_ = [
        ('lastLapTimeInMS', ctypes.c_uint32),  # Last lap time in milliseconds
        ('currentLapTimeInMS', ctypes.c_uint32),  # Current time around the lap in milliseconds
        ('sector1TimeInMS', ctypes.c_uint16),  # Sector 1 time in milliseconds
        ('sector2TimeInMS', ctypes.c_uint16),  # Sector 2 time in milliseconds
        ('lapDistance', ctypes.c_float),  # Distance vehicle is around current lap in metres – could be negative if
        # line hasn’t been crossed yet
        ('totalDistance', ctypes.c_float),  # Total distance travelled in session in metres – could be negative if
        # line hasn’t been crossed yet
        ('safetyCarDelta', ctypes.c_float),  # Delta in seconds for safety car
        ('carPosition', ctypes.c_uint8),  # Car race position
        ('currentLapNum', ctypes.c_uint8),  # Current lap number
        ('pitStatus', ctypes.c_uint8),  # 0 = none, 1 = pitting, 2 = in pit area
        ('numPitStops', ctypes.c_uint8),  # Number of pit stops taken in this race
        ('sector', ctypes.c_uint8),  # 0 = sector1, 1 = sector2, 2 = sector3
        ('currentLapInvalid', ctypes.c_uint8),  # Current lap invalid - 0 = valid, 1 = invalid
        ('penalties', ctypes.c_uint8),  # Accumulated time penalties in seconds to be added
        ('warnings', ctypes.c_uint8),  # Accumulated number of warnings issued
        ('numUnservedDriveThroughPens', ctypes.c_uint8),  # Num drive through pens left to serve
        ('numUnservedStopGoPens', ctypes.c_uint8),  # Num stop go pens left to serve
        ('gridPosition', ctypes.c_uint8),  # Grid position the vehicle started the race in
        ('driverStatus', ctypes.c_uint8),  # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out
        # lap, 4 = on track
        ('resultStatus', ctypes.c_uint8),  # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished,
        # 4 = didnotfinish, 5 = disqualified, 6 = not classified, 7 = retired
        ('pitLaneTimerActive', ctypes.c_uint8),  # Pit lane timing, 0 = inactive, 1 = active
        ('pitLaneTimeInLaneInMS', ctypes.c_uint16),  # If active, the current time spent in the pit lane in ms
        ('pitStopTimerInMS', ctypes.c_uint16),  # Time of the actual pit stop in ms
        ('pitStopShouldServePen', ctypes.c_uint8)  # Whether the car should serve a penalty at this stop
    ]
