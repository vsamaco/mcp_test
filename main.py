from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="HelloMCP")


@mcp.tool()
def hello() -> str:
    """Returns a greeting message."""
    return "Hello World from FastMCP!"


if __name__ == "__main__":
    mcp.run()  # uses default HTTP transport
