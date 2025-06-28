from mcp.server.fastmcp import FastMCP
from zerodha_client import ZerodhaClient
from dotenv import load_dotenv
import os

# Initialize FastMCP server
mcp = FastMCP("trading_bot")

@mcp.tool()
# Place a market buy order
def buy(stock: str, quantity: int):
    client.place_order("BUY", stock, quantity)

@mcp.tool()
def sell(stock: str, quantity: int):
# Place a market sell order
    client.place_order("SELL", stock, quantity)

if __name__ == "__main__":
    # setting up the client to place orders
    # This will always return the same initialized instance
    load_dotenv()
    API_KEY = os.getenv("ZERODHA_API_KEY")
    API_SECRET = os.getenv("ZERODHA_API_SECRET")
    client = ZerodhaClient(api_key=API_KEY, api_secret=API_SECRET)
    
    mcp.run(transport="streamable-http")