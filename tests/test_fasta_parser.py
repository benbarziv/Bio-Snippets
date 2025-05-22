from bio_snippets.fasta_parser import parse_fasta


def test_parse_fasta_single():
    fasta = ">seq1\nATGC"
    assert parse_fasta(fasta) == {"seq1": "ATGC"}


def test_parse_fasta_multiple():
    fasta = ">seq1\nATGC\n>seq2 description\nGATTACA"
    assert parse_fasta(fasta) == {"seq1": "ATGC", "seq2": "GATTACA"}