from typing import Optional, Dict, Any
import httpx
from .api.async_agents import AsyncAgentsAPI
from .api.async_domains import AsyncDomainsAPI

class AsyncClient:
    """Asynchronous client for the Headless Domains API."""
    
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
            
        self._http = httpx.AsyncClient(base_url=self.base_url, headers=headers)
        
        self.agents = AsyncAgentsAPI(self)
        self.domains = AsyncDomainsAPI(self)
        
    async def get(self, path: str, **kwargs) -> httpx.Response:
        return await self._http.get(path, **kwargs)
        
    async def post(self, path: str, **kwargs) -> httpx.Response:
        return await self._http.post(path, **kwargs)
        
    async def close(self):
        await self._http.aclose()
        
    async def __aenter__(self):
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
