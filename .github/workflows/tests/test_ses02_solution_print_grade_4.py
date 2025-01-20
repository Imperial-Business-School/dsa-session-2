test = {
  'name': 'test_ses02_solution_print_grade_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print_grade(70, 70, 50)
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
