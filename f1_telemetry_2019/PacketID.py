import enum


@enum.unique
class PacketID(enum.IntEnum):
    """Value as specified in the PacketHeader.packetId header field, used to distinguish packet types."""

    MOTION = 0
    SESSION = 1
    LAP_DATA = 2
    EVENT = 3
    PARTICIPANTS = 4  # 0.2 Hz (once every five seconds)
    CAR_SETUPS = 5
    CAR_TELEMETRY = 6
    CAR_STATUS = 7


PacketID.short_description = {
    PacketID.MOTION: 'Motion',
    PacketID.SESSION: 'Session',
    PacketID.LAP_DATA: 'Lap Data',
    PacketID.EVENT: 'Event',
    PacketID.PARTICIPANTS: 'Participants',
    PacketID.CAR_SETUPS: 'Car Setups',
    PacketID.CAR_TELEMETRY: 'Car Telemetry',
    PacketID.CAR_STATUS: 'Car Status'
}

PacketID.long_description = {
    PacketID.MOTION: 'Contains all motion data for player\'s car – only sent while player is in control',
    PacketID.SESSION: 'Data about the session – track, time left',
    PacketID.LAP_DATA: 'Data about all the lap times of cars in the session',
    PacketID.EVENT: 'Various notable events that happen during a session',
    PacketID.PARTICIPANTS: 'List of participants in the session, mostly relevant for multiplayer',
    PacketID.CAR_SETUPS: 'Packet detailing car setups for cars in the race',
    PacketID.CAR_TELEMETRY: 'Telemetry data for all cars',
    PacketID.CAR_STATUS: 'Status data for all cars such as damage'
}
