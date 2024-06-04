
def is_anagram(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False

    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False

    return True


p = "anagrama"
q = "gramanaa"

print(is_anagram(p, q))


# solution 2
# def is_anagram(s: str, t: str) -> bool:
#     if len(t) != len(s):
#         return False
#
#     elif sorted(s) == sorted(t):
#         return True
#     return False
#
#
# p = "aa"
# q = "aa"
#
# print(is_anagram(p, q))