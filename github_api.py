import requests
import config

def fetch_repo_data(repo_name):
    """
    Fetch repository metadata from the GitHub API.

    Args:
        repo_name (str): The name of the repository in the format 'owner/repo'.

    Returns:
        dict: JSON response containing repository details, or None if an error occurs.
    """
    url = f"{config.GITHUB_API_URL}/repos/{repo_name}"
    headers = {"Authorization": f"token {config.GITHUB_TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching repository data for {repo_name}: {e}")
        return None

def fetch_commits(repo_name, since_date=None):
    """
    Fetch commits from a GitHub repository.

    Args:
        repo_name (str): The name of the repository in the format 'owner/repo'.
        since_date (str, optional): ISO date to fetch commits since. Defaults to None.

    Returns:
        list: List of commits in JSON format, or None if an error occurs.
    """
    url = f"{config.GITHUB_API_URL}/repos/{repo_name}/commits"
    headers = {"Authorization": f"token {config.GITHUB_TOKEN}"}
    params = {"since": since_date} if since_date else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching commits for {repo_name}: {e}")
        return None