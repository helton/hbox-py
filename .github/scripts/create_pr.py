import os
import requests
import re


def create_pull_request():
    token = os.environ['GITHUB_TOKEN']
    repo = os.environ['GITHUB_REPOSITORY']
    branch = os.environ['GITHUB_REF']
    branch_name = branch.replace("refs/heads/", "")
    repository_owner = os.environ['GITHUB_REPOSITORY_OWNER']

    print(f"repo={repo}")
    print(f"branch={branch}")
    print(f"branch_name={branch_name}")
    print(f"repository_owner={repository_owner}")

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    payload = {
        'title': f'Pull request from {branch_name} to develop',
        'head': f'{repository_owner}:{branch_name}',
        'base': 'develop'
    }

    url = f'https://api.github.com/repos/{repo}/pulls'

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Pull request created successfully!")
    else:
        print(f"{response.status_code} - {response.text}")
        raise Exception("Failed to create pull request")


if __name__ == "__main__":
    create_pull_request()
