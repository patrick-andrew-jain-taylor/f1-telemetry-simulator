import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class FastestLap(PackedLittleEndianStructure):
    _fields_ = [
        ('vehicleIdx', ctypes.c_uint8),  # Vehicle index of car achieving fastest lap
        ('lapTime', ctypes.c_float),  # Lap time is in seconds
    ]


class Retirement(PackedLittleEndianStructure):
    _fields_ = [
        ('vehicleIdx', ctypes.c_uint8)  # Vehicle index of car retiring
    ]


class TeamMateInPits(PackedLittleEndianStructure):
    _fields_ = [
        ('vehicleIdx', ctypes.c_uint8)  # Vehicle index of team mate
    ]


class RaceWinner(PackedLittleEndianStructure):
    _fields_ = [
        ('vehicleIdx', ctypes.c_uint8)  # Vehicle index of the race winner
    ]


class Penalty(PackedLittleEndianStructure):
    _fields_ = [
        ('penaltyType', ctypes.c_uint8),  # Penalty type – see Appendices
        ('infringementType', ctypes.c_uint8),  # Infringement type – see Appendices
        ('vehicleIdx', ctypes.c_uint8),  # Vehicle index of the car the penalty is applied to
        ('otherVehicleIdx', ctypes.c_uint8),  # Vehicle index of the other car involved
        ('time', ctypes.c_uint8),  # Time gained, or time spent doing action in seconds
        ('lapNum', ctypes.c_uint8),  # Lap the penalty occurred on
        ('placesGained', ctypes.c_uint8)  # Number of places gained by this
    ]


class SpeedTrap(PackedLittleEndianStructure):
    _fields_ = [
        ('vehicleIdx', ctypes.c_uint8),  # Vehicle index of the vehicle triggering speed trap
        ('speed', ctypes.c_float),  # Top speed achieved in kilometres per hour
        ('overallFastestInSession', ctypes.c_uint8),  # Overall fastest speed in session = 1, otherwise 0
        ('driverFastestInSession', ctypes.c_uint8)  # Fastest speed for driver in session = 1, otherwise 0
    ]


class StartLIghts(PackedLittleEndianStructure):
    _fields_ = [
        ('numLights', ctypes.c_uint8)  # Number of lights showing
    ]


class DriveThroughPenaltyServed(PackedLittleEndianStructure):
    _fields_ = [
        ('vehicleIdx', ctypes.c_uint8)  # Vehicle index of the vehicle serving drive through
    ]


class StopGoPenaltyServed(PackedLittleEndianStructure):
    _fields_ = [
        ('vehicleIdx', ctypes.c_uint8)  # Vehicle index of the vehicle serving stop go
    ]


class Flashback(PackedLittleEndianStructure):
    _fields_ = [
        ('flashbackFrameIdentifier', ctypes.c_uint32),  # Frame identifier flashed back to
        ('flashbackSessionTime', ctypes.c_float)  # Session time flashed back to
    ]


class Buttons(PackedLittleEndianStructure):
    _fields_ = [
        ('buttonStatus', ctypes.c_uint32)  # Bit flags specifying which buttons are being pressed currently - see
        # appendices
    ]


class EventDataDetailsV1(ctypes.Union):
    _fields_ = [
        ('FastestLap', FastestLap),
        ('Retirement', Retirement),
        ('TeamMateInPits', TeamMateInPits),
        ('RaceWinner', RaceWinner),
        ('Penalty', Penalty),
        ('SpeedTrap', SpeedTrap),
        ('StartLIghts', StartLIghts),
        ('DriveThroughPenaltyServed', DriveThroughPenaltyServed),
        ('StopGoPenaltyServed', StopGoPenaltyServed),
        ('Flashback', Flashback),
        ('Buttons', Buttons)
    ]
