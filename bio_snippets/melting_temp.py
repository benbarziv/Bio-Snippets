def melting_temperature(sequence: str) -> float:
    """Calculate melting temperature of a DNA sequence using the Wallace rule: Tm = 2°C*(A+T) + 4°C*(G+C)."""
    seq = sequence.upper()
    at = seq.count('A') + seq.count('T')
    gc = seq.count('G') + seq.count('C')
    return 2 * at + 4 * gc