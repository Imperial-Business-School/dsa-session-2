test = {
  'name': 'test_ses02_solution_sum_of_squares_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = sum_of_squares(2, 3)
          >>> x + 1
          14
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
