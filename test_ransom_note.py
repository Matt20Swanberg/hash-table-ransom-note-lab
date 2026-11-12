
from ransom_note import can_construct

# Display a formatted header to distinguish the test suite output
# from other terminal messages
print ('**********************************')
print('Starting Test Suite')
print ('**********************************\n')

def run_test(ransomNote, magazine, expected):
    result = can_construct(ransomNote, magazine)
    print(f"Testing: can_construct({ransomNote!r}, {magazine!r})")
    print(f"Expected: {expected}, Got: {result}")
    assert result == expected
    print("✅ Test passed!\n")

def test_can_construct():
    run_test("a", "b", False)
    run_test("aa", "ab", False)
    run_test("aa", "aab", True)
    run_test("abc", "cba", True)
    run_test("aabbcc", "abcabc", True)
    run_test("aabbcc", "aabbc", False)

def test_longer_cases():
    run_test("hiddenclue", "the quick fox had no idea a clue was hidden nearby", True)
    run_test("pythoncode", "coding in java and python should be fun and concise", True)
    run_test("impossible", "simple string without enough matching letters", False)
    run_test("helloworld", "hold water well, re-do logic and end up low", True)
    run_test("missingletter", "all missive notes are later retrieved", False)
    run_test("findthekey", "they knew the key was left behind in the drawer", True)
    run_test("mapthesecrets", "some great mysteries are mapped across sectors", False)
    run_test("notavailable", "none of the values align or balance in later events", True)

if __name__ == "__main__":
    test_can_construct()
    test_longer_cases()
    print("🎉 All tests passed!")
