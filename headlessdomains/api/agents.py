from typing import Optional, Dict, Any
from . import BaseAPI
from ..models import AgentProvisionResult

class AgentsAPI(BaseAPI):
    """Operations related to Agents."""
    
    def provision(self, name: str) -> AgentProvisionResult:
        """
        Anonymously provision a new agent without a GFAVIP account.
        Returns credentials including the api_key and claim_code.
        """
        response = self.client.post("/api/v1/agents/provision", json={"name": name})
        data = self._handle_response(response)
        
        result_data = data.get("data", {})
        return AgentProvisionResult(
            agent_id=result_data.get("agent_id"),
            api_key=result_data.get("api_key"),
            claim_code=result_data.get("claim_code"),
            instructions=result_data.get("instructions"),
        )
