from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import List
from typing import Optional

from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration

from static.noptis.ptshared.pt_shared_types import DirectionOfLineRef
from static.noptis.ptshared.pt_shared_types import JourneyPatternPointRef
from static.noptis.ptshared.pt_shared_types import LineRef
from static.noptis.ptshared.pt_shared_types import StopAreaRef
from static.noptis.ptshared.pt_shared_types import TransportAuthorityRef
from static.noptis.ptshared.pt_shared_types import YesNo
from static.noptis.ptshared.pt_xmlstream import Messages
from static.noptis.ptshared.pt_xmlstream import Request
from static.noptis.ptshared.xmlstream import ErrorMessage
from static.noptis.ptshared.xmlstream import ErrorResponse
from static.noptis.ptshared.xmlstream import Idle
from static.noptis.ptshared.xmlstream import LastProcessedMessageRequest
from static.noptis.ptshared.xmlstream import LastProcessedMessageResponse

__NAMESPACE__ = 'http://www.pubtrans.com/ROI/3.0'


@dataclass
class AssignmentEventSelection:
    pass


class ToDocumentLayoutVersion(Enum):
    """The set of values in the enumeration indicates the range of schema versions
    that this schema version is backward compatible with.

    Used to ensure that the schema version that an incoming document was
    validated against is not in conflict with this schema version.
    """
    VALUE_3_0_7 = '3.0.7'


@dataclass
class JourneyScopeElement:
    journey_transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'JourneyTransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    line_ref: Optional[LineRef] = field(default=None,
                                        metadata={
                                            'name': 'LineRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    direction_of_line_ref: Optional[DirectionOfLineRef] = field(
        default=None,
        metadata={
            'name': 'DirectionOfLineRef',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class NetworkDeviationEventSelection:
    expand_deviation_message_data: YesNo = field(
        default=YesNo.N,
        metadata={
            'name': 'ExpandDeviationMessageData',
            'type': 'Attribute',
        })


@dataclass
class PublicationScopeElement:
    journey_transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'JourneyTransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    line_ref: Optional[LineRef] = field(default=None,
                                        metadata={
                                            'name': 'LineRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })


@dataclass
class ScopeElement:
    journey_transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'JourneyTransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    line_ref: Optional[LineRef] = field(default=None,
                                        metadata={
                                            'name': 'LineRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    direction_of_line_ref: Optional[DirectionOfLineRef] = field(
        default=None,
        metadata={
            'name': 'DirectionOfLineRef',
            'type': 'Element',
            'namespace': '',
        })
    stop_transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'StopTransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    stop_area_ref: Optional[StopAreaRef] = field(default=None,
                                                 metadata={
                                                     'name': 'StopAreaRef',
                                                     'type': 'Element',
                                                     'namespace': '',
                                                 })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })
    concerns_arrivals: YesNo = field(default=YesNo.Y,
                                     metadata={
                                         'name': 'ConcernsArrivals',
                                         'type': 'Attribute',
                                     })
    concerns_departures: YesNo = field(default=YesNo.Y,
                                       metadata={
                                           'name': 'ConcernsDepartures',
                                           'type': 'Attribute',
                                       })


@dataclass
class SubscriptionResumeRequest(Request):
    """
    :ivar subscription_id: The subscription to be resumed. This
        attribute can be omitted for single subscription peers.
    :ivar start_utc_date_time: Data that is no longer valid after this
        point in time should be excluded from the subscription. Thus,
        vehicle journeys with an end date/time before this point in time
        should be excluded. If omitted then the subscription is resumed
        from the last confirmed time, which means that no data will be
        lost.
    :ivar synchronised_upto_utc_date_time: This attribute should contain
        the value from the last received Synchronisation Report. It
        could also be used to force the synchronisation to start from an
        earlier time, if previously received data has been lost.
        Observe that if this attribute is left out and the
        StartUtcDateTime is back in time or left out, then previously
        sent data might be retransmitted.
    """
    subscription_id: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'SubscriptionId',
                                               'type': 'Attribute',
                                           })
    start_utc_date_time: Optional[XmlDateTime] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'StartUtcDateTime',
                                                           'type': 'Attribute',
                                                       })
    synchronised_upto_utc_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'SynchronisedUptoUtcDateTime',
            'type': 'Attribute',
        })


@dataclass
class SubscriptionTerminationRequest(Request):
    """
    :ivar subscription_id: The subscription to be terminated. If this
        attribute is omitted then any current subscription held by the
        requesting Peer should be terminated.
    """
    subscription_id: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'SubscriptionId',
                                               'type': 'Attribute',
                                           })


@dataclass
class PublicationScopeElements:
    publication_scope_element: List[PublicationScopeElement] = field(
        default_factory=list,
        metadata={
            'name': 'PublicationScopeElement',
            'type': 'Element',
            'namespace': '',
            'min_occurs': 1,
        })


@dataclass
class ScopeElements:
    scope_element: List[ScopeElement] = field(default_factory=list,
                                              metadata={
                                                  'name': 'ScopeElement',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'min_occurs': 1,
                                              })


@dataclass
class DeviationCaseEventSelection:
    """
    :ivar scope_elements:
    :ivar publication_scope_elements:
    :ivar include_source_control_action: If Y then the underlying
        Control Action RII-report will be appended in the
        SourceControlAction attribute.
    :ivar deviation_message_version_events_only: If Y, then all other
        deviation case events will be excluded. This option could be
        used for display systems.
    """
    scope_elements: Optional[ScopeElements] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'ScopeElements',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })
    publication_scope_elements: Optional[PublicationScopeElements] = field(
        default=None,
        metadata={
            'name': 'PublicationScopeElements',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    include_source_control_action: YesNo = field(
        default=YesNo.N,
        metadata={
            'name': 'IncludeSourceControlAction',
            'type': 'Attribute',
        })
    deviation_message_version_events_only: YesNo = field(
        default=YesNo.N,
        metadata={
            'name': 'DeviationMessageVersionEventsOnly',
            'type': 'Attribute',
        })


@dataclass
class VehicleJourneyEventSelection:
    """
    :ivar scope_elements:
    :ivar look_ahead_duration: Defines how far in advance, using a
        rolling time frame, that production plan data should be
        provided. A point in time can be constructed by adding the look-
        ahead duration to the current time. Data that is not yet valid
        at that point in time should be excluded.
    :ivar expand_stop_data:
    :ivar expand_destination_data:
    :ivar expand_vehicle_data:
    :ivar expand_line_data:
    :ivar expand_vehicle_operator_data:
    :ivar expand_service_requirement_data:
    :ivar expand_deviation_message_data:
    :ivar exclude_intermediate_state_changes: Follow up applications
        only interested in the final states of objects can use this
        option.
    """
    scope_elements: Optional[ScopeElements] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'ScopeElements',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })
    look_ahead_duration: Optional[XmlDuration] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'LookAheadDuration',
                                                           'type': 'Attribute',
                                                           'required': True,
                                                       })
    expand_stop_data: YesNo = field(default=YesNo.N,
                                    metadata={
                                        'name': 'ExpandStopData',
                                        'type': 'Attribute',
                                    })
    expand_destination_data: YesNo = field(default=YesNo.N,
                                           metadata={
                                               'name': 'ExpandDestinationData',
                                               'type': 'Attribute',
                                           })
    expand_vehicle_data: YesNo = field(default=YesNo.N,
                                       metadata={
                                           'name': 'ExpandVehicleData',
                                           'type': 'Attribute',
                                       })
    expand_line_data: YesNo = field(default=YesNo.N,
                                    metadata={
                                        'name': 'ExpandLineData',
                                        'type': 'Attribute',
                                    })
    expand_vehicle_operator_data: YesNo = field(
        default=YesNo.N,
        metadata={
            'name': 'ExpandVehicleOperatorData',
            'type': 'Attribute',
        })
    expand_service_requirement_data: YesNo = field(
        default=YesNo.N,
        metadata={
            'name': 'ExpandServiceRequirementData',
            'type': 'Attribute',
        })
    expand_deviation_message_data: YesNo = field(
        default=YesNo.N,
        metadata={
            'name': 'ExpandDeviationMessageData',
            'type': 'Attribute',
        })
    exclude_intermediate_state_changes: YesNo = field(
        default=YesNo.N,
        metadata={
            'name': 'ExcludeIntermediateStateChanges',
            'type': 'Attribute',
        })


@dataclass
class BasicSubscriptionRequest(Request):
    vehicle_journey_event_selection: Optional[
        VehicleJourneyEventSelection] = field(
            default=None,
            metadata={
                'name': 'VehicleJourneyEventSelection',
                'type': 'Element',
                'namespace': '',
            })
    deviation_case_event_selection: Optional[
        DeviationCaseEventSelection] = field(default=None,
                                             metadata={
                                                 'name':
                                                 'DeviationCaseEventSelection',
                                                 'type': 'Element',
                                                 'namespace': '',
                                             })
    assignment_event_selection: Optional[AssignmentEventSelection] = field(
        default=None,
        metadata={
            'name': 'AssignmentEventSelection',
            'type': 'Element',
            'namespace': '',
        })
    network_deviation_event_selection: Optional[
        NetworkDeviationEventSelection] = field(
            default=None,
            metadata={
                'name': 'NetworkDeviationEventSelection',
                'type': 'Element',
                'namespace': '',
            })


@dataclass
class SubscriptionSetupRequest(BasicSubscriptionRequest):
    """
    :ivar start_utc_date_time: Data that is no longer valid after this
        point in time should be excluded from the subscription. Thus,
        vehicle journeys with an end date/time before this point in time
        should be excluded. If this attribute is omitted then the
        current time will be used as the start date/time.
    """
    start_utc_date_time: Optional[XmlDateTime] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'StartUtcDateTime',
                                                           'type': 'Attribute',
                                                       })


@dataclass
class SubscriptionUpdateRequest(BasicSubscriptionRequest):
    """
    :ivar subscription_id: The subscription to be modified. This
        attribute can be omitted for single subscription peers.
    """
    subscription_id: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'SubscriptionId',
                                               'type': 'Attribute',
                                           })


@dataclass
class ToPubTransMessages(Messages):
    """
    :ivar last_processed_message_request:
    :ivar last_processed_message_response:
    :ivar idle: If no other messages are sent after half the timespan
        indicated by the attribute MaxMessageInterval in the MessageBath
        element, an Idle message must be sent as a reassurance that the
        communication is OK.
    :ivar error_message:
    :ivar error_response:
    :ivar subscription_request: This request sets up and starts the
        subscription.
    :ivar subscription_update_request: This request modifies an existing
        subscription.
    :ivar subscription_resume_request: This request should be sent after
        reestabling a broken connection to resume the flow of subscribed
        data.
    :ivar subscription_termination_request: This request terminates the
        subscription.
    :ivar document_layout_version:
    """

    class Meta:
        namespace = 'http://www.pubtrans.com/ROI/3.0'

    last_processed_message_request: List[LastProcessedMessageRequest] = field(
        default_factory=list,
        metadata={
            'name': 'LastProcessedMessageRequest',
            'type': 'Element',
            'namespace': '',
        })
    last_processed_message_response: List[
        LastProcessedMessageResponse] = field(
            default_factory=list,
            metadata={
                'name': 'LastProcessedMessageResponse',
                'type': 'Element',
                'namespace': '',
            })
    idle: List[Idle] = field(default_factory=list,
                             metadata={
                                 'name': 'Idle',
                                 'type': 'Element',
                                 'namespace': '',
                             })
    error_message: List[ErrorMessage] = field(default_factory=list,
                                              metadata={
                                                  'name': 'ErrorMessage',
                                                  'type': 'Element',
                                                  'namespace': '',
                                              })
    error_response: List[ErrorResponse] = field(default_factory=list,
                                                metadata={
                                                    'name': 'ErrorResponse',
                                                    'type': 'Element',
                                                    'namespace': '',
                                                })
    subscription_request: List[SubscriptionSetupRequest] = field(
        default_factory=list,
        metadata={
            'name': 'SubscriptionRequest',
            'type': 'Element',
            'namespace': '',
        })
    subscription_update_request: List[SubscriptionUpdateRequest] = field(
        default_factory=list,
        metadata={
            'name': 'SubscriptionUpdateRequest',
            'type': 'Element',
            'namespace': '',
        })
    subscription_resume_request: List[SubscriptionResumeRequest] = field(
        default_factory=list,
        metadata={
            'name': 'SubscriptionResumeRequest',
            'type': 'Element',
            'namespace': '',
        })
    subscription_termination_request: List[
        SubscriptionTerminationRequest] = field(
            default_factory=list,
            metadata={
                'name': 'SubscriptionTerminationRequest',
                'type': 'Element',
                'namespace': '',
            })
    document_layout_version: Optional[ToDocumentLayoutVersion] = field(
        default=None,
        metadata={
            'name': 'DocumentLayoutVersion',
            'type': 'Attribute',
            'required': True,
        })
