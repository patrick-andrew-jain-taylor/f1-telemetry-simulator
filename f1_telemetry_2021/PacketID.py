import enum


@enum.unique
class PacketID(enum.IntEnum):
    """Value as specified in the PacketHeader.packetId header field, used to distinguish packet types."""

    MOTION = 0
    SESSION = 1
    LAP_DATA = 2
    EVENT = 3
    PARTICIPANTS = 4
    CAR_SETUPS = 5
    CAR_TELEMETRY = 6
    CAR_STATUS = 7
    FINAL_CLASSIFICATION = 8
    LOBBY_INFO = 9
    CAR_DAMAGE = 10
    SESSION_HISTORY = 11


PacketID.short_description = {
    PacketID.MOTION: 'Motion',
    PacketID.SESSION: 'Session',
    PacketID.LAP_DATA: 'Lap Data',
    PacketID.EVENT: 'Event',
    PacketID.PARTICIPANTS: 'Participants',
    PacketID.CAR_SETUPS: 'Car Setups',
    PacketID.CAR_TELEMETRY: 'Car Telemetry',
    PacketID.CAR_STATUS: 'Car Status',
    PacketID.FINAL_CLASSIFICATION: 'Final Classification',
    PacketID.LOBBY_INFO: 'Lobby Info',
    PacketID.CAR_DAMAGE: 'Car Damage',
    PacketID.SESSION_HISTORY: 'Session History',
}

PacketID.long_description = {
    PacketID.MOTION: 'Contains all motion data for player\'s car – only sent while player is in control',
    PacketID.SESSION: 'Data about the session – track, time left',
    PacketID.LAP_DATA: 'Data about all the lap times of cars in the session',
    PacketID.EVENT: 'Various notable events that happen during a session',
    PacketID.PARTICIPANTS: 'List of participants in the session, mostly relevant for multiplayer',
    PacketID.CAR_SETUPS: 'Packet detailing car setups for cars in the race',
    PacketID.CAR_TELEMETRY: 'Telemetry data for all cars',
    PacketID.CAR_STATUS: 'Status data for all cars',
    PacketID.FINAL_CLASSIFICATION: 'Final classification confirmation at the end of a race',
    PacketID.LOBBY_INFO: 'Information about players in a multiplayer lobby',
    PacketID.CAR_DAMAGE: 'Damage status for all cars',
    PacketID.SESSION_HISTORY: 'Lap and tyre data for session'
}
