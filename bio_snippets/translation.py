from Bio.Seq import Seq


def translate_sequence(sequence: str, table: str = "Standard") -> str:
    """Translate a DNA sequence to a protein sequence using Biopython."""
    seq = Seq(sequence)
    return str(seq.translate(table=table))