import uuid
from dataclasses import dataclass, field
from datetime import datetime

from app.domain.entities.base import BaseEntity
from app.domain.events.messages import NewMessageReceivedEvent
from app.domain.values.messages import Text, Title





@dataclass
class Message(BaseEntity):


    created_at: datetime = field(default=datetime.now(), kw_only=True)
    text: Text

@dataclass
class Chat(BaseEntity):
    created_at: datetime = field(default=datetime.now(), kw_only=True)
    title: Title
    messages:list[Message] = field(default_factory=list,kw_only=True)




    def add_message(self,message:Message):
        self.messages.append(message)
        self.register_event(NewMessageReceivedEvent(message_text=message.text.as_generic_type(),
                                                    chat_oid=self.oid,
                                                    message_oid=message.oid))
