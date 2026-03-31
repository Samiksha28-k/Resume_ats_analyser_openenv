import os
from openai import OpenAI
from server.resume_env import ResumeEnv
from models import ResumeAction
from dotenv import load_dotenv

# load env from root
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check .env file")

client = OpenAI(api_key=api_key)

env = ResumeEnv()

obs = env.reset()

action = ResumeAction(
    action="analyze",
    resume="python fastapi machine learning pandas sql projects experience",
    job_description="python fastapi sql machine learning"
)

obs, reward, done, info = env.step(action)

print("Observation:", obs)
print("Reward:", reward)
print("Done:", done)
print("Info:", info)