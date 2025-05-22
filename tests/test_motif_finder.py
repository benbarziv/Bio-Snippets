from bio_snippets.motif_finder import find_motif


def test_find_motif_no_occurrence():
    assert find_motif("ATGCGC", "TT") == []


def test_find_motif_single():
    assert find_motif("ATGCGC", "GC") == [3, 5]


def test_find_motif_overlapping():
    assert find_motif("AAAAA", "AA") == [1, 2, 3, 4]