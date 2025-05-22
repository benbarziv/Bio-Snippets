def transcribe_sequence(sequence: str) -> str:
    """Transcribe a DNA sequence into RNA by replacing T with U."""
    return sequence.upper().replace('T', 'U')