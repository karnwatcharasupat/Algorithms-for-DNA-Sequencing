from kmer_index import SubseqIndex
from utils import readGenome

f = "chr1.GRCh38.excerpt.fasta"
t = readGenome(f)

def approx_match(p, t, k, tol, ival):

    index = SubseqIndex(t, k, ival)
    n = int(len(p)/k)

    all_matches = set()
    total_hits = 0
    span = index.span

    for i in range(len(p)-span+1):
        print(f'i = {i}')
        hits = index.query(p[i:])
        total_hits += len(hits)

        for h in hits:
            if h < i or h-i-len(p) > len(t):
                continue

            mismatches = 0

            for j in range(i):
                if p[j] != t[h - i + j]:
                    mismatches += 1
                    if mismatches > tol:
                        break
            for j in range(i + span, len(p)):
                if p[j] != t[h - i + j]:
                    mismatches += 1
                    if mismatches > tol:
                        break

            if mismatches <= tol:
                all_matches.add(h - i)

    return list(all_matches), total_hits 


p = "GGCGCGGTGGCTCACGCCTGTAAT"

matches, total_hits = approx_match(p, t, 8, 2, 3)

print(len(matches))
print(total_hits)