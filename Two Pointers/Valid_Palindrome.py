
# def isPalindrome(s: str) -> bool:
#     newStr = ""
#     for c in s:
#         if c.isalnum():
#             newStr += c.lower()
#         return newStr == newStr[::-1]
#
# print(isPalindrome("sugar"))

def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1

    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

print(isPalindrome("A man, a plan, a canal: Panama"))

