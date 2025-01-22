import schedule
import time
from github_api import fetch_commits, fetch_repo_data
from db_setup import create_connection
from config import DB_PATH, REPO_NAME, START_DATE

def update_commits():
    """
    Fetch new commits for the repository and update the database.
    """
    connection = create_connection(DB_PATH)
    if connection:
        repo_data = fetch_repo_data(REPO_NAME)
        if repo_data:
            print("Updating repository metadata...")
            cursor = connection.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO repositories (name, description, url, language, forks, stars, open_issues, watchers, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                repo_data["full_name"], repo_data.get("description"), repo_data.get("html_url"),
                repo_data.get("language"), repo_data.get("forks"), repo_data.get("stargazers_count"),
                repo_data.get("open_issues"), repo_data.get("watchers"), repo_data.get("created_at"),
                repo_data.get("updated_at")
            ))
            connection.commit()

            print("Fetching new commits...")
            commits = fetch_commits(REPO_NAME, START_DATE)
            if commits:
                for commit in commits:
                    cursor.execute("""
                        INSERT OR IGNORE INTO commits (commit_message, author, date, url, repo_id)
                        VALUES (?, ?, ?, ?, ?)
                    """, (
                        commit["commit"]["message"],
                        commit["commit"]["author"].get("name"),
                        commit["commit"]["author"].get("date"),
                        commit.get("html_url"),
                        repo_data["id"]
                    ))
                connection.commit()
                print(f"{len(commits)} commits updated.")
        connection.close()

def start_scheduler():
    """
    Start the scheduler to periodically update repository data.
    """
    schedule.every(3600).seconds.do(update_commits)
    while True:
        schedule.run_pending()
        time.sleep(1)