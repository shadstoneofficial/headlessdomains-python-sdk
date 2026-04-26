import pytest
from headlessdomains import Client, AsyncClient

def test_client_init():
    client = Client(api_key="hd_test_123")
    assert client._http.headers.get("x-api-key") == "hd_test_123"

def test_async_client_init():
    client = AsyncClient(api_key="hd_test_123")
    assert client._http.headers.get("x-api-key") == "hd_test_123"
