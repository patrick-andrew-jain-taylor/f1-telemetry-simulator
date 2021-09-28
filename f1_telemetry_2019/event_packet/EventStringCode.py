import enum


@enum.unique
class EventStringCode(enum.Enum):
    """Value as specified in the PacketEventData_V1.eventStringCode header field, used to distinguish packet types."""
    SSTA = b'SSTA'
    SEND = b'SEND'
    FTLP = b'FTLP'
    RTMT = b'RTMT'
    DRSE = b'DRSE'
    DRSD = b'DRSD'
    TMPT = b'TMPT'
    CHQF = b'CHQF'
    RCWN = b'RCWN'


EventStringCode.short_description = {
    EventStringCode.SSTA: 'Session Started',
    EventStringCode.SEND: 'Session Ended',
    EventStringCode.FTLP: 'Fastest Lap',
    EventStringCode.RTMT: 'Retirement',
    EventStringCode.DRSE: 'DRS enabled',
    EventStringCode.DRSD: 'DRS disabled',
    EventStringCode.TMPT: 'Team mate in pits',
    EventStringCode.CHQF: 'Chequered flag',
    EventStringCode.RCWN: 'Race Winner'
}

EventStringCode.long_description = {
    EventStringCode.SSTA: 'Sent when the session starts',
    EventStringCode.SEND: 'Sent when the session ends',
    EventStringCode.FTLP: 'When a driver achieves the fastest lap',
    EventStringCode.RTMT: 'When a driver retires',
    EventStringCode.DRSE: 'Race control have enabled DRS',
    EventStringCode.DRSD: 'Race control have disabled DRS',
    EventStringCode.TMPT: 'Your team mate has entered the pits',
    EventStringCode.CHQF: 'The chequered flag has been waved',
    EventStringCode.RCWN: 'The race winner is announced'
}
