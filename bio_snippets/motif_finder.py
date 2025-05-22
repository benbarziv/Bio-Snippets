from typing import List


def find_motif(sequence: str, motif: str) -> List[int]:
    """Return 1-based start positions of motif occurrences in the sequence."""
    positions: List[int] = []
    start = 0
    while True:
        idx = sequence.find(motif, start)
        if idx == -1:
            break
        positions.append(idx + 1)
        start = idx + 1
    return positions