from datetime import datetime, timedelta
from unittest import mock
from unittest.mock import MagicMock

from pr_analyzer.application import pr_analyzer
from pr_analyzer.application.model import PullRequest
from pr_analyzer.application.pr_analyzer import _get_lead_time, get_prs_statistics, get_open_prs, \
    get_prs_leadtime_statistics


def test_get_open_prs():
    # Arrange
    pr_analyzer.get_prs = MagicMock()
    expected_prs = get_pulls([1, 2, 3], [1, 2, 3], [1, 2, 3])

    pr_analyzer.get_prs.side_effect = [expected_prs]

    # Act
    result = get_open_prs('/user/repository')

    # Assert
    assert len(result) == 3
    assert expected_prs == result


def test_get_open_prs_with_created():
    # Arrange
    pr_analyzer.get_prs = MagicMock()
    created_1 = datetime.now() + timedelta(days=-3)
    created_2 = datetime.now() + timedelta(days=-2)
    pr_analyzer.get_prs.side_effect = [get_pulls([created_1,
                                                  created_2,
                                                  datetime.now() + timedelta(days=-1)],
                                                 [1, 2, 3],
                                                 [1, 2, 3])]

    # Act
    result = get_open_prs('/user/repository', created=2)

    # Assert
    assert len(result) == 2
    assert result[0].created == created_1
    assert result[1].created == created_2


def test_get_open_prs_with_updated():
    # Arrange
    pr_analyzer.get_prs = MagicMock()
    updated_1 = datetime.now() + timedelta(days=-3)
    updated_2 = datetime.now() + timedelta(days=-2)
    pr_analyzer.get_prs.side_effect = [get_pulls([1, 2, 3],
                                                 [updated_1,
                                                  updated_2,
                                                  datetime.now() + timedelta(days=-1)],
                                                 [1, 2, 3])]

    # Act
    result = get_open_prs('/user/repository', updated=2)

    # Assert
    assert len(result) == 2
    assert result[0].updated == updated_1
    assert result[1].updated == updated_2


def test__get_prs_statistics():
    # Arrange
    pr_analyzer.get_prs = MagicMock()
    pr_mock = MagicMock()
    pr_mock.merged = True
    pr_mock_not_merged = MagicMock()
    pr_mock_not_merged.merged = False
    pr_analyzer.get_prs.side_effect = [[pr_mock, pr_mock, pr_mock_not_merged], [pr_mock, pr_mock]]

    # Act
    result = get_prs_statistics('/user/repository')

    # Assert
    assert result == (2, 2, 1)
    calls = [mock.call('/user/repository', closed=True), mock.call('/user/repository')]
    pr_analyzer.get_prs.assert_has_calls(calls)


def test_get_prs_leadtime_statistics():
    # Arrange
    pr_analyzer.get_prs = MagicMock()
    pr_mock = MagicMock()
    pr_mock.merged = True
    result_list = [pr_mock, pr_mock, pr_mock]
    pr_analyzer.get_prs.side_effect = [result_list]
    pr_analyzer._get_lead_time = MagicMock()
    pr_analyzer._get_lead_time.side_effect = [1, 2, 10]

    # Act
    result = get_prs_leadtime_statistics('/user/repository')

    # Assert
    assert result == tuple([timedelta(seconds=res) for res in (4, 1, 10)])


def test__get_lead_time() -> int:
    pr = PullRequest()
    pr.merged = datetime.fromordinal(2) + timedelta(seconds=531)
    pr.created = datetime.fromordinal(1)
    # Should be number of seconds in day  + timedelta (531 seconds)
    assert 86931 == _get_lead_time(pr)


def get_pulls(created: list, updated: list, merged: list):
    pulls = []

    for i in range(len(created)):
        pull = MagicMock()

        pull.created = created[i]
        pull.updated = updated[i]
        pull.merged = merged[i]

        pulls.append(pull)
    return pulls
