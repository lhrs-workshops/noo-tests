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
    "q18": False,
    "q19": False,
    "q20": False
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
        print(data["q1"])
        print(hash_answer(data["q1"]))
        assert hash_answer(data["q1"]) == q1_hash
        results["q1"] = True
    except:
        results["q1"] = False
        raise

def test_q4():
    q2_hash = "cca6864bfd7980be6e9a0edbf3193654f6a9bbf573a15753f3951bebdcb42095"
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
        

def test_q5():
    q1_hash = "5d3015b63d8af4f4724ffc3b91d4e98d67939990619c523d4402d16a81fdf559"
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

def test_q6():
    q2_hash = "cafc2b4e51c9f05e6291fa49acf275332cd769692ad2f13d64dcc8a520e6f58c"
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

def test_q7():
    q1_hash = "2c84e13e57f61c52eeb4bae9c6149f20c89d30c0f3be7544682738431d4049f9"
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
        
def test_q8():
    q1_hash = "eb6b42f54c42d2832e296319f7fdad64d46aecd1ec19b0e9c80b85b7cfc6dcae"
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
        
def test_q9():
    q1_hash = "28da6f798cd9ae0d25d6fcc3be6bc6d8abd09cb9049a66bc895b25893a796c71"
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
        
def test_q10():
    q1_hash = "ed24133505fb139983ca73ee8f0aa16a49ce35a040ba9b525cc0290677889a2f"
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
        
def test_q11():
    q1_hash = "ca35426354b0032527ee935252de08087d146765e61ace737370d85743b1d29b"
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
        
def test_q12():
    q1_hash = "10938bcaeb7f854e57ff7d4eb6d2ec753e1c54d028a48d7ebfe229d03c0ad316"
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
        
def test_q13():
    q1_hash = "6de531d5bd95ebde1a6812a0f67eaadcc9df6cb99fb5855eba296f553a8b3570"
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
        
def test_q14():
    q1_hash = "81ca8841de3e558d0619e9233e0c4bd94929c12a0459424e0dd09956733c9845"
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
        
def test_q15():
    q1_hash = "cf4dd3ed7f51e354195effa629655379abce5fb41136ee6f1dc8920c95c45e05"
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
        
def test_q16():
    q1_hash = "4e4232796d245bc814daf8c0a3728a84230cb2536976eb6b3efd5179a35e18c4"
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
        
def test_q17():
    q1_hash = "c91a003e06cd9fcb5a4e6bb8662286863fd0c7d3f22306ad3074552e2bea5f84"
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
        
def test_q18():
    q1_hash = "cdf74c872e4cd3cd00b0a4901b8228ea45c489ed6699c11596dc7888c60e7f8e"
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
        
def test_q19():
    q1_hash = "092c2f2772756f811244f41109dd39f2041a54af886587d370f8f8536bdf4c21"
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
        
def test_q20():
    q1_hash = "d2de5615db80158ab8b7910584e9b30cd3467837d9e07295b34ae6c89b871534"
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

        
        
# This is the main entry point for testing the tests. It's not needed by GH workflows, but it's useful for local testing.
if __name__ == "__main__":
    print("Local run")
