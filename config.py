from dotenv import load_dotenv 
import os
load_dotenv()

GITHUB_API_URL = "https://api.github.com"
REPO_NAME = "chromium/chromium"
DB_PATH = "repositories.db"
PER_PAGE = 100  # Number of results per page
POLLING_INTERVAL = 3600  # 1 hour in seconds
START_DATE = "2022-01-01T00:00:00Z"  # ISO date format for commits
#GITHUB_TOKEN = os.getenv("")  #please, uncomment this line and complete with your personal GitHub token 
if not GITHUB_TOKEN:
  raise ValueError("Missing GITHUB_TOKEN in environment variables.")