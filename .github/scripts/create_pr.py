import os
import sys
import requests


token = os.environ['GITHUB_TOKEN']
repo = os.environ['GITHUB_REPOSITORY']
branch = os.environ['GITHUB_REF']
source_branch = branch.replace("refs/heads/", "")
repository_owner = os.environ['GITHUB_REPOSITORY_OWNER']
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}
target_branch = sys.argv[1]


def check_if_pull_request_exists():
    url = f'https://api.github.com/repos/{repo}/pulls'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pull_requests = response.json()
        for pr in pull_requests:
            if pr['head']['ref'] == source_branch:
                return True
    else:
        print(f"{response.status_code} - {response.text}")
        raise Exception("Failed to fetch pull requests.")


def create_pull_request():
    payload = {
        'title': f'Pull request from {source_branch} to {target_branch}',
        'head': f'{repository_owner}:{source_branch}',
        'base': target_branch
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
        print(f"There's already a pull request from {source_branch} to {target_branch}. Skipping...")
    else:
        create_pull_request()


if __name__ == "__main__":
    run()
