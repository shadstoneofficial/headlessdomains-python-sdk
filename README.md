# Headless Domains Python SDK

The official Python SDK for the Headless Domains API. Build decentralized identities, register agent names, and execute Machine-to-Machine (M2M) payments effortlessly.

## Installation

```bash
pip install headlessdomains
```

## Quick Start

### 1. Anonymous Agent Provisioning (Zero-Human Start)
AI Agents can onboard themselves without a human account:

```python
from headlessdomains import Client

client = Client() # No auth needed to provision
agent = client.agents.provision("my-cool-agent")

print(f"My API Key: {agent.api_key}")
print(f"Give this code to my human owner: {agent.claim_code}")
```

### 2. Authenticated Usage
Once you have an API key, use it to search and lookup domains:

```python
from headlessdomains import Client

client = Client(api_key="hd_agent_XXXXX")

# Check availability
availability = client.domains.search("janice.agent")
if availability.is_available:
    print(f"Domain is available for {availability.price} Gems")

# Get domain profile
profile = client.domains.lookup("janice.agent")
print(f"Bio: {profile.bio}")
print(f"Skills: {profile.skills}")
```

### 3. Machine-to-Machine Payments (MPP)

**Note on Registration Auth:** To register or renew domains, an agent must either be claimed by a human account (GFAVIP) or you must authenticate directly using a `gfavip_token`. Using an unclaimed `hd_agent_` key alone will return a `401 Authentication Error`.

The SDK natively catches and parses `402 Payment Required` responses, giving you structured data to execute smart contract transactions.

```python
from headlessdomains import Client, PaymentRequiredError

# Use a GFAVIP token (or a fully claimed agent api_key) for registration
client = Client(gfavip_token="gfavip_XXXXX")

try:
    client.domains.register("mybot.chatbot", years=1)
    print("Registered successfully with existing Gems!")
except PaymentRequiredError as e:
    print(f"Payment Required!")
    print(f"Send {e.amount} wei to {e.recipient}")
    print(f"Currency Contract: {e.currency} on Chain {e.chain_id}")
    print(f"Session ID to use in Memo: {e.session_id}")
    
    # ... execute your web3 transaction ...
```

## Async Support
An asynchronous client is also available for high-concurrency systems:

```python
import asyncio
from headlessdomains import AsyncClient

async def main():
    async with AsyncClient(api_key="hd_agent_XXXXX") as client:
        profile = await client.domains.lookup("janice.agent")
        print(profile.status)

asyncio.run(main())
```