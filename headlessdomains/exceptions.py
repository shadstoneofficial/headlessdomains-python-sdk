class HeadlessDomainsError(Exception):
    """Base exception for Headless Domains API."""
    pass

class AuthenticationError(HeadlessDomainsError):
    """Raised when authentication fails (401/403)."""
    pass

class APIError(HeadlessDomainsError):
    """Raised when the API returns a generic error."""
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response or {}

class PaymentRequiredError(HeadlessDomainsError):
    """
    Raised during MPP flows when a 402 Payment Required is returned.
    Contains the structured payment request data needed to complete the transaction.
    """
    def __init__(self, message: str, payment_request: dict, session_id: str, payment_request_b64: str = None):
        super().__init__(message)
        self.payment_request = payment_request
        self.session_id = session_id
        self.payment_request_b64 = payment_request_b64
        
    @property
    def amount(self) -> str:
        """The amount required in wei/base units (e.g. '520000')."""
        return self.payment_request.get('amount')
        
    @property
    def recipient(self) -> str:
        """The wallet address to send the payment to."""
        return self.payment_request.get('recipient')
        
    @property
    def currency(self) -> str:
        """The smart contract address of the currency (e.g. USDC)."""
        return self.payment_request.get('currency')
        
    @property
    def chain_id(self) -> int:
        """The blockchain network ID."""
        return self.payment_request.get('chainId')
