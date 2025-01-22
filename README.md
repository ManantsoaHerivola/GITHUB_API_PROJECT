# GitHub API Data Fetcher and Monitor

This project fetches and monitors repository metadata and commits from GitHub's public API, storing the data in a SQLite database. It supports continuous monitoring for updates at configurable intervals.

---

## Features

1. Fetch metadata of any GitHub repository (e.g., `chromium/chromium`).
2. Fetch and store commits, including:
   - Commit message
   - Author name
   - Date
   - URL
3. Avoid duplicate commits in the database.
4. Monitor repositories for updates every hour (default).
5. Start data collection from a specific date (configurable).

---

## Requirements

- Python 3.8+
- SQLite
- GitHub API Token with `public_repo` access

---

## Installation

1. Clone this repository

2.Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Configure the project in config.py:
- Add your GitHub Personal Access Token in config.py
- Set the repository name (by default, for the test, i set it to"chromium/chromium").

## Usage
1. Initialize the database and fetch initial data

## configuration
2. Create a `.env` file in the prject root
2. Add the folowing variables :
GITHUB_TOKEN=your_personal_access_token
3. Run the application : 
python main.py

2.The script will:
- Fetch repository metadata and commits.
- Start a scheduler to monitor changes every hour.

3.Testing
python -m unittest test_github_api.py
