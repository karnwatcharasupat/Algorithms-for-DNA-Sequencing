
from naive_with_counts import naive_with_counts
from bm_with_counts import boyer_moore_with_counts
from utils import readGenome
from bm_preproc import BoyerMoore

f = "chr1.GRCh38.excerpt.fasta"
t = readGenome(f)


p1 = "GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG"
_, n_align_naive, n_char_naive = naive_with_counts(p1, t)

print(f'Q1: {n_align_naive}')
print(f'Q2: {n_char_naive}')

p_bm = BoyerMoore(p1, 'ACGT')

_, n_align_bm, _ = boyer_moore_with_counts(p1, p_bm, t)

print(f'Q3: {n_align_bm}')
