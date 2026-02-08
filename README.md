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
