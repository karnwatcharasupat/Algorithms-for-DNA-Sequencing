def naive_mm(p, t, n):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        mismatches = 0
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                mismatches += 1
            
            if mismatches > n:
                match = False
                break

        if match:
            occurrences.append(i)  # all chars matched; record

    return occurrences

def naive_2mm(p, t):
    return naive_mm(p, t, 2)