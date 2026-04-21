"""
Module for validating and processing alien contact logs.
"""
from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Enumeration of authorized extraterrestrial contact types."""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Model for validating cosmic contact reports with custom business rules."""
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_rules(self) -> 'AlienContact':
        """Validates complex business rules for specific contact types."""
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) must include a message")

        return self


def main() -> None:
    """Demonstrates alien contact validation rules."""
    print("Alien Contact Log Validation")
    print("=" * 40)
    print("Valid contact report:")
    try:
        true_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print(f"ID: {true_contact.contact_id}")
        print(f"Type: {true_contact.contact_type.value}")
        print(f"Location: {true_contact.location}")
        print(f"Signal: {true_contact.signal_strength}/10")
        print(f"Duration: {true_contact.duration_minutes} minutes")
        print(f"Witnesses: {true_contact.witness_count}")
        print(f"Message: '{true_contact.message_received}'")
    except ValidationError as error:
        print(f"Unexpect error: {error}")
    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_TELE_99",
            timestamp=datetime.now(),
            location="Moon Base Alpha",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1
        )
    except ValidationError as error_message:
        print(error_message.errors()[0]['msg'])


if __name__ == "__main__":
    main()
