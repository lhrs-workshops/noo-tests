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

# Import the student's code
from student_code import square, is_even

# Prepare grading dictionary
results = {
    "q1": False,
    "q2": False,
    "q3": False,
    "q4": False,
    "q5": False,
    "q6": False,
    "q7": False,
    "q8": False,
    "q9": False,
    "q10": False,
    "q11": False,
    "q12": False,
    "q13": False,
    "q14": False,
    "q15": False,
    "q16": False,
    "q17": False,
}

def test_q1():
    q1_hash = "6218a8b8f0507acd99dac07206c9dd2d73f6dddcfdfc0d26b0264dbb76eb39ef"
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
    q2_hash = "60ff583acf2d35c1d7aaa45f8c436719a05951d17b0a5712e87ea3cc43f7f382"
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
    q1_hash = "019d8e5e3e7673ef80f1990be820ad456ae262ccad0a9acb02f43b7c9e9bdb50"
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

def test_q4():
    q2_hash = "d7a873550da50b47731800ebb08ab2b98483e67d24a2a0be4251e9c98e06ee93"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q4"])
        print(hash_answer(data["q4"]))
        assert hash_answer(data["q4"]) == q2_hash
        results["q4"] = True
    except:
        results["q4"] = False
        raise
        

def test_q5():
    q1_hash = "19093b85033a762a28a4e8652ac83b0d298605d11f03bd6e0a351ce825044aec"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q5"])
        print(hash_answer(data["q5"]))
        assert hash_answer(data["q5"]) == q1_hash
        results["q5"] = True
    except:
        results["q5"] = False
        raise

def test_q6():
    q2_hash = "b343d67e8385edb06e3db9758b92173a44aac2c0f3d8f2ba471ee3a43056cbbc"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q6"])
        print(hash_answer(data["q6"]))
        assert hash_answer(data["q6"]) == q2_hash
        results["q6"] = True
    except:
        results["q6"] = False
        raise

def test_q7():
    q1_hash = "d36b46937928cd1f2dcdb61e31df60b22c95501ebaaea0894a5d90583a75914d"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q7"])
        print(hash_answer(data["q7"]))
        assert hash_answer(data["q7"]) == q1_hash
        results["q7"] = True
    except:
        results["q7"] = False
        raise
        
def test_q8():
    q1_hash = "3b4db5e3b968412d97bf0001e2ffa0642bfe28610325f187f373059b30311ebe"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q8"])
        print(hash_answer(data["q8"]))
        assert hash_answer(data["q8"]) == q1_hash
        results["q8"] = True
    except:
        results["q8"] = False
        raise
        
def test_q9():
    q1_hash = "d2fe550ff61eec5df86a18f1778a4a38454df937e9264d4fa76ad273e358ec61"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q9"])
        print(hash_answer(data["q9"]))
        assert hash_answer(data["q9"]) == q1_hash
        results["q9"] = True
    except:
        results["q9"] = False
        raise
        
def test_q10():
    q1_hash = "c12d5a738c9433175229f2f1591b1ae042098b0f5e3239f1cfc5720f8e62f036"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q10"])
        print(hash_answer(data["q10"]))
        assert hash_answer(data["q10"]) == q1_hash
        results["q10"] = True
    except:
        results["q10"] = False
        raise
        
def test_q11():
    q1_hash = "33fbff18c59d019a46b107382c39e06ccfe4b6641c419d4653db5546fe8f647c"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q11"])
        print(hash_answer(data["q11"]))
        assert hash_answer(data["q11"]) == q1_hash
        results["q11"] = True
    except:
        results["q11"] = False
        raise
        
def test_q12():
    q1_hash = "ca0ec58701e94d68ae34ea8c0b25ed1287a5aaf9c2eedd1cfec30c35c2d62f8d"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q12"])
        print(hash_answer(data["q12"]))
        assert hash_answer(data["q12"]) == q1_hash
        results["q12"] = True
    except:
        results["q12"] = False
        raise
        
def test_q13():
    q1_hash = "c9512a1b12d7f5d1ec7bffbe6ce7bb6dcecc896b1dc464bfb03d2423a3af24e4"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q13"])
        print(hash_answer(data["q13"]))
        assert hash_answer(data["q13"]) == q1_hash
        results["q13"] = True
    except:
        results["q13"] = False
        raise
        
def test_q14():
    q1_hash = "1f738ec23c79e1cf2094324dd1c779d579bbd4b586f88f3d683aee47fbd2f479"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q14"])
        print(hash_answer(data["q14"]))
        assert hash_answer(data["q14"]) == q1_hash
        results["q14"] = True
    except:
        results["q14"] = False
        raise
        
def test_q15():
    q1_hash = "396789174ea86a40c4d3097f5498b04e1304f623dd079cb30d8cfe469ff95e86"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q15"])
        print(hash_answer(data["q15"]))
        assert hash_answer(data["q15"]) == q1_hash
        results["q15"] = True
    except:
        results["q15"] = False
        raise
        
def test_q16():
    q1_hash = "fc03eb60da66c2387f28a8cfc5d9826718d1fe5c52e46f5273168637d4b9c3cb"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q16"])
        print(hash_answer(data["q16"]))
        assert hash_answer(data["q16"]) == q1_hash
        results["q16"] = True
    except:
        results["q16"] = False
        raise
        
def test_q17():
    q1_hash = "38b4d1351fe8f20596489ef205b80541c3d66cd43de8ec30b82d64533f90c7c4"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q17"])
        print(hash_answer(data["q17"]))
        assert hash_answer(data["q17"]) == q1_hash
        results["q17"] = True
    except:
        results["q17"] = False
        raise


        
# This is the main entry point for testing the tests. It's not needed by GH workflows, but it's useful for local testing.
if __name__ == "__main__":
    print("Local run")
