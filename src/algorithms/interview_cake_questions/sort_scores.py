def sort_scores(scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score + 1)
    sorted_scores = []

    for score in scores:
        score_counts[score] += 1

    for score_index in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score_index]

        for _ in range(count):
            sorted_scores.append(score_index)

    return sorted_scores
