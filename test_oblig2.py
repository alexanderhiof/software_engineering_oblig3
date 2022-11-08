import pytest

# Leap year check function for testing
def LeapCheck(year):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0: # Leap year check'
        return True
    else:
        return False
        


# Tests using unittest
# class CheckLeapYear(unittest.TestCase):
#     def tests(self):
#         self.assertTrue(LeapCheck(2000)) # Year is Divisible By 400
#         self.assertTrue(LeapCheck(1996)) # Year is Divisible By 4 Not 100
#         self.assertFalse(LeapCheck(1900)) # Year is Not Divisible By 4
#         self.assertFalse(LeapCheck(1700)) # Year is Divisible By 100 Not 400

# Tests using pytest
class TestLeapYear():
        
    def testYearIsDivisibleBy400(self):
        result = LeapCheck(2000)
        assert result == True
        
    def testYearisDivisibleBy4Not100(self):
        result = LeapCheck(1996)
        assert result == True
        
    def testYearisNotDivisibleBy4(self):
        result = LeapCheck(1900)
        assert result == False
        
    def testYearisDivisibleBy100Not400(self):
        result = LeapCheck(1800)
        assert result == False

    
