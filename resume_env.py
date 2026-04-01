from models import ResumeObservation, ResumeReward
from server.skill_matcher import match_skills
from server.scorer import calculate_score
from server.suggestion_engine import get_suggestions
from server.ats_checker import calculate_ats_score


class ResumeEnv:

    def __init__(self):
        self.state_data = None
        self.done = False

    def reset(self):

        self.state_data = ResumeObservation(
            job_description="",
            resume="",
            task="analyze resume",

            matched_skills=[],
            missing_skills=[],
            score=0.0,
            ats_score=0.0,
            suggestions=[]
        )

        self.done = False

        return self.state_data

    def step(self, action):

        if self.done:
            return self.state(), 0.0, True, "Episode already finished"

        matched, missing, similarity = match_skills(
            action.resume,
            action.job_description
        )

        score = calculate_score(matched, missing,similarity)

        ats_score = calculate_ats_score(action.resume)

        suggestions = get_suggestions(missing)

        reward = similarity / 100

        if similarity >= 80:
            self.done = True

        observation = ResumeObservation(
            job_description=action.job_description,
            resume=action.resume,
            task=action.action,

            matched_skills=matched,
            missing_skills=missing,
            score=score,
            ats_score=ats_score,
            suggestions=suggestions
        )

        info = "analysis completed"

        return observation, reward, self.done, info

    def state(self):
        return self.state_data