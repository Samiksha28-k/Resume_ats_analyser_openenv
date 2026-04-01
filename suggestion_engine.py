<<<<<<< HEAD
def get_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        if skill == "docker":
            suggestions.append("Learn Docker for deployment")

        elif skill == "python":
            suggestions.append("Improve Python programming")

        elif skill == "fastapi":
            suggestions.append("Learn FastAPI for backend development")

        elif skill == "sql":
            suggestions.append("Learn SQL for database")

        elif skill == "machine":
            suggestions.append("Learn Machine Learning basics")

        elif skill == "deep":
            suggestions.append("Learn Deep Learning")

        elif skill == "api":
            suggestions.append("Understand API development")

        else:
            suggestions.append(f"Try learning {skill}")

=======
def get_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        if skill == "docker":
            suggestions.append("Learn Docker for deployment")

        elif skill == "python":
            suggestions.append("Improve Python programming")

        elif skill == "fastapi":
            suggestions.append("Learn FastAPI for backend development")

        elif skill == "sql":
            suggestions.append("Learn SQL for database")

        elif skill == "machine":
            suggestions.append("Learn Machine Learning basics")

        elif skill == "deep":
            suggestions.append("Learn Deep Learning")

        elif skill == "api":
            suggestions.append("Understand API development")

        else:
            suggestions.append(f"Try learning {skill}")

>>>>>>> d89e674387131ac4a6df1aba512450ec1da38eb1
    return suggestions