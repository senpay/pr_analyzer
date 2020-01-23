from datetime import datetime, timezone

from pr_analyzer.application.model import PullRequest


def test_pr_helper_repr():
    pr = PullRequest()
    pr.number = 1
    pr.title = 'title'
    pr.created = datetime(1970, 1, 1, tzinfo=timezone.utc)
    pr.updated = datetime(1971, 1, 1, tzinfo=timezone.utc)

    assert pr.__repr__() == '1 "title": created 1970-01-01 00:00:00+00:00, updated 1971-01-01 00:00:00+00:00'
    assert pr.__str__() == pr.__repr__()
