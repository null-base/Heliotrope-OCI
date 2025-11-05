from dataclasses import dataclass

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from heliotrope.infrastructure.sqlalchemy.mixin import Schema


@dataclass
class CharacterSchema(Schema):
    __tablename__ = "character"

    character: Mapped[str] = mapped_column(String(255), unique=True)
    url: Mapped[str] = mapped_column(String(255))
