class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversedWords = words[::-1]
        return ' '.join(reversedWords)
inputString = "Hello world!"
sol = Solution()
reversedStr = sol.reverseWords(inputString)
print(f"Orig. string: {inputString}")
print(f"Reversed string: {reversedStr}")
inputStringTwo = "Testing string two"
reversedStrTwo = sol.reverseWords(inputStringTwo)
print(f"Orig. string: {inputStringTwo}")
print(f"Reversed string: {reversedStrTwo}")
