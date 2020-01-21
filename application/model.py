class PullRequest:
    """
    PullRequest class represents a PR entity withing the repository.

    Currently we're interested only in the following PR-related data:
    - Date when PR was opened
    - Date when PR was updated
    - Date when PR was merged
    - PR reviewer's emails
    - PR author
    - PR title
    - PR number
    """
    def __repr__(self) -> str:
        return f'{self.number} "{self.title}": created {self.created}, updated {self.updated}'

    def __str__(self) -> str:
        return self.__repr__()
