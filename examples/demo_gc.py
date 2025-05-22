from bio_snippets.gc_content import gc_content

if __name__ == "__main__":
    seq = "ATGCGCATTAAGCGC"
    gc = gc_content(seq)
    print(f"Sequence: {seq}")
    print(f"GC content: {gc:.2f}%")
