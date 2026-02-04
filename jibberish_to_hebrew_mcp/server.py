"""
MCP server: Jibberish <-> Hebrew keyboard layout converter.
Converts text that looks like English gibberish (typed with Hebrew layout) to Hebrew,
and Hebrew text to the equivalent QWERTY key sequence.
"""
from mcp.server.fastmcp import FastMCP
from keyboard_map import qwerty_to_hebrew, hebrew_to_qwerty

mcp = FastMCP(
    "jibberish-to-hebrew",
    json_response=True,
)


@mcp.tool()
def qwerty_to_hebrew_text(text: str) -> dict:
    """
    Convert English-looking gibberish to Hebrew by swapping each character
    from QWERTY keyboard layout to its counterpart on the Hebrew (SI 1452) layout.
    Use when someone typed Hebrew but their keyboard was set to English.
    """
    result = qwerty_to_hebrew(text)
    return {"original": text, "hebrew": result}


@mcp.tool()
def hebrew_to_qwerty_text(text: str) -> dict:
    """
    Convert Hebrew text to the equivalent QWERTY key sequence by swapping each
    Hebrew character to its counterpart on the US QWERTY keyboard layout.
    Use when someone typed English but their keyboard was set to Hebrew.
    """
    result = hebrew_to_qwerty(text)
    return {"original": text, "qwerty": result}


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
