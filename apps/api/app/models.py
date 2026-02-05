from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base
from .vector_utils import Vector

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    reputation_score = Column(Integer, default=0)

    packs = relationship("VibePack", back_populates="owner")

class VibePack(Base):
    __tablename__ = "vibe_packs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    is_public = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    forked_from_id = Column(Integer, ForeignKey("vibe_packs.id"), nullable=True)

    # Relationships
    owner = relationship("User", back_populates="packs")
    # Self-referential relationship for forking
    forked_from = relationship("VibePack", remote_side=[id], backref="forks")

    rules = relationship("Rule", back_populates="pack", cascade="all, delete-orphan")
    terms = relationship("Term", back_populates="pack", cascade="all, delete-orphan")

class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text) # The active instruction
    explanation = Column(Text, nullable=True) # The "Why" or "Context"

    # rule_type maps to "Vibe" (Instruction) or "Anti-Pattern" (Constraint)
    rule_type = Column(String, default="Instruction")

    tags = Column(String, nullable=True) # Comma-separated tags for Vibes

    pack_id = Column(Integer, ForeignKey("vibe_packs.id"))
    votes = Column(Integer, default=0)

    # Vector embedding for semantic search
    embedding = Column(Vector(1536))

    pack = relationship("VibePack", back_populates="rules")

class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    definition_raw = Column(Text, nullable=True) # AI's definition
    definition_personal = Column(Text, nullable=True) # User's note/insight
    pack_id = Column(Integer, ForeignKey("vibe_packs.id"))

    # Vector embedding for semantic search
    embedding = Column(Vector(1536))

    pack = relationship("VibePack", back_populates="terms")
