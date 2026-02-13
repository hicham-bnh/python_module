from pydantic import ValidationError, model_validator, BaseModel, field_validator
from datetime import datetime
from typing import Optional
from enum import Enum

class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

class AlienContact(BaseModel):
    contact_id: str
    timestamp: datetime
    location: str
    contact_type: ContactType
    signal_strength: float
    duration_minutes: int
    witness_count: int
    message_received: Optional[str]
    is_verified: bool

    @field_validator('contact_id')
    @classmethod
    def check_contact(cls, contact_id: str) -> str:
        if len(contact_id) < 5 or len(contact_id) > 15:
            raise ValueError("contact_id must be less than 15 and more than 5")
        return contact_id
    
    @field_validator('location')
    @classmethod
    def check_location(cls, location: str) -> str:
        if len(location) < 3 or len(location) > 100:
            raise ValueError("location must be less than 100 or more than 3")
        return location
    
    @field_validator('contact_type')
    @classmethod
    def check_contact_type(cls, contact_type: ContactType) -> ContactType:
        if contact_type is not ContactType:
            raise ValueError("contact_type invalid")
        return contact_type

    @field_validator('signal_strenght')
    @classmethod
    def check_signal(cls, signal_strenght: float) -> float:
        if signal_strenght < 0 or signal_strenght > 10.0:
            raise ValueError("signal_strenght should be less than 10 and modre than 0")
        return signal_strenght
    
    @field_validator('duration_minutes')
    @classmethod
    def check_duration(cls, duration_minutes: int) -> int:
        if duration_minutes < 1 or duration_minutes > 1440:
            raise ValueError("min duration 1min and max 1440min = 24h")
        return duration_minutes
    
    @field_validator('witness_count')
    @classmethod
    def check_witness(cls, witness_count: int) -> int:
        if witness_count < 0 or witness_count > 1000:
            raise ValueError("min people 1 and max 100")
        return witness_count
    
    @field_validator('message_received')
    @classmethod
    def check_message(cls, message_received: Optional[str]) -> Optional[str]:
        if message_received is not None and len(message_received) > 500:
            raise ValueError("max len for the mesaage is 500")
        return message_received
    
    @field_validator('is_verified')
    @classmethod
    def check_verifiction(cls, is_verified: bool) -> bool:
        if not isinstance(is_verified, bool):
            raise ValueError("is_verified must be true or false")
        return (is_verified)

    @model_validator(mode='after')
    @classmethod
    def check_rules(cls, model):
        id = model.data.get('contact_id')
        if not id.startswith("AC"):
            raise ValueError("contac id must begin with AC")