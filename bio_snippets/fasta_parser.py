from typing import Dict


def parse_fasta(fasta_str: str) -> Dict[str, str]:
    """Parses a FASTA formatted string into a dict of header to sequence."""
    sequences: Dict[str, str] = {}
    header = None
    seq_lines = []
    for line in fasta_str.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if header:
                sequences[header] = "".join(seq_lines)
            header = line[1:].split()[0]
            seq_lines = []
        else:
            seq_lines.append(line)
    if header:
        sequences[header] = "".join(seq_lines)
    return sequences