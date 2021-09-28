import ctypes

from f1_telemetry_2021.PackedLittleEndianStructure import PackedLittleEndianStructure


class CarMotionDataV1(PackedLittleEndianStructure):
    """This type is used for the 20-element 'carMotionData' array of the PacketMotionData_V1 type, defined below."""
    _fields_ = [
        ('worldPositionX', ctypes.c_float),  # World space X position
        ('worldPositionY', ctypes.c_float),  # World space Y position
        ('worldPositionZ', ctypes.c_float),  # World space Z position
        ('worldVelocityX', ctypes.c_float),  # Velocity in world space X
        ('worldVelocityY', ctypes.c_float),  # Velocity in world space Y
        ('worldVelocityZ', ctypes.c_float),  # Velocity in world space Z
        ('worldForwardDirX', ctypes.c_int16),  # World space forward X direction (normalised)
        ('worldForwardDirY', ctypes.c_int16),  # World space forward Y direction (normalised)
        ('worldForwardDirZ', ctypes.c_int16),  # World space forward Z direction (normalised)
        ('worldRightDirX', ctypes.c_int16),  # World space right X direction (normalised)
        ('worldRightDirY', ctypes.c_int16),  # World space right Y direction (normalised)
        ('worldRightDirZ', ctypes.c_int16),  # World space right Z direction (normalised)
        ('gForceLateral', ctypes.c_float),  # Lateral G-Force component
        ('gForceLongitudinal', ctypes.c_float),  # Longitudinal G-Force component
        ('gForceVertical', ctypes.c_float),  # Vertical G-Force component
        ('yaw', ctypes.c_float),  # Yaw angle in radians
        ('pitch', ctypes.c_float),  # Pitch angle in radians
        ('roll', ctypes.c_float)  # Roll angle in radians
    ]


