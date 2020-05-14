from kmer_index import Index
from utils import readGenome

f = "chr1.GRCh38.excerpt.fasta"
t = readGenome(f)

def approx_match(p, t, k, tol):

    index = Index(t, k)
    n = int(len(p)/k)

    all_matches = set()
    total_hits = 0

    for i in range(n):
        start = k*i
        end = min(k*(i+1), len(p))
        hits = index.query(p[start:end])

        total_hits += len(hits)

        for h in hits:
            if h < start or h-start-len(p) > len(t):
                continue

            mismatches = 0

            for j in range(start):
                if p[j] != t[h - start + j]:
                    mismatches += 1
                    if mismatches > tol:
                        break
            for j in range(end, len(p)):
                if p[j] != t[h - start + j]:
                    mismatches += 1
                    if mismatches > tol:
                        break

            if mismatches <= tol:
                all_matches.add(h - start)

    return list(all_matches), total_hits 


p = "GGCGCGGTGGCTCACGCCTGTAAT"

matches, total_hits = approx_match(p, t, 8, 2)

print(len(matches))
print(total_hits)