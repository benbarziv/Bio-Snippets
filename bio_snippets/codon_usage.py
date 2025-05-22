from typing import Dict


def codon_usage(sequence: str) -> Dict[str, int]:
    """Count codon usage for a given DNA sequence."""
    usage: Dict[str, int] = {}
    seq = sequence.upper()
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i : i + 3]
        if len(codon) == 3:
            usage[codon] = usage.get(codon, 0) + 1
    return usage