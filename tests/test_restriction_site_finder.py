from bio_snippets.restriction_site_finder import find_restriction_sites


def test_restriction_sites_simple():
    assert find_restriction_sites('AAGCTTAAGCTT', 'AAGCTT') == [1, 7]
    assert find_restriction_sites('AAA', 'TTT') == []