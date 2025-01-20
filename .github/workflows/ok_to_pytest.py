import subprocess
import sys

def run_ok_test(test_name):
    """Run ok --score and check the score for a specific test"""
    result = subprocess.run([sys.executable, 'ok', '--score'], capture_output=True, text=True)
    
    # Find score for specific test
    for line in result.stdout.split('\n'):
        if test_name in line and ': ' in line:
            score_part = line.split(': ')[1]
            actual_score, total_score = map(float, score_part.split('/'))
            assert actual_score == total_score, f"{test_name} received {actual_score}/{total_score} points instead of full credit"
            return
    
    # If we didn't find the test
    assert False, f"Could not find score for {test_name}"

def test_print_grade_0():
    run_ok_test("test_ses02_solution_print_grade_0")

def test_print_grade_1():
    run_ok_test("test_ses02_solution_print_grade_1")

def test_print_grade_2():
    run_ok_test("test_ses02_solution_print_grade_2")

def test_sum_of_squares_0():
    run_ok_test("test_ses02_solution_sum_of_squares_0")

def test_sum_of_squares_1():
    run_ok_test("test_ses02_solution_sum_of_squares_1")

def test_sum_of_squares_2():
    run_ok_test("test_ses02_solution_sum_of_squares_2")

def test_sum_of_squares_3():
    run_ok_test("test_ses02_solution_sum_of_squares_3")

def test_weeks_0():
    run_ok_test("test_ses02_solution_weeks_0")

def test_weeks_1():
    run_ok_test("test_ses02_solution_weeks_1")

def test_weeks_2():
    run_ok_test("test_ses02_solution_weeks_2")

def test_weeks_3():
    run_ok_test("test_ses02_solution_weeks_3")