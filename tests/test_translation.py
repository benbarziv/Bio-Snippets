from bio_snippets.translation import translate_sequence


def test_translation_simple():
    assert translate_sequence('ATGGCC') == 'MA'