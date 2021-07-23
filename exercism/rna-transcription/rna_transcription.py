def to_rna(dna_strand):

  dnatorna = {"G": "C",
              "C": "G",
              "T": "A",
              "A": "U",
              "": "",
  }

  return ''.join(dnatorna[a] for a in dna_strand)
