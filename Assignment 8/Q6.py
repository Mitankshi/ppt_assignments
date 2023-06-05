from collections import Counter

def findAnagrams(s, p):
    targetFreq = Counter(p)
    windowFreq = Counter()
    left = right = 0
    count = 0
    result = []

    while right < len(s):
        if s[right] in targetFreq:
            windowFreq[s[right]] += 1
            if windowFreq[s[right]] <= targetFreq[s[right]]:
                count += 1

        if right - left + 1 == len(p):
            if count == len(p):
                result.append(left)

            if s[left] in targetFreq:
                windowFreq[s[left]] -= 1
                if windowFreq[s[left]] < targetFreq[s[left]]:
                    count -= 1

            left += 1

        right += 1

    return result

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s=s,p=p))