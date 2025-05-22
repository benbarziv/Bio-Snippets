def sequence_length(sequence: str) -> int:
    """Return the length of the DNA sequence, ignoring whitespace and newline characters."""
    cleaned = ''.join(sequence.split())
    return len(cleaned)