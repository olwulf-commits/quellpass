from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections.abc import Callable, Iterable, Sequence
from typing import Any


def passages(pages: Sequence[dict[str, Any]], max_pages: int = 20, max_per_page: int = 12) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for page in pages[:max_pages]:
        url = str(page.get("url") or "").strip()
        body = str(page.get("text") or "").strip()
        if not url.startswith(("http://", "https://")) or not body:
            continue
        sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", body) if part.strip()]
        selected: list[str] = []
        current = ""
        for sentence in sentences:
            if current and len(current) + len(sentence) + 1 > 700:
                if len(current) >= 80:
                    selected.append(current)
                current = sentence
            else:
                current = f"{current} {sentence}".strip()
        if len(current) >= 80:
            selected.append(current)
        for passage in selected[:max_per_page]:
            result.append({"url": url, "passage": passage})
    return result


def _cosine(left: Sequence[float], right: Sequence[float]) -> float:
    if len(left) != len(right) or not left:
        raise ValueError("Embedding-Dimensionen stimmen nicht überein")
    product = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if not math.isfinite(product) or not left_norm or not right_norm:
        raise ValueError("Ungültiges Embedding")
    return product / (left_norm * right_norm)


def rank_passages(
    question: str,
    pages: Sequence[dict[str, Any]],
    embed_many: Callable[[list[str]], Iterable[Sequence[float]]],
    top_k: int = 5,
) -> list[dict[str, Any]]:
    question = question.strip()
    if not question:
        raise ValueError("Frage fehlt")
    if top_k < 1:
        raise ValueError("top_k muss positiv sein")
    candidates = passages(pages)
    if not candidates:
        return []
    vectors = [list(map(float, vector)) for vector in embed_many([question] + [item["passage"] for item in candidates])]
    if len(vectors) != len(candidates) + 1:
        raise ValueError("Embedding-Anzahl stimmt nicht überein")
    ranked = [
        {**item, "score": _cosine(vectors[0], vectors[index + 1])}
        for index, item in enumerate(candidates)
    ]
    ranked.sort(key=lambda item: item["score"], reverse=True)
    return ranked[:top_k]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()
    payload = json.load(sys.stdin)
    from fastembed import TextEmbedding

    model = TextEmbedding(args.model)
    result = rank_passages(
        str(payload.get("question") or ""),
        payload.get("pages") or [],
        model.embed,
        args.top_k,
    )
    json.dump(result, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
