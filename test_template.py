import sys
import os
import json
import hashlib
import atexit

# ============================ DO NOT MODIFY ============================
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'odgovori.json'))
def hash_answer(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()
def write_grade_summary():
    # Calculate scores and write the grade summary (this assumes all tests have the same weight)
    results["total_score"] = sum(results.values())
    results["max_score"] = len([k for k in results if isinstance(results[k], bool)])
    results["passed_tests"] = sum(results.values())
    results["total_tests"] = len([k for k in results if isinstance(results[k], bool)])
    try:
        with open("grade_summary.json", "w") as f:
            json.dump(results, f, indent=2, sort_keys=True)
    except Exception as e:
        print(f"Failed to write grade summary: {e}")

@atexit.register
def write_fallback_summary():
    write_grade_summary()

def pytest_sessionfinish(session, exitstatus):
    write_grade_summary()
# END OF DO NOT MODIFY THIS PART

# Import the student's code
from student_code import square, is_even

# Prepare grading dictionary
results = {
    "square": False,
    "is_even": False,
    "q1": False,
    "q2": False
}

# Test and record outcomes manually
def test_square():
    try:
        assert square(2) == 4
        assert square(3) == 9
        assert square(-1) == 1
        results["square"] = True
    except:
        results["square"] = False
        raise

def test_is_even():
    try:
        assert is_even(0) is True
        assert is_even(3) is False
        assert is_even(4) is True
        results["is_even"] = True
    except:
        results["is_even"] = False
        raise

def test_q1():
    q1_hash = "87b0d0175e1ee6134da981c2118695824b1d7073e81c9f358b8dcbfc8cbea847"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data["q1"])
        print(hash_answer(data["q1"]))
        assert hash_answer(data["q1"]) == q1_hash
        results["q1"] = True
    except:
        results["q1"] = False
        raise

def test_q2():
    q2_hash = "0bc4c9fd80ef53c294f056451fae3fae433e6274cb710598d5963b5a367d1b1b"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data["q2"])
        print(hash_answer(data["q2"]))
        assert hash_answer(data["q2"]) == q2_hash
        results["q2"] = True
    except:
        results["q2"] = False
        raise

# This is the main entry point for testing the tests. It's not needed by GH workflows, but it's useful for local testing.
if __name__ == "__main__":
    print("Local run")
