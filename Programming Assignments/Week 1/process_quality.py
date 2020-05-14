def process_quality(q_list):

    score_list = []
    min_idx = []

    for q in q_list:
        score = []
        for letter in q:
            score.append(ord(letter))

        score_list.append(score)
        min_idx.append(score.index(min(score)))

    fault = max(set(min_idx), key=min_idx.count)
    return fault

        
