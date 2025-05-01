# Travel Itinerary Backend

This backend system allows you to manage and retrieve travel itineraries, and get recommendations using an MCP server.

## 🔧 Setup Instructions

1. **Install dependencies**
```bash
pip install -r requirements.txt
```
2. **Seed the database**

```bash
python seed/seed.py
```
3. **Run the main FastAPI server**

```bash
uvicorn app.main:app --reload --port 8000
```
4. **Run the MCP recommendation server**
   
```bash
uvicorn app.mcp_server:mcp_app --reload --port 8001
```
