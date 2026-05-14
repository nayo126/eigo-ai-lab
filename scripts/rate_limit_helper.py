"""Common helper: detect claude CLI rate-limit signals and persist resumable state."""
from __future__ import annotations
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

STATE_FILE = Path.home() / "RATE_LIMIT_STATE.json"

RATE_PATTERNS = (
    r"rate.?limit",
    r"too many requests",
    r"429",
    r"quota",
    r"usage limit",
    r"daily limit",
    r"max.{0,20}token",
    r"exceeded",
)


def looks_like_rate_limit(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    return any(re.search(p, t) for p in RATE_PATTERNS)


def mark_rate_limited(component: str, hint: str = "") -> None:
    state = load_state()
    state[component] = {
        "blocked_at": datetime.now(timezone.utc).isoformat(),
        "next_retry_at": _next_retry_iso(),
        "hint": hint[:300],
        "attempts": state.get(component, {}).get("attempts", 0) + 1,
    }
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2))


def mark_clear(component: str) -> None:
    state = load_state()
    if component in state:
        del state[component]
        STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2))


def is_currently_blocked(component: str) -> bool:
    state = load_state()
    info = state.get(component)
    if not info:
        return False
    nxt = info.get("next_retry_at")
    if not nxt:
        return True
    try:
        nxt_dt = datetime.fromisoformat(nxt.replace("Z", "+00:00"))
    except ValueError:
        return True
    return datetime.now(timezone.utc) < nxt_dt


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text())
    except Exception:
        return {}


def _next_retry_iso() -> str:
    # exponential backoff: try again in 1h
    from datetime import timedelta
    return (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()
