import unittest
from unittest.mock import patch
from github_api import fetch_commits

class TestGitHubAPI(unittest.TestCase):
    @patch("github_api.requests.get")
    def test_fetch_commits(self, mock_get):
        """
        Test fetch_commits to ensure it fetches data correctly from GitHub API.
        """
        # Mock the API response
        mock_response = {
            "commit": {
                "message": "Initial commit",
                "author": {"name": "AuthorName", "date": "2022-01-01T00:00:00Z"}
            },
            "html_url": "https://github.com/chromium/chromium/commit/123456"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [mock_response]

        # Call the function
        repo_name = "chromium/chromium"
        commits = fetch_commits(repo_name, "2022-01-01T00:00:00Z")

        # Assertions
        self.assertIsNotNone(commits)
        self.assertEqual(len(commits), 1)
        self.assertEqual(commits[0]["commit"]["message"], "Initial commit")
        self.assertEqual(commits[0]["commit"]["author"]["name"], "AuthorName")

if __name__ == "__main__":
    unittest.main()
