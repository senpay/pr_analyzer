import os

import github
from github import Github

from pr_analyzer.application.model import PullRequest

g = Github(os.getenv('GITHUB_TOKEN'))


def get_prs(repository_url: str, closed=False) -> list:
    user, repository = _get_user_and_repository(repository_url)
    pulls = _get_closed_prs(user, repository, 'master') if closed else _get_prs(user, repository, 'master')
    prs = []
    for pull in pulls:
        pr = _convert_pull_request(pull)
        prs.append(pr)
    prs.sort(key=lambda x: x.created)
    return prs


def _get_prs(user, repository, base):
    return g.get_user(user).get_repo(repository).get_pulls(base=base)


def _get_closed_prs(user, repository, base):
    return g.get_user(user).get_repo(repository).get_pulls(base=base, state='closed')


def _convert_pull_request(pull: github.PullRequest) -> PullRequest:
    """
    Converts github.PullRequest to application.model.PullRequest

    :param pull: github.PullRequest
    :return: pr: application.model.PullRequest
    """
    pr = PullRequest()
    pr.created = pull.created_at
    pr.updated = pull.updated_at
    pr.merged = pull.merged_at
    pr.title = pull.title
    pr.author = pull.user
    pr.number = pull.number
    return pr


def _get_user_and_repository(repository_url: str) -> tuple:
    """
    Get User name and repository name from the given Github repository link

    >>> _get_user_and_repository('https://github.com/user/repository')
    ('user', 'repository')

    :param repository_url: string
    :return: (user: string, repository: string)
    """
    url_split = repository_url.split('/')
    return url_split[-2], url_split[-1]
