import subprocess
import sys
import pytest

def get_ok_scores():
    """Run ok --score and parse output for individual test scores"""
    result = subprocess.run([sys.executable, 'ok', '--score'], capture_output=True, text=True)
    
    scores = []
    in_point_breakdown = False
    
    for line in result.stdout.split('\n'):
        # Skip empty lines
        if not line.strip():
            continue
            
        # Check if we're in the point breakdown section
        if line.strip() == "Point breakdown":
            in_point_breakdown = True
            continue
            
        # Only process lines in point breakdown section
        if not in_point_breakdown:
            continue
        
        # Match lines like "test_ses02_solution_print_grade_0: 0.0/1"
        parts = line.strip().split(': ')
        if len(parts) == 2:
            test_name = parts[0]
            score_parts = parts[1].split('/')
            if len(score_parts) == 2:
                score = float(score_parts[0])
                total = float(score_parts[1])
                scores.append((test_name, score, total))
    
    return scores


ALL_SCORES = get_ok_scores()

@pytest.mark.parametrize("test_name,score,total", ALL_SCORES)
def test_ok_score(test_name, score, total):
    """Test that each component received full points"""
    assert score == total, f"{test_name} received {score}/{total} points instead of full credit"