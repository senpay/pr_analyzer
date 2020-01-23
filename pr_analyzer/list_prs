#!/usr/bin/python3

import argparse

from pr_analyzer.application.pr_analyzer import get_open_prs
from pr_analyzer.common import print_info_message

print_info_message()

parser = argparse.ArgumentParser(description='Prints list of open pull requests for given repositories')
parser.add_argument('url', metavar='url', type=str, nargs='+',
                    help='repository url')
parser.add_argument('--created', metavar='created', type=int, nargs='?',
                    help='If given - will show PRs created more than `created` days ago')
parser.add_argument('--updated', metavar='updated', type=int, nargs='?',
                    help='If given - will show PRs updated more than `updated` days ago')
parser.add_argument('--top', metavar='top', type=int, nargs='?',
                    help='If given - returns up to `top` PRs starting from the oldest')

args = parser.parse_args()

for url in args.url:
    print(f'List PRs for the repository: {url}')
    prs = get_open_prs(url, args.created, args.updated)
    if args.top and args.top < len(prs):
        prs = prs[:args.top]
    if prs:
        print(f'Number of open PRs: {len(prs)}')
        for pr in prs:
            print(pr)
    else:
        print('No open PRs found!')
    print()
