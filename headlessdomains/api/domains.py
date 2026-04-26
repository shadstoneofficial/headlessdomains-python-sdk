from typing import Optional, Dict, Any, List
from . import BaseAPI
from ..models import DomainAvailability, DomainProfile
from ..exceptions import PaymentRequiredError

class DomainsAPI(BaseAPI):
    """Operations related to Domains."""
    
    def search(self, domain: str) -> DomainAvailability:
        """Check if a domain is available for registration."""
        response = self.client.get("/api/v1/search", params={"domain": domain})
        data = self._handle_response(response)
        
        return DomainAvailability(
            name=domain,
            is_available=data.get("is_available", False),
            price=data.get("price"),
            currency=data.get("currency"),
            reason=data.get("reason"),
        )
        
    def lookup(self, domain: str) -> DomainProfile:
        """Lookup an existing domain's profile and DNS records."""
        response = self.client.get(f"/api/v1/lookup/{domain}")
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
        
    def register(self, domain: str, years: int = 1) -> Dict[str, Any]:
        """
        Register a new domain.
        
        If the account has sufficient Gems, it will complete immediately.
        If using MPP, this will raise a PaymentRequiredError containing the structured payment request.
        """
        payload = {"domain": domain, "years": years}
        response = self.client.post("/api/v1/domains/register", json=payload)
        
        # This will natively raise PaymentRequiredError if a 402 is returned
        data = self._handle_response(response)
        return data
        
    def renew(self, domain: str, years: int = 1) -> Dict[str, Any]:
        """
        Renew an existing domain.
        
        If the account has sufficient Gems, it will complete immediately.
        If using MPP, this will raise a PaymentRequiredError containing the structured payment request.
        """
        payload = {"domain": domain, "years": years}
        response = self.client.post("/api/v1/domains/renew", json=payload)
        
        # This will natively raise PaymentRequiredError if a 402 is returned
        data = self._handle_response(response)
        return data
