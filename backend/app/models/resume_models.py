from pydantic import BaseModel
from typing import List, Optional


class Contact(BaseModel):
    email: str
    phone: str

class Education(BaseModel):
    degree: str
    college: str
    score: Optional[str] = None

class Experience(BaseModel):
    company: str
    role: str
    duration: Optional[str] = None
    description: Optional[str] = None

class Project(BaseModel):
    name: str
    description: str
    tech_stack: List[str]

class Resume(BaseModel):
    name: str
    summary: Optional[str] = None
    contact: Contact
    skills: List[str]
    education: List[Education]
    experience: List[Experience]
    projects: List[Project]
    certifications: Optional[List[str]] = None


resume_schema = Resume.model_json_schema()