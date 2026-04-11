
def calculate_score(matched, missing, similarity):

    skill_score = (len(matched) / (len(matched) + len(missing) + 1)) * 60

    similarity_score = similarity * 0.4

    total_score = skill_score + similarity_score

def calculate_score(matched, missing, similarity):

    skill_score = (len(matched) / (len(matched) + len(missing) + 1)) * 60

    similarity_score = similarity * 0.4

    total_score = skill_score + similarity_score


    return round(total_score, 2)