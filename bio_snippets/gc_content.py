from Bio.Seq import Seq

def gc_content(sequence: str) -> float:
    """Calculate the GC content of a DNA sequence."""
    seq = Seq(sequence)
    return float(seq.count('G') + seq.count('C')) / len(seq) * 100