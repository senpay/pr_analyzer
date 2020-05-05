from datetime import timedelta, datetime
from statistics import mean

from pr_analyzer.adapters.github_adapter import get_prs
from pr_analyzer.application.model import PullRequest


def get_open_prs(repository_url: str, created: int = None, updated: int = None) -> list:
    """
    Returns list of open PRs in the repository

    :param repository_url: str - repository url
    :param created: int - if given - filters out PRs created less than -{created} days ago
    :param updated: int - if given - filters out PRs updated less than -{updated} days ago
    :return: list of string PRs representation
    """
    prs = get_prs(repository_url)
    if created:
        prs = [pr for pr in prs if pr.created < (datetime.now() + timedelta(days=-created))]
    if updated:
        prs = [pr for pr in prs if pr.updated < (datetime.now() + timedelta(days=-updated))]

    return prs


def get_prs_leadtime_statistics(repository_url: str) -> tuple:
    """
    Returns lead-time statistics tuple

    :param repository_url: str - repository url
    :return:
    """
    # TODO: Test case is needed here
    prs = get_prs(repository_url, closed=True)
    pr_lead_times = [_get_lead_time(pr) for pr in prs if pr.merged]

    result_tuple = int(mean(pr_lead_times)), min(pr_lead_times), max(pr_lead_times)
    return tuple([timedelta(seconds=res) for res in result_tuple])


def get_prs_statistics(repository_url: str) -> list:
    """
    Returns tuple with the number of open and closed(merged) and closed(not merged) PRs in the repository

    :param repository_url: str - repository url
    :return: number_of_open_prs, number_of_merged_prs, number_of_refused_prs
    """
    closed_prs = get_prs(repository_url, closed=True)
    merged_prs = [pr for pr in closed_prs if pr.merged]
    not_merged_prs = [pr for pr in closed_prs if not pr.merged]
    open_prs = get_prs(repository_url)

    return len(open_prs), len(merged_prs), len(not_merged_prs)


def _get_lead_time(pr: PullRequest) -> timedelta:
    lead_timedelta = pr.merged - pr.created
    return lead_timedelta.days * 86400 + lead_timedelta.seconds
