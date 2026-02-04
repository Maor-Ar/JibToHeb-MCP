# QWERTY (US) <-> Hebrew (SI 1452) keyboard layout mapping
# Same physical key produces different character depending on layout.

# When user intended to type Hebrew but keyboard was set to English, they get QWERTY
# characters that look like gibberish. We map those QWERTY keys -> Hebrew (SI 1452).
QWERTY_TO_HEBREW = {
    "q": "/",
    "w": "'",
    "e": "ק",
    "r": "ר",
    "t": "א",
    "y": "ט",
    "u": "ו",
    "i": "ן",  # final nun (same key as I)
    "o": "ם",  # final mem (same key as O)
    "p": "פ",
    "a": "ש",
    "s": "ד",
    "d": "ג",
    "f": "כ",
    "g": "ע",
    "h": "י",
    "j": "ח",
    "k": "ל",
    "l": "ך",  # final kaf
    "z": "ז",
    "x": "ס",
    "c": "ב",
    "v": "ה",
    "b": "נ",
    "n": "מ",
    "m": "צ",
    ";": "ף",  # final pe
    "'": ",",
    ",": "ת",
    ".": "ץ",  # final tsadi
    "/": ".",
    "[": "[",
    "]": "]",
    "\\": "\\",
    "`": "`",
    "-": "-",
    "=": "=",
}

# Reverse: Hebrew -> QWERTY (for decoding Hebrew typed with Hebrew layout
# but displayed/captured as if it were English, or for "Hebrew gibberish" -> English)
HEBREW_TO_QWERTY = {v: k for k, v in QWERTY_TO_HEBREW.items()}

# Add common alternate forms so both directions work well
# (e.g. regular נ/מ vs final ן/ם - same key on keyboard)
HEBREW_TO_QWERTY["נ"] = "b"
HEBREW_TO_QWERTY["מ"] = "n"
HEBREW_TO_QWERTY["כ"] = "f"
HEBREW_TO_QWERTY["ך"] = "l"  # already from ך->l
HEBREW_TO_QWERTY["פ"] = "p"
HEBREW_TO_QWERTY["ף"] = ";"  # already from ף->;
HEBREW_TO_QWERTY["צ"] = "m"
HEBREW_TO_QWERTY["ץ"] = "."  # already from ץ->.
# Comma and period: we have ',' -> ת and '.' -> ץ. So ת -> ',' and . (period) -> '/'
HEBREW_TO_QWERTY["."] = "/"  # period key
# Don't overwrite ת (already maps to ','). Good.


def qwerty_to_hebrew(text: str) -> str:
    """Convert text that looks like English gibberish (typed on Hebrew layout) to Hebrew."""
    return "".join(QWERTY_TO_HEBREW.get(c.lower(), c) for c in text)


def hebrew_to_qwerty(text: str) -> str:
    """Convert Hebrew (or Hebrew-looking) text to QWERTY as if typed on Hebrew keyboard."""
    return "".join(HEBREW_TO_QWERTY.get(c, c) for c in text)
