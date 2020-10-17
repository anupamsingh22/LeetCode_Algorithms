# https://leetcode.com/problems/integer-to-roman/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_values ={1000:'M',
                    900:'CM',
                    500:'D',
                    400:'CD',
                    100:'C',
                    90:'XC',
                    50:'L',
                    40:'XL',
                    10:'X',
                    9:'IX',
                    5:'V',
                    4:'IV',
                    1:'I'}
        roman_string=''
        roman_numbers= [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        for k in roman_numbers:
            while(num-k>=0):
                num-=k
                roman_string+=roman_values[k]
        return roman_string
