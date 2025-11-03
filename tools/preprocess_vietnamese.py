#!/usr/bin/env python3
"""
Convenience wrapper that delegates to `preprocess_data.py` with the same CLI.
Kept for quick access when working on the Vietnamese pipeline.
"""

from preprocess_data import main as preprocess_main


def main() -> None:
    preprocess_main()


if __name__ == "__main__":
    main()
