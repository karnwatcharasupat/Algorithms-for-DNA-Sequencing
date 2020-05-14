def naive_with_counts(p, t):
    occurrences = []
    n_alignment = 0
    n_char = 0
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        n_alignment += 1
        match = True
        for j in range(len(p)):  # loop over characters
            n_char += 1
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
               
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences, n_alignment, n_char