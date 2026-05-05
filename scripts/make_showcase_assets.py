#!/usr/bin/env python3
"""Generate simple PNG showcase assets for the README."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str | None = None) -> None:
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=outline, width=2 if outline else 1)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    lines: list[str] = []
    for para in text.split("\n"):
        words = para.split()
        current = ""
        for word in words:
            probe = word if not current else f"{current} {word}"
            if draw.textbbox((0, 0), probe, font=fnt)[2] <= width:
                current = probe
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        if not words:
            lines.append("")
    return lines


def draw_text_block(draw: ImageDraw.ImageDraw, x: int, y: int, width: int, title: str, body: str) -> int:
    title_font = font(28, True)
    body_font = font(19)
    draw.text((x, y), title, fill="#111827", font=title_font)
    y += 44
    for line in wrap(draw, body, body_font, width):
        draw.text((x, y), line, fill="#374151", font=body_font)
        y += 28
    return y


def make_overview() -> None:
    img = Image.new("RGB", (1400, 850), "#f8fafc")
    draw = ImageDraw.Draw(img)
    title_font = font(48, True)
    subtitle_font = font(24)
    label_font = font(22, True)
    small_font = font(18)

    draw.text((70, 55), "Paper Review Skills For Agents", fill="#0f172a", font=title_font)
    draw.text(
        (72, 120),
        "Portable workflows for paper review, data audits, rebuttals, artifacts, and camera-ready polish.",
        fill="#475569",
        font=subtitle_font,
    )

    cards = [
        ("Full Review", "Central claims, reviewer attacks, score, and revision plan.", "#dbeafe"),
        ("Data Audit", "Tables, metrics, configs, arithmetic, and external plausibility.", "#dcfce7"),
        ("Rebuttal", "Reviewer belief map, issue triage, evidence plan, and draft.", "#fef3c7"),
        ("Artifact Audit", "Runnable boundary, anonymity, release hygiene, and traceability.", "#fee2e2"),
        ("Camera Ready", "Final consistency, checklist, captions, bibliography, upload risks.", "#ede9fe"),
    ]
    x0, y0 = 70, 220
    for i, (name, desc, color) in enumerate(cards):
        x = x0 + (i % 3) * 430
        y = y0 + (i // 3) * 215
        rounded(draw, (x, y, x + 385, y + 150), "#ffffff", "#cbd5e1")
        draw.rounded_rectangle((x + 24, y + 24, x + 84, y + 84), radius=14, fill=color)
        draw.text((x + 105, y + 27), name, fill="#111827", font=label_font)
        for n, line in enumerate(wrap(draw, desc, small_font, 240)[:3]):
            draw.text((x + 105, y + 65 + n * 25), line, fill="#475569", font=small_font)

    rounded(draw, (70, 670, 1330, 780), "#0f172a")
    draw.text((105, 705), "Works in Codex natively, and in ChatGPT / Claude / Cursor-style agents through adapters + prompts.", fill="#f8fafc", font=subtitle_font)

    OUT.mkdir(exist_ok=True)
    img.save(OUT / "showcase-overview.png")


def make_case_study() -> None:
    img = Image.new("RGB", (1400, 980), "#ffffff")
    draw = ImageDraw.Draw(img)
    title_font = font(42, True)
    draw.text((70, 55), "Anonymous Case Study Output", fill="#111827", font=title_font)

    rounded(draw, (70, 135, 655, 880), "#f8fafc", "#cbd5e1")
    rounded(draw, (745, 135, 1330, 880), "#f8fafc", "#cbd5e1")

    left = (
        "Verdict: borderline reject to weak reject, medium confidence.\n\n"
        "P0: Algorithm 1 enforces a count-style budget, while Table 2 is framed as a retained-token budget. "
        "Without a mapping between chunks and tokens, the comparison may not be capacity-matched.\n\n"
        "P1: The overhead claim is under-supported without timing protocol, hardware, precision, and batch settings."
    )
    right = (
        "Artifact verdict: not ready for anonymous submission.\n\n"
        "P0: .env contains an API credential. This is both a security issue and a submission-risk issue.\n\n"
        "Rebuttal note: prioritize the budget-definition concern first, concede ambiguity, and avoid claiming new full benchmarks."
    )

    draw_text_block(draw, 105, 175, 500, "Case 1: Paper Review", left)
    draw_text_block(draw, 780, 175, 500, "Case 2: Artifact + Rebuttal", right)

    OUT.mkdir(exist_ok=True)
    img.save(OUT / "case-study-output.png")


def main() -> int:
    make_overview()
    make_case_study()
    print(f"Wrote assets to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
