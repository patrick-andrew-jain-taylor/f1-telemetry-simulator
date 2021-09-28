import ctypes

from f1_telemetry_2019 import PackedLittleEndianStructure, PacketHeader, MarshalZoneV1


class PacketSessionDataV1(PackedLittleEndianStructure):
    """The session packet includes details about the current session in progress.

    Frequency: 2 per second
    Size: 149 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('weather', ctypes.c_uint8),  # Weather - 0 = clear, 1 = light cloud, 2 = overcast
        # 3 = light rain, 4 = heavy rain, 5 = storm
        ('trackTemperature', ctypes.c_int8),  # Track temp. in degrees celsius
        ('airTemperature', ctypes.c_int8),  # Air temp. in degrees celsius
        ('totalLaps', ctypes.c_uint8),  # Total number of laps in this race
        ('trackLength', ctypes.c_uint16),  # Track length in metres
        ('sessionType', ctypes.c_uint8),  # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P
        # 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ
        # 10 = R, 11 = R2, 12 = Time Trial
        ('trackId', ctypes.c_int8),  # -1 for unknown, 0-21 for tracks, see appendix
        ('m_formula', ctypes.c_uint8),  # Formula, 0 = F1 Modern, 1 = F1 Classic, 2 = F2,
        # 3 = F1 Generic
        ('sessionTimeLeft', ctypes.c_uint16),  # Time left in session in seconds
        ('sessionDuration', ctypes.c_uint16),  # Session duration in seconds
        ('pitSpeedLimit', ctypes.c_uint8),  # Pit speed limit in kilometres per hour
        ('gamePaused', ctypes.c_uint8),  # Whether the game is paused
        ('isSpectating', ctypes.c_uint8),  # Whether the player is spectating
        ('spectatorCarIndex', ctypes.c_uint8),  # Index of the car being spectated
        ('sliProNativeSupport', ctypes.c_uint8),  # SLI Pro support, 0 = inactive, 1 = active
        ('numMarshalZones', ctypes.c_uint8),  # Number of marshal zones to follow
        ('marshalZones', MarshalZoneV1 * 21),  # List of marshal zones – max 21
        ('safetyCarStatus', ctypes.c_uint8),  # 0 = no safety car, 1 = full safety car
        # 2 = virtual safety car
        ('networkGame', ctypes.c_uint8)  # 0 = offline, 1 = online
    ]