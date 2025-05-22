from bio_snippets.seq_length import sequence_length


def test_sequence_length_simple():
    assert sequence_length("ATGC") == 4


def test_sequence_length_empty():
    assert sequence_length("") == 0


def test_sequence_length_with_whitespace():
    assert sequence_length(" A T G C\n") == 4