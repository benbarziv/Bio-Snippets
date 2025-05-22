from typing import List


def find_restriction_sites(sequence: str, site: str) -> List[int]:
    """Return 1-based start positions of a restriction site in the sequence."""
    seq_up = sequence.upper()
    site_up = site.upper()
    positions: List[int] = []
    start = 0
    while True:
        idx = seq_up.find(site_up, start)
        if idx == -1:
            break
        positions.append(idx + 1)
        start = idx + 1
    return positions