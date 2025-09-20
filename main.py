import os
import uvicorn
import aiohttp
from mcp.server.fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware

mcp = FastMCP(name="NetworkCalc MCP Server")

async def fetch_dns_lookup(domain: str) -> str:
    url = f"https://networkcalc.com/api/dns/lookup/{domain}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                dns_data = await response.json()
                return str(dns_data)
            else:
                return f"Failed to retrieve DNS data for {domain}. Status code: {response.status}"

async def fetch_whois_lookup(domain: str) -> str:
    url = f"https://networkcalc.com/api/dns/whois/{domain}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                whois_data = await response.json()
                return str(whois_data)
            else:
                return f"Failed to retrieve WHOIS data for {domain}. Status code: {response.status}"

async def fetch_spf_lookup(domain: str) -> str:
    url = f"https://networkcalc.com/api/dns/spf/{domain}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            if response.status == 200:
                spf_data = await response.json()
                return str(spf_data)
            else:
                return f"Failed to retrieve SPF info for {domain}. Status code: {response.status}"


#
# tools definition 
#

@mcp.tool()
async def dns_lookup(domain: str) -> str:
    """Fetch DNS info for a given domain"""
    dns_info = await fetch_dns_lookup(domain)
    return f"DNS lookup results for {domain}:\n{dns_info}"

@mcp.tool()
async def whois_lookup(domain: str) -> str:
    """Fetch WHOIS info for a given domain"""
    whois_info = await fetch_whois_lookup(domain)
    return f"WHOIS lookup results for {domain}:\n{whois_info}"

@mcp.tool()
async def spf_lookup(domain: str) -> str:
    """Fetch SPF info for a given domain or host"""
    spf_info = await fetch_spf_lookup(domain)
    return f"SPF lookup results for {domain}:\n{spf_info}"

if __name__ == "__main__":
    # Get the Starlette app and add CORS middleware
    app = mcp.streamable_http_app()

    # Add CORS middleware with proper header exposure for MCP session management
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure this more restrictively in production
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["mcp-session-id", "mcp-protocol-version"],  # Allow client to read session ID
        max_age=86400,
    )

    # Use PORT environment variable
    port = int(os.environ.get("PORT", 8081))

    # Run the MCP server with HTTP transport using uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",  # Listen on all interfaces for containerized deployment
        port=port,
        log_level="debug"
    )
