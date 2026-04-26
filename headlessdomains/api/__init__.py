from typing import Optional, Dict, Any
import httpx
from ..exceptions import AuthenticationError, APIError, PaymentRequiredError

class BaseAPI:
    """Base class for API resources."""
    def __init__(self, client):
        self.client = client

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """Parse the response and handle Headless Domains specific error codes."""
        if response.status_code == 401 or response.status_code == 403:
            raise AuthenticationError(f"Authentication failed: {response.text}")
            
        try:
            data = response.json()
        except ValueError:
            raise APIError(f"Invalid JSON response: {response.text}", status_code=response.status_code)
            
        if response.status_code == 402:
            # Handle MPP Payment Required Flow
            raise PaymentRequiredError(
                message=data.get('error', 'Payment Required'),
                payment_request=data.get('payment_request', {}),
                session_id=data.get('session_id', ''),
                payment_request_b64=data.get('payment_request_b64', '')
            )
            
        if not (200 <= response.status_code < 300):
            raise APIError(
                message=data.get('error', 'Unknown API Error'),
                status_code=response.status_code,
                response=data
            )
            
        return data
