from dataclasses import dataclass

from static.noptis.ptshared.xmlstream import ErrorMessage
from static.noptis.ptshared.xmlstream import \
    ErrorResponse as XmlstreamErrorResponse
from static.noptis.ptshared.xmlstream import Message as XmlstreamMessage
from static.noptis.ptshared.xmlstream import MessageBatch
from static.noptis.ptshared.xmlstream import Request as XmlstreamRequest
from static.noptis.ptshared.xmlstream import Response as XmlstreamResponse

__NAMESPACE__ = 'http://www.pubtrans.com/PT/1.0'


@dataclass
class ErrorReport(ErrorMessage):
    pass


@dataclass
class ErrorResponse(XmlstreamErrorResponse):
    pass


@dataclass
class Message(XmlstreamMessage):
    pass


@dataclass
class Messages(MessageBatch):
    pass


@dataclass
class Report(XmlstreamMessage):
    pass


@dataclass
class Request(XmlstreamRequest):
    pass


@dataclass
class Response(XmlstreamResponse):
    pass
