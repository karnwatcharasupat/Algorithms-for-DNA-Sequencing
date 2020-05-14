from overlap import overlap
from kmer_index import Index
from collections import defaultdict

# https://github.com/sidsriv/Algorithms-for-DNA-sequencing/blob/master/homework-3.ipynb

def overlap_graph(reads, k=30):
    index = defaultdict(set)

    for read in reads:
        for i in range(len(read) - k + 1):
            index[read[i:i+k]].add(read)

    graph = defaultdict(set)

    for r in reads:
        for o in index[r[-k:]]:
            if r != o:
                if overlap(r, o, k):
                    graph[r].add(o)

    edges = 0
    for read in graph:
        edges += len(graph[read])
        
    return edges, len(graph)

    














    for k in range(min_len, len(reads[0])):
        pass
