# checking if two strings are anagram 

s = "aabc"
t = "abca"

if len(s) != len(t):
    print("Not Anagram")
else:
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in t:
        if ch not in freq:
            print("Not Anagram")
            break
        freq[ch] -= 1
        if freq[ch] < 0:
            print("Not Anagram")
            break
    else:
        print("Anagram")

  # time complexity O(n)
  # space complexity O(n)
