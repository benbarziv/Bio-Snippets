# Bio script Snippets





A lightweight Python package of reusable bioinformatics utilities built on bio. Designed to simplify common sequence analyses with a consistent, test-driven API.

## Included Snippets

* **GC Content**: Calculate the GC percentage of a DNA sequence.
* **Reverse Complement**: Generate the reverse complement of a sequence.
* **Motif Finder**: Locate all occurrences of a motif in a sequence.
* **FASTA Parser**: Parse FASTA-formatted strings into Python dictionaries.
* **Codon Usage**: Compute codon frequencies from a coding sequence.
* **Melting Temperature**: Estimate primer melting temperature via the Wallace rule.
* **Sequence Length**: Compute sequence length, ignoring whitespace.
* **Transcription**: Transcribe a DNA sequence into RNA by replacing thymine (T) with uracil (U).
* **Translation**: Translate a DNA sequence into a protein sequence using the standard genetic code.
* **Restriction Site Finder**: Identify all occurrences of a restriction enzyme recognition site in a sequence.


## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Examples](#examples)
* [Development](#development)


## Installation

Install from PyPI:

```bash
pip install bio_snippets
```

Or clone and install from source:

```bash
git clone https://github.com/benbarziv/bio_snippets.git
cd bio_snippets
pip install -r requirements.txt
pip install -e .
```

## Usage

### GC Content

```python
from bio_snippets.gc_content import gc_content

print(gc_content("GATTACA"))  # 28.57
```

### Reverse Complement

```python
from bio_snippets.reverse_complement import reverse_complement

print(reverse_complement("ATGC"))  # GCAT
```

### Motif Finder

```python
from bio_snippets.motif_finder import find_motif

print(find_motif("GCGCGC", "GC"))  # [1, 3, 5]
```


## Development

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv && source venv/bin/activate
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Link in editable mode:

   ```bash
   pip install -e .
   ```
4. Run tests:

   ```bash
   pytest -q
   ```


