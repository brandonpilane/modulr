from sqlalchemy import (
    Column, Integer, String, ForeignKey, Time, Enum, Table
)
from sqlalchemy.orm import relationship
from ..database import Base
import enum

# Define enum for lesson_type
class LessonTypeEnum(enum.Enum):
    lecture = "lecture"
    tutorial = "tutorial"
    lab = "lab"

class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    modules = relationship("Module", back_populates="program")

class YearLevel(Base):
    __tablename__ = "year_levels"
    id = Column(Integer, primary_key=True, autoincrement=True)
    level = Column(Integer, unique=True, nullable=False)
    modules = relationship("Module", back_populates="year_level")

class Module(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    program_id = Column(Integer, ForeignKey("programs.id"), nullable=False)
    year_level_id = Column(Integer, ForeignKey("year_levels.id"), nullable=False)

    program = relationship("Program", back_populates="modules")
    year_level = relationship("YearLevel", back_populates="modules")
    lessons = relationship("Lesson", back_populates="module")

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    lessons = relationship("Lesson", back_populates="location")

class TimeSlot(Base):
    __tablename__ = "time_slots"
    id = Column(Integer, primary_key=True, autoincrement=True)
    day_of_week = Column(String, nullable=False)  # e.g. "Monday"
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    lesson_time_slots = relationship("LessonTimeSlot", back_populates="time_slot")

class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    lesson_type = Column(Enum(LessonTypeEnum), nullable=False)

    module = relationship("Module", back_populates="lessons")
    location = relationship("Location", back_populates="lessons")
    time_slots = relationship(
        "LessonTimeSlot", back_populates="lesson", cascade="all, delete-orphan"
    )

class LessonTimeSlot(Base):
    __tablename__ = "lesson_time_slots"
    lesson_id = Column(Integer, ForeignKey("lessons.id"), primary_key=True)
    time_slot_id = Column(Integer, ForeignKey("time_slots.id"), primary_key=True)

    lesson = relationship("Lesson", back_populates="time_slots")
    time_slot = relationship("TimeSlot", back_populates="lesson_time_slots")
