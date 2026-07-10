#!/usr/bin/env python3
"""Atomic semantic topic ledger for the pregnancy visual content skill."""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "used-topics.json"


def normalize(value: str) -> str:
    value = value.casefold()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value)
    return " ".join(value.split())


def signature(topic: str, correct: str, wrong: str) -> str:
    return normalize(" | ".join((topic, correct, wrong)))


def load() -> dict:
    if not LEDGER.exists():
        return {"version": 1, "topics": []}
    with LEDGER.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data.get("topics"), list):
        raise ValueError("Invalid ledger: topics must be a list")
    return data


def atomic_save(data: dict) -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix="used-topics-", suffix=".json", dir=LEDGER.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, LEDGER)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def find_matches(data: dict, sig: str, threshold: float) -> list[tuple[float, dict]]:
    matches = []
    for item in data["topics"]:
        old = item.get("signature") or signature(
            item.get("topic", ""), item.get("correct", ""), item.get("wrong", "")
        )
        ratio = SequenceMatcher(None, sig, old).ratio()
        new_tokens, old_tokens = set(sig.split()), set(old.split())
        union = new_tokens | old_tokens
        jaccard = len(new_tokens & old_tokens) / len(union) if union else 1.0
        score = max(ratio, jaccard)
        if score >= threshold:
            matches.append((score, item))
    return sorted(matches, key=lambda pair: pair[0], reverse=True)


def add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--topic", required=True)
    parser.add_argument("--correct", required=True)
    parser.add_argument("--wrong", required=True)
    parser.add_argument("--threshold", type=float, default=0.70)


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    add_common(check)
    reserve = sub.add_parser("reserve")
    add_common(reserve)
    reserve.add_argument("--slug", required=True)
    reserve.add_argument("--owner", default="unknown")
    sub.add_parser("list")
    args = parser.parse_args()

    data = load()
    if args.command == "list":
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    sig = signature(args.topic, args.correct, args.wrong)
    matches = find_matches(data, sig, args.threshold)
    if matches:
        print(json.dumps({"unique": False, "matches": [
            {"score": round(score, 3), "topic": item.get("topic"), "slug": item.get("slug")}
            for score, item in matches[:5]
        ]}, ensure_ascii=False))
        return 2

    if args.command == "check":
        print(json.dumps({"unique": True}, ensure_ascii=False))
        return 0

    entry = {
        "slug": args.slug,
        "topic": args.topic,
        "correct": args.correct,
        "wrong": args.wrong,
        "signature": sig,
        "owner": args.owner,
        "reserved_at": datetime.now(timezone.utc).isoformat(),
    }
    data["topics"].append(entry)
    atomic_save(data)
    print(json.dumps({"reserved": True, "entry": entry}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
