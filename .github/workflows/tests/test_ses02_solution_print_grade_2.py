test = {
  'name': 'test_ses02_solution_print_grade_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print_grade(90, 80, 60)
          distinction
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
