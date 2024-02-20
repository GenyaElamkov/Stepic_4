from collections import Counter

def duplicate_encode(word):
    cnt = Counter(word.lower())
    return ''.join([')' if cnt[c] > 1 else '(' for c in word.lower() ])



print(duplicate_encode('Success'))