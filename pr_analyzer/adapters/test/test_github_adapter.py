from unittest.mock import MagicMock

from pr_analyzer.adapters.github_adapter import get_prs, _get_prs
from pr_analyzer.adapters import github_adapter


def test_get_prs():
    # Arrange
    github_adapter._get_prs = MagicMock(return_value=get_pulls())

    # Act
    actual_pulls = get_prs('adsad/user/repository')

    # Assert
    assert len(actual_pulls) == 1
    assert actual_pulls[0].created == 'created'
    assert actual_pulls[0].updated == 'updated'
    assert actual_pulls[0].merged == 'merged'
    assert actual_pulls[0].title == 'title'
    assert actual_pulls[0].author == 'author'
    assert actual_pulls[0].number == 'number'
    github_adapter._get_prs.assert_called_with('user', 'repository', 'master')


def test__get_prs():
    # Arrange
    github_adapter.g = MagicMock()
    get_pulls_mock = MagicMock()
    get_pulls_mock.get_pulls = MagicMock()
    get_repo_mock = MagicMock()
    get_repo_mock.get_repo = MagicMock(return_value=get_pulls_mock)
    github_adapter.g.get_user = MagicMock(return_value=get_repo_mock)

    # Act
    _get_prs('user', 'repo', 'base')

    # Assert
    github_adapter.g.get_user.assert_called_with('user')
    get_repo_mock.get_repo.assert_called_with('repo')
    get_pulls_mock.get_pulls.assert_called_with(base='base')


def get_pulls():
    pulls = []
    pull = MagicMock()

    pull.created_at = 'created'
    pull.updated_at = 'updated'
    pull.merged_at = 'merged'
    pull.title = 'title'
    pull.user = 'author'
    pull.number = 'number'

    pulls.append(pull)
    return pulls
