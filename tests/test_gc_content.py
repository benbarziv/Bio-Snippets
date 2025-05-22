import pytest
from bio_snippets.gc_content import gc_content

def test_gc_content_high_gc():
    assert pytest.approx(gc_content("GCGC")) == 100.0

def test_gc_content_low_gc():
    assert pytest.approx(gc_content("ATAT")) == 0.0

def test_gc_content_mid_gc():
    assert pytest.approx(gc_content("ATGC")) == 50.0

print("hello")