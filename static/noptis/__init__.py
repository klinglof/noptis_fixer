from static.noptis.roi_from_pub_trans import Arrival
from static.noptis.roi_from_pub_trans import ArrivalCreateEvent
from static.noptis.roi_from_pub_trans import ArrivalDeviation
from static.noptis.roi_from_pub_trans import ArrivalDeviationEvent
from static.noptis.roi_from_pub_trans import ArrivalRef
from static.noptis.roi_from_pub_trans import ArrivalUpdateEvent
from static.noptis.roi_from_pub_trans import AssignmentEvent
from static.noptis.roi_from_pub_trans import BlockAssignment
from static.noptis.roi_from_pub_trans import CallRef
from static.noptis.roi_from_pub_trans import Connection
from static.noptis.roi_from_pub_trans import ConnectionCreateEvent
from static.noptis.roi_from_pub_trans import ConnectionDeleteEvent
from static.noptis.roi_from_pub_trans import ConnectionRef
from static.noptis.roi_from_pub_trans import ConnectionUpdateEvent
from static.noptis.roi_from_pub_trans import DatedVehicleJourney
from static.noptis.roi_from_pub_trans import DatedVehicleJourneyCreateEvent
from static.noptis.roi_from_pub_trans import DatedVehicleJourneyDeleteEvent
from static.noptis.roi_from_pub_trans import DatedVehicleJourneyRef
from static.noptis.roi_from_pub_trans import DeletedConnection
from static.noptis.roi_from_pub_trans import Departure
from static.noptis.roi_from_pub_trans import DepartureCreateEvent
from static.noptis.roi_from_pub_trans import DepartureDeviation
from static.noptis.roi_from_pub_trans import DepartureDeviationEvent
from static.noptis.roi_from_pub_trans import DepartureRef
from static.noptis.roi_from_pub_trans import DepartureUpdateEvent
from static.noptis.roi_from_pub_trans import DestinationDisplay
from static.noptis.roi_from_pub_trans import DestinationDisplayRef
from static.noptis.roi_from_pub_trans import DeviationCase
from static.noptis.roi_from_pub_trans import DeviationCaseEvent
from static.noptis.roi_from_pub_trans import DeviationCaseRef
from static.noptis.roi_from_pub_trans import DeviationMessage
from static.noptis.roi_from_pub_trans import DeviationMessageVersion
from static.noptis.roi_from_pub_trans import DeviationMessageVersionEvent
from static.noptis.roi_from_pub_trans import DeviationMessageVersionRef
from static.noptis.roi_from_pub_trans import DeviationReason
from static.noptis.roi_from_pub_trans import DriverAssignment
from static.noptis.roi_from_pub_trans import DutyAssignment
from static.noptis.roi_from_pub_trans import FromDocumentLayoutVersion
from static.noptis.roi_from_pub_trans import FromPubTransMessages
from static.noptis.roi_from_pub_trans import Instance
from static.noptis.roi_from_pub_trans import LaxDatedVehicleJourneyRef
from static.noptis.roi_from_pub_trans import Line
from static.noptis.roi_from_pub_trans import MessageVariant
from static.noptis.roi_from_pub_trans import MessageVariants
from static.noptis.roi_from_pub_trans import MonitoredVehicleJourney
from static.noptis.roi_from_pub_trans import MonitoredVehicleJourneyRef
from static.noptis.roi_from_pub_trans import NetworkDeviation
from static.noptis.roi_from_pub_trans import NetworkDeviationEvent
from static.noptis.roi_from_pub_trans import ObservedCallRef
from static.noptis.roi_from_pub_trans import OrganisationalUnitRef
from static.noptis.roi_from_pub_trans import OriginalInstance
from static.noptis.roi_from_pub_trans import Priority
from static.noptis.roi_from_pub_trans import PublicationDecision
from static.noptis.roi_from_pub_trans import PublicationDecisionEvent
from static.noptis.roi_from_pub_trans import PublicationScope
from static.noptis.roi_from_pub_trans import PublicationScopeRef
from static.noptis.roi_from_pub_trans import PublicationScopes
from static.noptis.roi_from_pub_trans import ScopeElement
from static.noptis.roi_from_pub_trans import ScopeElements
from static.noptis.roi_from_pub_trans import ServiceRequirement
from static.noptis.roi_from_pub_trans import ServiceRequirementRef
from static.noptis.roi_from_pub_trans import SourceControlAction
from static.noptis.roi_from_pub_trans import StopArea
from static.noptis.roi_from_pub_trans import StopPoint
from static.noptis.roi_from_pub_trans import StopScope
from static.noptis.roi_from_pub_trans import StopScopes
from static.noptis.roi_from_pub_trans import SubscriptionErrorReport
from static.noptis.roi_from_pub_trans import SubscriptionErrorResponse
from static.noptis.roi_from_pub_trans import SubscriptionResponse
from static.noptis.roi_from_pub_trans import SubscriptionResumeResponse
from static.noptis.roi_from_pub_trans import SubscriptionTerminationResponse
from static.noptis.roi_from_pub_trans import SynchronisationReport
from static.noptis.roi_from_pub_trans import TargetAudience
from static.noptis.roi_from_pub_trans import TargetAudiences
from static.noptis.roi_from_pub_trans import TimeScope
from static.noptis.roi_from_pub_trans import TransportAuthority
from static.noptis.roi_from_pub_trans import UpdatedArrival
from static.noptis.roi_from_pub_trans import UpdatedConnection
from static.noptis.roi_from_pub_trans import UpdatedDatedVehicleJourney
from static.noptis.roi_from_pub_trans import UpdatedDeparture
from static.noptis.roi_from_pub_trans import User
from static.noptis.roi_from_pub_trans import Vehicle
from static.noptis.roi_from_pub_trans import VehicleJourneyAssignment
from static.noptis.roi_from_pub_trans import VehicleJourneyDeviation
from static.noptis.roi_from_pub_trans import VehicleJourneyDeviationEvent
from static.noptis.roi_from_pub_trans import VehicleJourneyUpdateEvent
from static.noptis.roi_from_pub_trans import VehicleOperator
from static.noptis.roi_from_pub_trans import VehicleOperatorRef
from static.noptis.roi_shared_types import ArrivalState
from static.noptis.roi_shared_types import AssignmentState
from static.noptis.roi_shared_types import BusSizeType
from static.noptis.roi_shared_types import ConnectionState
from static.noptis.roi_shared_types import ContentType
from static.noptis.roi_shared_types import DepartureState
from static.noptis.roi_shared_types import DeviationReasonCategory
from static.noptis.roi_shared_types import EmissionLevel
from static.noptis.roi_shared_types import FuelType
from static.noptis.roi_shared_types import OperationActionType
from static.noptis.roi_shared_types import PassengerLevel
from static.noptis.roi_shared_types import PredictionState
from static.noptis.roi_shared_types import Status
from static.noptis.roi_shared_types import VehicleJourneyState

__all__ = [
    'Arrival',
    'ArrivalCreateEvent',
    'ArrivalDeviation',
    'ArrivalDeviationEvent',
    'ArrivalRef',
    'ArrivalUpdateEvent',
    'AssignmentEvent',
    'BlockAssignment',
    'CallRef',
    'Connection',
    'ConnectionCreateEvent',
    'ConnectionDeleteEvent',
    'ConnectionRef',
    'ConnectionUpdateEvent',
    'DatedVehicleJourney',
    'DatedVehicleJourneyCreateEvent',
    'DatedVehicleJourneyDeleteEvent',
    'DatedVehicleJourneyRef',
    'DeletedConnection',
    'Departure',
    'DepartureCreateEvent',
    'DepartureDeviation',
    'DepartureDeviationEvent',
    'DepartureRef',
    'DepartureUpdateEvent',
    'DestinationDisplay',
    'DestinationDisplayRef',
    'DeviationCase',
    'DeviationCaseEvent',
    'DeviationCaseRef',
    'DeviationMessage',
    'DeviationMessageVersion',
    'DeviationMessageVersionEvent',
    'DeviationMessageVersionRef',
    'DeviationReason',
    'DriverAssignment',
    'DutyAssignment',
    'FromDocumentLayoutVersion',
    'FromPubTransMessages',
    'Instance',
    'LaxDatedVehicleJourneyRef',
    'Line',
    'MessageVariant',
    'MessageVariants',
    'MonitoredVehicleJourney',
    'MonitoredVehicleJourneyRef',
    'NetworkDeviation',
    'NetworkDeviationEvent',
    'ObservedCallRef',
    'OrganisationalUnitRef',
    'OriginalInstance',
    'Priority',
    'PublicationDecision',
    'PublicationDecisionEvent',
    'PublicationScope',
    'PublicationScopeRef',
    'PublicationScopes',
    'ScopeElement',
    'ScopeElements',
    'ServiceRequirement',
    'ServiceRequirementRef',
    'SourceControlAction',
    'StopArea',
    'StopPoint',
    'StopScope',
    'StopScopes',
    'SubscriptionErrorReport',
    'SubscriptionErrorResponse',
    'SubscriptionResponse',
    'SubscriptionResumeResponse',
    'SubscriptionTerminationResponse',
    'SynchronisationReport',
    'TargetAudience',
    'TargetAudiences',
    'TimeScope',
    'TransportAuthority',
    'UpdatedArrival',
    'UpdatedConnection',
    'UpdatedDatedVehicleJourney',
    'UpdatedDeparture',
    'User',
    'Vehicle',
    'VehicleJourneyAssignment',
    'VehicleJourneyDeviation',
    'VehicleJourneyDeviationEvent',
    'VehicleJourneyUpdateEvent',
    'VehicleOperator',
    'VehicleOperatorRef',
    'ArrivalState',
    'AssignmentState',
    'BusSizeType',
    'ConnectionState',
    'ContentType',
    'DepartureState',
    'DeviationReasonCategory',
    'EmissionLevel',
    'FuelType',
    'OperationActionType',
    'PassengerLevel',
    'PredictionState',
    'Status',
    'VehicleJourneyState',
]
