test = {
  'name': 'test_ses02_solution_sum_of_squares_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum_of_squares(100, 3)
          10009
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ses02 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
