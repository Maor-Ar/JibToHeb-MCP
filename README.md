# Jibberish-to-Hebrew MCP

MCP server that converts text between “gibberish” English and Hebrew by swapping characters according to the QWERTY ↔ Hebrew (SI 1452) keyboard layout.

## Tools

- `qwerty_to_hebrew_text` — Converts English-looking gibberish (typed with Hebrew in mind but keyboard set to English) to Hebrew.
- `hebrew_to_qwerty_text` — Converts Hebrew text to the equivalent QWERTY key sequence.

## Install and run

### With pip

```bash
pip install jibberish-to-hebrew-mcp
jibberish-to-hebrew-mcp
```

## With uv
```bash
uvx jibberish-to-hebrew-mcp
```
## 🧠 Cursor / Claude Config
Add to your MCP config (~/.cursor/mcp.json):
```bash
json
{
  "mcpServers": {
    "jibberish-to-hebrew": {
      "command": "jibberish-to-hebrew-mcp",
      "args": []
    }
  }
}
```
If command not on PATH, use full path or uvx:
```bash
json
{
  "mcpServers": {
    "jibberish-to-hebrew": {
      "command": "uvx",
      "args": ["jibberish-to-hebrew-mcp"]
    }
  }
}
```
## ✨ Example
text
```bash
> qwerty_to_hebrew_text "r,nhoh"
> שלום

```
