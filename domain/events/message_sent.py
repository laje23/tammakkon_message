# domain/events/bot_account_created.py
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class MessageSentEvent:
    entity_id: int
    sent_time: datetime
