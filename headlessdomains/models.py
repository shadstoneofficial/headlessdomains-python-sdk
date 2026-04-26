from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class AgentProvisionResult:
    agent_id: str
    api_key: str
    claim_code: str
    instructions: str

@dataclass
class DomainAvailability:
    name: str
    is_available: bool
    price: Optional[float] = None
    currency: Optional[str] = None
    reason: Optional[str] = None

@dataclass
class DomainProfile:
    name: str
    status: str
    bio: Optional[str] = None
    location: Optional[str] = None
    avatar_url: Optional[str] = None
    urls: List[str] = None
    skills: List[str] = None
    integrations: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.urls is None:
            self.urls = []
        if self.skills is None:
            self.skills = []
        if self.integrations is None:
            self.integrations = {}
