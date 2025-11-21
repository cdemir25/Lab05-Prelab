# Do not change below
import unittest
from q1 import longest_palindromic_substring



class test_longest_palindromic_substring(unittest.TestCase):
    def test_longest_palindromic_substring1(self):
        def longest_palindromic_substring(s):
            n = len(s)
            max_len = 0
            result = ""
            
            for i in range(n):
                # Odd length palindrome
                l, r = i, i
                while l >= 0 and r < n and s[l] == s[r]:
                    if (r - l + 1) > max_len:
                        max_len = r - l + 1
                        result = s[l:r+1]
                    l -= 1
                    r += 1

                # Even length palindrome
                l, r = i, i + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    if (r - l + 1) > max_len:
                        max_len = r - l + 1
                        result = s[l:r+1]
                    l -= 1
                    r += 1

            if max_len < 2:
                return ""  # If no palindromic substring of length >= 2

            return result
        self.assertEqual(longest_palindromic_substring('baabaad'),'aabaa', msg= "Test 1 Failed")
        
    def test_longest_palindromic_substring2(self):
        self.assertEqual(longest_palindromic_substring('cbfbdc'),'bfb', msg= "Test 2 Failed")
        
    def test_longest_palindromic_substring3(self):
        self.assertEqual(longest_palindromic_substring('Melonnothanks'),'onno', msg= "Test 3 Failed")
        
    def test_longest_palindromic_substring4(self):
        self.assertEqual(longest_palindromic_substring('nopalindrome'),'', msg= "Test 4 Failed")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_longest_palindromic_substring)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")