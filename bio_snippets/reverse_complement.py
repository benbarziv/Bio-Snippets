from Bio.Seq import Seq


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    return str(Seq(sequence).reverse_complement())