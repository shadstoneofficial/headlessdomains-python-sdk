from typing import Optional, Dict, Any
import httpx
from .api.agents import AgentsAPI
from .api.domains import DomainsAPI

class Client:
    """Synchronous client for the Headless Domains API."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        gfavip_token: Optional[str] = None,
        base_url: str = "https://headlessdomains.com"
    ):
        self.base_url = base_url.rstrip("/")
        headers = {"Content-Type": "application/json"}
        
        if api_key:
            headers["X-API-Key"] = api_key
        elif gfavip_token:
            headers["Authorization"] = f"Bearer {gfavip_token}"
            
        self._http = httpx.Client(base_url=self.base_url, headers=headers)
        
        self.agents = AgentsAPI(self)
        self.domains = DomainsAPI(self)
        
    def get(self, path: str, **kwargs) -> httpx.Response:
        return self._http.get(path, **kwargs)
        
    def post(self, path: str, **kwargs) -> httpx.Response:
        return self._http.post(path, **kwargs)
        
    def register(self, domain: str, namespace: str, years: int = 1, payment_method: str = "gems", workflows: dict = None) -> Dict[str, Any]:
        """Convenience method to register a domain."""
        return self.domains.register(domain, namespace, years, payment_method, workflows)
        
    def update_bio(self, domain: str, workflows: dict = None, **kwargs) -> Dict[str, Any]:
        """Convenience method to update an agent's bio and workflows."""
        return self.domains.update_bio(domain, workflows, **kwargs)
        
    def close(self):
        self._http.close()
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
