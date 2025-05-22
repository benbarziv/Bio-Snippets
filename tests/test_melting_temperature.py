from bio_snippets.melting_temp import melting_temperature


def test_melting_temperature_simple():
    assert melting_temperature("ATGC") == 12  # 2*(A+T=2) + 4*(G+C=2)
    assert melting_temperature("AAAA") == 8  # 2*(A+T=4)


def test_melting_temperature_case_insensitive():
    assert melting_temperature("atgc") == melting_temperature("ATGC")