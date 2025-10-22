from __future__ import annotations

# Target difficulty labels are validated by rating after generation.
PRESETS: dict[str, tuple[int, int]] = {
    # value: (min clues, max clues) as a soft guide; rating decides final label
    "Beginner": (36, 45),
    "Easy": (32, 40),
    "Medium": (28, 36),
    "Hard": (24, 32),
    "Expert": (17, 28),
}
