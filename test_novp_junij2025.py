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
    q1_hash = "86768c6a5f7b7aad72621d650535d202ff6adcad4d7dc5c43a4e4b70ff6258e2"
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
    q2_hash = "d0ca09523ee73d662cd73024771da6b0d2959d1f36c102002c1fe7664bf78cdb"
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
    q3_hash = "36a703a54b51a692a666bb4e71cbdd666362eb6d3dbc46185ea1453417059ea9"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q3"])
        print(hash_answer(data["q3"]))
        assert hash_answer(data["q3"]) == q3_hash
        results["q3"] = True
    except:
        results["q3"] = False
        raise

def test_q4():
    q4_hash = "d230ea4eed71a89323c41594e699f21bea3f9b3f4b6750c7bc93f8ac829800af"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q4"])
        print(hash_answer(data["q4"]))
        assert hash_answer(data["q4"]) == q4_hash
        results["q4"] = True
    except:
        results["q4"] = False
        raise

def test_q5():
    q5_hash = "b6a58405ea3be6d740142ec7a06a954fcf6d108ebd9adeec2082940904ce0266"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q5"])
        print(hash_answer(data["q5"]))
        assert hash_answer(data["q5"]) == q5_hash
        results["q5"] = True
    except:
        results["q5"] = False
        raise

def test_q6():
    q6_hash = "b8401ddc027073fb4219e056e2a9ba5b6e6933a1c140e7b92aaf8dda63868edc"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q6"])
        print(hash_answer(data["q6"]))
        assert hash_answer(data["q6"]) == q6_hash
        results["q6"] = True
    except:
        results["q6"] = False
        raise

def test_q7():
    q7_hash = "0d06c1823b61eb8e39f71f62f9225391ff8580f8f827950b809972743737491b"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q7"])
        print(hash_answer(data["q7"]))
        assert hash_answer(data["q7"]) == q7_hash
        results["q7"] = True
    except:
        results["q7"] = False
        raise

def test_q8():
    q8_hash = "2a47a1f7d3b1590529b2f9f7ad145e2ba9cfcaa236a5d5fd8c7969ca5796cfc1"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q8"])
        print(hash_answer(data["q8"]))
        assert hash_answer(data["q8"]) == q8_hash
        results["q8"] = True
    except:
        results["q8"] = False
        raise

def test_q9():
    q9_hash = "93150c190c14ed56ae649716bd6bd8ea3cbc3acb1c0b772de9f4587a60e306f2"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q9"])
        print(hash_answer(data["q9"]))
        assert hash_answer(data["q9"]) == q9_hash
        results["q9"] = True
    except:
        results["q9"] = False
        raise

def test_q10():
    q10_hash = "8109b0cf8b49f7fa64aaeadb5ec32b690bd535b5a4fb9b266b587c73de67245a"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q10"])
        print(hash_answer(data["q10"]))
        assert hash_answer(data["q10"]) == q10_hash
        results["q10"] = True
    except:
        results["q10"] = False
        raise

def test_q11():
    q11_hash = "4235554ffc86b117b4ce06634a75e47054c1d6fa2f6ca6e3e31916af369e037f"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q11"])
        print(hash_answer(data["q11"]))
        assert hash_answer(data["q11"]) == q11_hash
        results["q11"] = True
    except:
        results["q11"] = False
        raise

def test_q12():
    q12_hash = "686ce729ae71d12e96c3b4f5d4cb7b18bb6d710c34fd5c101b5c463eee4a3ae8"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q12"])
        print(hash_answer(data["q12"]))
        assert hash_answer(data["q12"]) == q12_hash
        results["q12"] = True
    except:
        results["q12"] = False
        raise

def test_q13():
    q13_hash = "7b1962ed5aaf05941e6b766e7b509de7d270eec76f2ac6298666e6710e138671"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q13"])
        print(hash_answer(data["q13"]))
        assert hash_answer(data["q13"]) == q13_hash
        results["q13"] = True
    except:
        results["q13"] = False
        raise

def test_q14():
    q14_hash = "dc69fd52b74d90a633225c5893a33c5d4e1c114558ce2b16be7364b4caf70d74"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q14"])
        print(hash_answer(data["q14"]))
        assert hash_answer(data["q14"]) == q14_hash
        results["q14"] = True
    except:
        results["q14"] = False
        raise

def test_q15():
    q15_hash = "0d06c1823b61eb8e39f71f62f9225391ff8580f8f827950b809972743737491b"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q15"])
        print(hash_answer(data["q15"]))
        assert hash_answer(data["q15"]) == q15_hash
        results["q15"] = True
    except:
        results["q15"] = False
        raise

def test_q16():
    q16_hash = "ab840185ac3611542f7c7b0df4c039e834d4dd62f8b76118fe2dbb2e3a3e12ef"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q16"])
        print(hash_answer(data["q16"]))
        assert hash_answer(data["q16"]) == q16_hash
        results["q16"] = True
    except:
        results["q16"] = False
        raise

def test_q17():
    q17_hash = "1cae7292c2d66740d41f6c36ba9586d5bf53a403a9777e3a8114f9576d7f37eb"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q17"])
        print(hash_answer(data["q17"]))
        assert hash_answer(data["q17"]) == q17_hash
        results["q17"] = True
    except:
        results["q17"] = False
        raise

def test_q18():
    q18_hash = "eca68f378c86cdaf5975299ce86d1c99b8a472bf3ec00b4804af464aaf72a975"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q18"])
        print(hash_answer(data["q18"]))
        assert hash_answer(data["q18"]) == q18_hash
        results["q18"] = True
    except:
        results["q18"] = False
        raise

def test_q19():
    q19_hash = "dd47445dbdf488550f6b6024fccb26fd9642c07d263652124dfd0a9c62b0a090"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q19"])
        print(hash_answer(data["q19"]))
        assert hash_answer(data["q19"]) == q19_hash
        results["q19"] = True
    except:
        results["q19"] = False
        raise

def test_q20():
    q20_hash = "8d97786e2eb365de29010ff990d95d0fc3175a4a01af34b57356d84ac48d2cbe"
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        print(data)
        print(data["q20"])
        print(hash_answer(data["q20"]))
        assert hash_answer(data["q20"]) == q20_hash
        results["q20"] = True
    except:
        results["q20"] = False
        raise

# This is the main entry point for testing the tests. It's not needed by GH workflows, but it's useful for local testing.
if __name__ == "__main__":
    print("Local run")
