import sys
import os
import json
import hashlib
import atexit

# ============================ DO NOT MODIFY ============================
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'results.json'))
def hash_answer(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()
    
def write_grade_summary():
    # Extract only test-related boolean results
    test_keys = [k for k, v in results.items() if isinstance(v, bool)]
    passed = sum(results[k] is True for k in test_keys)
    max_score = len(test_keys)

    summary = {
        "total_score": passed,
        "max_score": max_score,
        "breakdown": {k: results[k] for k in test_keys}
    }

    try:
        with open("grade_summary.json", "w") as f:
            json.dump(summary, f, indent=2, sort_keys=True)
    except Exception as e:
        print(f"Failed to write grade summary: {e}")

@atexit.register
def write_fallback_summary():
    write_grade_summary()

def pytest_sessionfinish(session, exitstatus):
    write_grade_summary()
# ============================ DO NOT MODIFY END ========================

# Prepare grading dictionary
results = {
    "q1": False,
    "q2": False,
    "q3": False
}

def test_q1():
    q1_hash = "c7bf9385f58340b874a90022a40e0526a8cf197bd9e3f040625cc2e406372007"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q1"])
        print(hash_answer(data["q1"]))
        assert hash_answer(data["q1"]) == q1_hash
        results["q1"] = True
    except:
        results["q1"] = False
        raise

def test_q2():
    q2_hash = "3bc04fe8a605a977f168d0b2298073e80274aa5e7c319d2e8c06a0607671fdd2"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q2"])
        print(hash_answer(data["q2"]))
        assert hash_answer(data["q2"]) == q2_hash
        results["q2"] = True
    except:
        results["q2"] = False
        raise
        

def test_q3():
    q1_hash = "958e40ad722bd3f5e741ef7d0b1543a00af8ff17313dfaa2f1aac404c9c280de"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q3"])
        print(hash_answer(data["q3"]))
        assert hash_answer(data["q3"]) == q1_hash
        results["q3"] = True
    except:
        results["q3"] = False
        raise

        
        
# This is the main entry point for testing the tests. It's not needed by GH workflows, but it's useful for local testing.
if __name__ == "__main__":
    print("Local run")
