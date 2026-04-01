<<<<<<< HEAD
def calculate_score(matched, missing, similarity):

    skill_score = (len(matched) / (len(matched) + len(missing) + 1)) * 60

    similarity_score = similarity * 0.4

    total_score = skill_score + similarity_score

=======
def calculate_score(matched, missing, similarity):

    skill_score = (len(matched) / (len(matched) + len(missing) + 1)) * 60

    similarity_score = similarity * 0.4

    total_score = skill_score + similarity_score

>>>>>>> d89e674387131ac4a6df1aba512450ec1da38eb1
    return round(total_score, 2)