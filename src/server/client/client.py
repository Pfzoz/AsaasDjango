from dataclasses import dataclass, field
from pydantic import BaseModel

@dataclass
class Client(BaseModel):
    name: str = field(repr=True)
    cpfCnpj: str = field(repr=True)
    email: str = None
    phone: str = None
    mobile_phone: str = None
    postal_code: str = None
    address: str = None
    address_number: str = None
    complement: str = None
    province: str = None
    external_reference: str = None
    notification_disabled: bool = None
    additional_emails: str = None
    municipal_inscription: str = None
    state_inscription: str = None
    observations: str = None
    group_name: str = None
    company: str = None
