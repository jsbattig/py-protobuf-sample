from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Person(_message.Message):
    __slots__ = ["email", "id", "name", "phones"]
    class PhoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class PhoneNumber(_message.Message):
        __slots__ = ["number", "type"]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        number: str
        type: Person.PhoneType
        def __init__(self, number: _Optional[str] = ..., type: _Optional[_Union[Person.PhoneType, str]] = ...) -> None: ...
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HOME: Person.PhoneType
    ID_FIELD_NUMBER: _ClassVar[int]
    MOBILE: Person.PhoneType
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    WORK: Person.PhoneType
    email: str
    id: int
    name: str
    phones: _containers.RepeatedCompositeFieldContainer[Person.PhoneNumber]
    def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., email: _Optional[str] = ..., phones: _Optional[_Iterable[_Union[Person.PhoneNumber, _Mapping]]] = ...) -> None: ...
