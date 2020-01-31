# PR Analyzer
Imagine that you work on a project, and your Pull Requests don't get reviewed fast enough. Is it just that odds were
against you, or in this project Pull Requests are usually not reviewed in a timely fashion?

PR Analyzer is a small set of command line utilities for analyzing Pull Requests in the GitHub, and it should help you
to find an answer for the question above.

Using **PR Analyzer** you will be able:
  -  Find out the list of open pull requests
  -  Get the statistics about lead time, time before a first comment for the Pull Requests in the repo
  -  Generate some nice reports from this statistics, or export this into other systems
  
***Note:*** Please be aware that the tool is currently under active development.

# Installation
You can install pr_analyzer using pip:
```bash
$ pip install pr-analyzer
```

GitHub token is required for the pr_analyzer to be able to use GitHub API:
```bash
$ set GITHUB_TOKEN=your_token_value
```


# Available commands
## list_prs

```bash
usage: $python list_prs.py [-h] [--created [created]] [--updated [updated]]
                           [--top [top]]
                           url [url ...]

Prints list of open pull requests for given repositories

positional arguments:
  url                  repository url

optional arguments:
  -h, --help           show this help message and exit
  --created [created]  If given - will show PRs created more than `created` days ago
  --updated [updated]  If given - will show PRs updated more than `updated` days ago
  --top [top]          If given - returns up to `top` PRs starting from the oldest
```

## print_stats
```bash
Prints statistics about pull requests activity for given repositories

positional arguments:
  url         repository url

optional arguments:
  -h, --help  show this help message and exit

```
![GitHub CI](https://github.com/senpay/pr_analyzer/workflows/ci/badge.svg)
  
 
[![Azure Pipeline](https://apushkarev.visualstudio.com/pr%20analyzer/_apis/build/status/Alex%20Pushkarev%20CI-Python%20package-CI)](https://apushkarev.visualstudio.com/pr%20analyzer/_build/latest?definitionId=2)

![](https://img.shields.io/pypi/dm/pr-analyzer.svg)
