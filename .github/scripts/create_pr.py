import os
import requests
import re


def get_repository_owner():
    repo_url = os.environ['GITHUB_REPOSITORY']
    owner_match = re.match(r'.*/(.+)$', repo_url)
    if owner_match:
        return owner_match.group(1)
    else:
        raise ValueError("Unable to determine repository owner from the repository URL")


def create_pull_request():
    token = os.environ['GITHUB_TOKEN']
    repo = os.environ['GITHUB_REPOSITORY']
    branch = os.environ['GITHUB_REF']
    branch_name = branch.split('/')[-1]
    repository_owner = get_repository_owner()

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    payload = {
        'title': f'Pull request from {branch_name} to develop',
        'head': f'{repository_owner}:{branch_name}',  # Updated head parameter
        'base': 'develop'
    }

    url = f'https://api.github.com/repos/{repo}/pulls'

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Pull request created successfully!")
    else:
        print("Failed to create pull request.")
        print(response.text)


if __name__ == "__main__":
    create_pull_request()
