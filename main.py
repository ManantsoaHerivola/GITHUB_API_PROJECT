from db_setup import initialize_db
from github_api import fetch_commits, fetch_repo_data
import scheduler
from config import DB_PATH, REPO_NAME

def main():
    """
    Main function to coordinate the GitHub API project.
    """
    # Initialize the database
    initialize_db(DB_PATH)

    # Fetch repository metadata
    print("Fetching repository metadata...")
    repo_data = fetch_repo_data(REPO_NAME)

    if repo_data:
        print(f"Successfully fetched metadata for repository: {repo_data['full_name']}")
    else:
        print(f"Failed to fetch metadata for repository: {REPO_NAME}. Check your configuration or network connection.")

    # Start the scheduler for periodic updates
    print("Starting scheduler for periodic updates...")
    scheduler.start_scheduler()

if __name__ == "__main__":
    main()