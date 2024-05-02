import os
import requests
import re


token = os.environ['GITHUB_TOKEN']
repo = os.environ['GITHUB_REPOSITORY']
branch = os.environ['GITHUB_REF']
branch_name = branch.replace("refs/heads/", "")
repository_owner = os.environ['GITHUB_REPOSITORY_OWNER']
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}


def check_if_pull_request_exists():
    url = f'https://api.github.com/repos/{repo}/pulls'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pull_requests = response.json()
        for pr in pull_requests:
            if pr['head']['ref'] == branch_name:
                return True
    else:
        print(f"{response.status_code} - {response.text}")
        raise Exception("Failed to fetch pull requests.")


def create_pull_request():
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


def run():
    if check_if_pull_request_exists():
        print(f"There's already a pull request for the branch: {branch_name}. Skipping")
    else:
        create_pull_request()


if __name__ == "__main__":
    run()
