import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader, CarMotionDataV1


class PacketMotionDataV1(PackedLittleEndianStructure):
    """The motion packet gives physics data for all the cars being driven.

    There is additional data for the car being driven with the goal of being able to drive a motion platform setup.

    N.B. For the normalised vectors below, to convert to float values divide by 32767.0f – 16-bit signed values are
    used to pack the data and on the assumption that direction values are always between -1.0f and 1.0f.

    Frequency: Rate as specified in menus
    Size: 1343 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('carMotionData', CarMotionDataV1 * 20),  # Data for all cars on track
        # Extra player car ONLY data
        ('suspensionPosition', ctypes.c_float * 4),  # Note: All wheel arrays have the following order:
        ('suspensionVelocity', ctypes.c_float * 4),  # RL, RR, FL, FR
        ('suspensionAcceleration', ctypes.c_float * 4),  # RL, RR, FL, FR
        ('wheelSpeed', ctypes.c_float * 4),  # Speed of each wheel
        ('wheelSlip', ctypes.c_float * 4),  # Slip ratio for each wheel
        ('localVelocityX', ctypes.c_float),  # Velocity in local space
        ('localVelocityY', ctypes.c_float),  # Velocity in local space
        ('localVelocityZ', ctypes.c_float),  # Velocity in local space
        ('angularVelocityX', ctypes.c_float),  # Angular velocity x-component
        ('angularVelocityY', ctypes.c_float),  # Angular velocity y-component
        ('angularVelocityZ', ctypes.c_float),  # Angular velocity z-component
        ('angularAccelerationX', ctypes.c_float),  # Angular acceleration x-component
        ('angularAccelerationY', ctypes.c_float),  # Angular acceleration y-component
        ('angularAccelerationZ', ctypes.c_float),  # Angular acceleration z-component
        ('frontWheelsAngle', ctypes.c_float)  # Current front wheels angle in radians
    ]
