test = {
  'name': 'test_ses02_solution_print_grade_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> grade_high = 70 
          >>> grade_low = 50
          >>> print_grade(20, grade_high, grade_low)
          fail
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
