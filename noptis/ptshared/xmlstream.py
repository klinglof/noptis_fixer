from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.pubtrans.com/XMLStream/1.0"


@dataclass
class AbstractMessage:
    message_id: Optional[str] = field(default=None,
                                      metadata={
                                          "name": "MessageId",
                                          "type": "Attribute",
                                          "required": True,
                                      })


class ErrorType(Enum):
    INTERNALERROR = "INTERNALERROR"
    TIMEOUT = "TIMEOUT"
    SERVICECLOSED = "SERVICECLOSED"
    NOTSUCCEDED = "NOTSUCCEDED"
    NOTGRANTED = "NOTGRANTED"
    NOTSUPPORTED = "NOTSUPPORTED"
    NOTUNDERSTOOD = "NOTUNDERSTOOD"


@dataclass
class MessageBatch:
    """
    A set of messages sent in one batch.

    :ivar peer_id:
    :ivar last_processed_message_id: This attribute contains a reference
        to the last succesfully recieved message on the parallell stream
        working in the opposite direction.  Left out if no messages have
        been processed yet or if the peer does not support this function
    :ivar max_message_interval: Denotes the maximum interval between
        messages. If no message has been sent after half this timespan,
        an Idle message must be sent. If at the recieving end, no
        message has been recieved within the timespan, the reciever
        shall try to send an error message followed by the closing root
        element and then terminate the connection. It is the client that
        is responsible for re-establishing the connection regardless
        which peer that detects a time-out.
    """
    peer_id: Optional[str] = field(default=None,
                                   metadata={
                                       "name": "PeerId",
                                       "type": "Attribute",
                                       "required": True,
                                   })
    last_processed_message_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastProcessedMessageId",
            "type": "Attribute",
        })
    max_message_interval: XmlDuration = field(default=XmlDuration("PT60S"),
                                              metadata={
                                                  "name": "MaxMessageInterval",
                                                  "type": "Attribute",
                                              })


@dataclass
class Message(AbstractMessage):
    pass


@dataclass
class Request(AbstractMessage):
    pass


@dataclass
class Response(AbstractMessage):
    """
    :ivar on_message_id: This attribute contains a reference to the
        MessageId of the orginating Request message from the parallell
        stream working in the opposite direction.
    """
    on_message_id: Optional[str] = field(default=None,
                                         metadata={
                                             "name": "OnMessageId",
                                             "type": "Attribute",
                                             "required": True,
                                         })


@dataclass
class ErrorMessage(Message):
    """
    ErrorMessage indicates there is a problem not specifically connected with a
    certain recieved message.
    """
    type_value: Optional[ErrorType] = field(default=None,
                                            metadata={
                                                "name": "Type",
                                                "type": "Attribute",
                                                "required": True,
                                            })
    text: Optional[str] = field(default=None,
                                metadata={
                                    "name": "Text",
                                    "type": "Attribute",
                                })
    code: Optional[str] = field(default=None,
                                metadata={
                                    "name": "Code",
                                    "type": "Attribute",
                                })


@dataclass
class ErrorResponse(Message):
    """
    ErrorResponse indicates that there is a problem with a specific recieved
    message.

    :ivar on_message_id: This attribute contains a reference to the
        orginating message.
    :ivar type_value:
    :ivar text:
    :ivar code:
    """
    on_message_id: Optional[str] = field(default=None,
                                         metadata={
                                             "name": "OnMessageId",
                                             "type": "Attribute",
                                             "required": True,
                                         })
    type_value: Optional[ErrorType] = field(default=None,
                                            metadata={
                                                "name": "Type",
                                                "type": "Attribute",
                                                "required": True,
                                            })
    text: Optional[str] = field(default=None,
                                metadata={
                                    "name": "Text",
                                    "type": "Attribute",
                                })
    code: Optional[str] = field(default=None,
                                metadata={
                                    "name": "Code",
                                    "type": "Attribute",
                                })


@dataclass
class Idle(Message):
    pass


@dataclass
class LastProcessedMessageRequest(Request):
    pass


@dataclass
class LastProcessedMessageResponse(Response):
    """
    :ivar last_processed_message_id: This attribute contains a reference
        to the last succesfully recieved message on the parallell stream
        working in the opposite direction.
    """
    last_processed_message_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastProcessedMessageId",
            "type": "Attribute",
            "required": True,
        })
