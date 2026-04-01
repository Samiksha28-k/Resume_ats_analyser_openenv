def grade_skill_matching(score):
    return score / 100

def grade_ats(ats):
    return ats / 100

def grade_hiring(score, ats):

    final = (score + ats) / 2

    return final / 100