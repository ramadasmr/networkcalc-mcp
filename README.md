# 🌐 networkcalc-mcp
[![smithery badge](https://smithery.ai/badge/@ramadasmr/networkcalc-mcp)](https://smithery.ai/server/@ramadasmr/networkcalc-mcp)

**networkcalc-mcp** is a server component (MCP Server) that powers utility services from [networkcalc.com](https://networkcalc.com). It provides a set of network tools accessible via API or integration with your own frontend.

## 🔧 Features

This server includes support for the following tools:

- 🔍 **DNS Lookup** – Resolve domain names to IP addresses and view DNS records.
- 🗂️ **WHOIS Lookup** – Retrieve registration and ownership details for domains and IPs.
- 📜 **SPF Lookup** – Inspect Sender Policy Framework (SPF) records for domains.
- 🔐 **Certificate Lookup** – Check SSL/TLS certificates for domains.
- 🧮 **Subnet Lookup** – Analyze IP subnets and CIDR ranges.

## 📖 How to Use

Run below command to add it to claude 
```bash
claude mcp add --transport http ramadasmr-networkcalc-mcp "https://server.smithery.ai/@ramadasmr/networkcalc-mcp/mcp"
```

## Installing via Smithery

To install NetworkCalc automatically via [Smithery](https://smithery.ai/server/@ramadasmr/networkcalc-mcp):

```bash
npx -y @smithery/cli install @ramadasmr/networkcalc-mcp
```

To see full usage instructions and available endpoints, please refer to the hosted service:
👉 [https://smithery.ai/server/@ramadasmr/networkcalc-mcp](https://smithery.ai/server/@ramadasmr/networkcalc-mcp)

