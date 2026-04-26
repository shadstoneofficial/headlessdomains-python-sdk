from typing import Optional, Dict, Any, List
from . import BaseAPI
from ..models import DomainAvailability, DomainProfile
from ..exceptions import PaymentRequiredError

class AsyncDomainsAPI(BaseAPI):
    """Asynchronous operations related to Domains."""
    
    async def search(self, domain: str) -> DomainAvailability:
        """Check if a domain is available for registration."""
        response = await self.client.get("/api/v1/domains/search", params={"q": domain})
        data = self._handle_response(response)
        
        return DomainAvailability(
            name=domain,
            is_available=data.get("is_available", False),
            price=data.get("price"),
            currency=data.get("currency"),
            reason=data.get("reason"),
        )
        
    async def lookup(self, domain: str) -> DomainProfile:
        """Lookup an existing domain's profile and DNS records."""
        response = await self.client.get(f"/api/v1/lookup/{domain}")
        data = self._handle_response(response)
        
        profile_data = data.get("data", {})
        hns_bio = profile_data.get("hns_bio", {})
        
        return DomainProfile(
            name=domain,
            status=profile_data.get("status"),
            bio=hns_bio.get("bio"),
            location=hns_bio.get("location"),
            avatar_url=hns_bio.get("avatar"),
            urls=hns_bio.get("urls", []),
            skills=profile_data.get("skills", []),
            integrations=profile_data.get("integrations", {}),
        )
        
    async def register(self, domain: str, years: int = 1) -> Dict[str, Any]:
        """
        Register a new domain.
        
        Requires authentication via a `gfavip_token` or a fully claimed `api_key`.
        If the account has sufficient Gems, it will complete immediately.
        If using MPP, this will raise a PaymentRequiredError containing the structured payment request.
        """
        payload = {"domain": domain, "years": years}
        response = await self.client.post("/api/v1/domains/register", json=payload)
        
        # This will natively raise PaymentRequiredError if a 402 is returned
        data = self._handle_response(response)
        return data
        
    async def renew(self, domain: str, years: int = 1) -> Dict[str, Any]:
        """
        Renew an existing domain.
        
        Requires authentication via a `gfavip_token` or a fully claimed `api_key`.
        If the account has sufficient Gems, it will complete immediately.
        If using MPP, this will raise a PaymentRequiredError containing the structured payment request.
        """
        payload = {"domain": domain, "years": years}
        response = await self.client.post("/api/v1/domains/renew", json=payload)
        
        # This will natively raise PaymentRequiredError if a 402 is returned
        data = self._handle_response(response)
        return data
