from enum import Enum

__NAMESPACE__ = "http://www.pubtrans.com/ROI/3.0"


class ArrivalState(Enum):
    NOTEXPECTED = "NOTEXPECTED"
    NOTCALLED = "NOTCALLED"
    EXPECTED = "EXPECTED"
    CANCELLED = "CANCELLED"
    DUE = "DUE"
    ARRIVED = "ARRIVED"
    ASSUMEDARRIVED = "ASSUMEDARRIVED"
    PASSED = "PASSED"
    MISSED = "MISSED"


class AssignmentState(Enum):
    ASSIGNED = "ASSIGNED"
    SIGNEDON = "SIGNEDON"


class BusSizeType(Enum):
    """
    Code for generic bus sizes.

    :cvar ARTICUL: Articulated bus (ledbuss)
    :cvar BOGGIE: Boggie bus
    :cvar DDECKER: Double decker bus
    :cvar MINI: Mini bus
    :cvar SMALL: Small bus
    :cvar STANDARD: Standard or normal bus
    """
    ARTICUL = "ARTICUL"
    BOGGIE = "BOGGIE"
    DDECKER = "DDECKER"
    MINI = "MINI"
    SMALL = "SMALL"
    STANDARD = "STANDARD"


class ConnectionState(Enum):
    NOTEXPECTED = "NOTEXPECTED"
    EXPECTED = "EXPECTED"
    CANCELLED = "CANCELLED"
    WAITING = "WAITING"
    RELEASED = "RELEASED"
    SUCCEEDED = "SUCCEEDED"
    ASSUMEDSUCCEEDED = "ASSUMEDSUCCEEDED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


class ContentType(Enum):
    TEXT_PLAIN = "text/plain"
    URN_MP3 = "urn/mp3"


class DepartureState(Enum):
    NOTEXPECTED = "NOTEXPECTED"
    NOTCALLED = "NOTCALLED"
    EXPECTED = "EXPECTED"
    CANCELLED = "CANCELLED"
    ATSTOP = "ATSTOP"
    BOARDING = "BOARDING"
    BOARDINGCLOSED = "BOARDINGCLOSED"
    DEPARTED = "DEPARTED"
    ASSUMEDDEPARTED = "ASSUMEDDEPARTED"
    PASSED = "PASSED"
    MISSED = "MISSED"
    REPLACED = "REPLACED"


class DeviationReasonCategory(Enum):
    ACCIDENT = "ACCIDENT"
    ASSAULT = "ASSAULT"
    VANDALISM = "VANDALISM"
    NODRIVER = "NODRIVER"
    STRIKE = "STRIKE"
    VEHICLESHORTAGE = "VEHICLESHORTAGE"
    TECHNICALFAILURE = "TECHNICALFAILURE"
    VEHICLEBREAKDOWN = "VEHICLEBREAKDOWN"
    INFRASTRUCTUREFAILURE = "INFRASTRUCTUREFAILURE"
    DELAYS = "DELAYS"
    REDUCEDSPEED = "REDUCEDSPEED"
    WEATHER = "WEATHER"
    CONGESTION = "CONGESTION"
    ROADWORK = "ROADWORK"
    CHANGEDROUTE = "CHANGEDROUTE"
    OTHER = "OTHER"
    TRAFFICINCIDENT = "TRAFFICINCIDENT"
    EARLYDEPARTURE = "EARLYDEPARTURE"
    WRONGROUTE = "WRONGROUTE"
    POLICEDECISION = "POLICEDECISION"
    SAFETY = "SAFETY"
    SMOKE = "SMOKE"
    MEDICAL = "MEDICAL"
    HEAVYLOAD = "HEAVYLOAD"
    RESTOREOPERATION = "RESTOREOPERATION"
    MAINTENANCE = "MAINTENANCE"
    SERVICEINFO = "SERVICEINFO"
    MARKETINGINFO = "MARKETINGINFO"


class EmissionLevel(Enum):
    """
    Emission standard according to European norms.
    """
    EURO_I = "EURO_I"
    EURO_II = "EURO_II"
    EURO_III = "EURO_III"
    EURO_IV = "EURO_IV"
    EURO_V = "EURO_V"
    EURO_VI = "EURO_VI"


class FuelType(Enum):
    """
    :cvar BATTERY: Electric (battery)
    :cvar BIOGAS: Biogas
    :cvar CNG: Natural gas.
    :cvar DIESEL: Diesel
    :cvar DIESELN: Diesel, standard
    :cvar DIESELL: Diesel, light
    :cvar E85: Blend of 85% ethanol and 15% petrol
    :cvar ELECTRIC: Electric (overhead wire or equivalent)
    :cvar HYBRIDDB: Hybrid, diesel/battery
    :cvar HYDROGEN: Hydrogen
    :cvar LPG: LPG.
    :cvar PETROLL: Petrol, leaded
    :cvar PETROLUL: Petrol, unleaded
    :cvar UNKNOWN: Fuel unknown
    """
    BATTERY = "BATTERY"
    BIOGAS = "BIOGAS"
    CNG = "CNG"
    DIESEL = "DIESEL"
    DIESELN = "DIESELN"
    DIESELL = "DIESELL"
    E85 = "E85"
    ELECTRIC = "ELECTRIC"
    HYBRIDDB = "HYBRIDDB"
    HYDROGEN = "HYDROGEN"
    LPG = "LPG"
    PETROLL = "PETROLL"
    PETROLUL = "PETROLUL"
    UNKNOWN = "UNKNOWN"


class OperationActionType(Enum):
    INFORMATION = "INFORMATION"
    JOURNEYCREATION = "JOURNEYCREATION"
    JOURNEYCANCELLATION = "JOURNEYCANCELLATION"
    PARTIALJOURNEYCANCELLATION = "PARTIALJOURNEYCANCELLATION"
    JOURNEYORDERING = "JOURNEYORDERING"
    CHANGEOFJOURNEYPATTERN = "CHANGEOFJOURNEYPATTERN"
    CHANGEOFJOURNEYPROGRESS = "CHANGEOFJOURNEYPROGRESS"
    CHANGEOFJOURNEYTIMING = "CHANGEOFJOURNEYTIMING"
    CONNECTIONCREATION = "CONNECTIONCREATION"
    CONNECTIONMODIFICATION = "CONNECTIONMODIFICATION"
    CONNECTIONCANCELLATION = "CONNECTIONCANCELLATION"
    STOPPOINTCLOSED = "STOPPOINTCLOSED"
    STOPPOINTATTENTION = "STOPPOINTATTENTION"
    STOPPOINTLIMITEDACCESS = "STOPPOINTLIMITEDACCESS"
    BRIDGINGDEVICECLOSED = "BRIDGINGDEVICECLOSED"
    BRIDGINGDEVICEATTENTION = "BRIDGINGDEVICEATTENTION"
    BRIDGINGDEVICELIMITEDACCESS = "BRIDGINGDEVICELIMITEDACCESS"
    STATIONENTRANCEPOINTCLOSED = "STATIONENTRANCEPOINTCLOSED"
    STATIONENTRANCEPOINTATTENTION = "STATIONENTRANCEPOINTATTENTION"
    STATIONENTRANCEPOINTLIMITEDACCESS = "STATIONENTRANCEPOINTLIMITEDACCESS"
    VEHICLEWORKASSIGNMENT = "VEHICLEWORKASSIGNMENT"
    VEHICLEWORKDEASSIGNMENT = "VEHICLEWORKDEASSIGNMENT"


class PassengerLevel(Enum):
    EMPTY = "EMPTY"
    SEATSAVAILABLE = "SEATSAVAILABLE"
    STANDINGPASSENGERS = "STANDINGPASSENGERS"
    PASSENGERSLEFTBEHIND = "PASSENGERSLEFTBEHIND"


class PredictionState(Enum):
    NORMAL = "NORMAL"
    LOSTCONTACT = "LOSTCONTACT"
    UNRELIABLE = "UNRELIABLE"


class Status(Enum):
    LIMITEDACCESS = "LIMITEDACCESS"
    CLOSED = "CLOSED"
    ATTENTION = "ATTENTION"


class VehicleJourneyState(Enum):
    """
    :cvar NOTEXPECTED:
    :cvar NOTRUN:
    :cvar EXPECTED:
    :cvar ASSIGNED:
    :cvar CANCELLED:
    :cvar SIGNEDON:
    :cvar ASSUMEDCOMPLETED: The combined vehicle journey state covers
        the phase before a dated journey is monitored, the states above,
        as well as the monitored phase, see states below.
    :cvar ATORIGIN:
    :cvar FASTPROGRESS:
    :cvar NORMALPROGRESS:
    :cvar SLOWPROGRESS:
    :cvar NOPROGRESS:
    :cvar OFFROUTE:
    :cvar ABORTED:
    :cvar COMPLETED:
    """
    NOTEXPECTED = "NOTEXPECTED"
    NOTRUN = "NOTRUN"
    EXPECTED = "EXPECTED"
    ASSIGNED = "ASSIGNED"
    CANCELLED = "CANCELLED"
    SIGNEDON = "SIGNEDON"
    ASSUMEDCOMPLETED = "ASSUMEDCOMPLETED"
    ATORIGIN = "ATORIGIN"
    FASTPROGRESS = "FASTPROGRESS"
    NORMALPROGRESS = "NORMALPROGRESS"
    SLOWPROGRESS = "SLOWPROGRESS"
    NOPROGRESS = "NOPROGRESS"
    OFFROUTE = "OFFROUTE"
    ABORTED = "ABORTED"
    COMPLETED = "COMPLETED"