#!/usr/bin/python

import argparse

from pr_analyzer.application.pr_analyzer import get_prs_statistics, get_prs_leadtime_statistics
from pr_analyzer.common import print_info_message


def print_prs_statistics(url: str):
    prs_stats = get_prs_statistics(url)
    print(f'Open PRs count: {prs_stats[0]}, Closed PRs count: {prs_stats[1]}')


def print_prs_leadtime_statistics(url: str):
    prs_stats = get_prs_leadtime_statistics(url)
    print(f'Average time to closed: {prs_stats[0]} (minimum: {prs_stats[1]}, maximum: {prs_stats[2]})')


print_info_message()

parser = argparse.ArgumentParser(description='Prints statistics about pull requests activity for given repositories')
parser.add_argument('url', metavar='url', type=str, nargs='+',
                    help='repository url')

args = parser.parse_args()

for url in args.url:
    print(f'Statistics for the repository: {url}')
    print_prs_statistics(url)
    print_prs_leadtime_statistics(url)
