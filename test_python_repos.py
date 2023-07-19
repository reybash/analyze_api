import unittest

from python_repos_visual import get_status_code


class Python_Repos_TestCase(unittest.TestCase):
    def test_get_status_code(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}

        self.assertEqual('200', str(get_status_code(headers, url)))


if __name__ == '__main__':
    unittest.main()
