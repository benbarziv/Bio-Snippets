from bio_snippets.transcription import transcribe_sequence


def test_transcription_simple():
    assert transcribe_sequence('ATGC') == 'AUGC'
    assert transcribe_sequence('atgc') == 'AUGC'