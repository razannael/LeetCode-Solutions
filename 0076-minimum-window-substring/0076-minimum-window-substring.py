class Solution:
 def minWindow(self, s: str, t: str) -> str:
  need = {}
  have = {}
  for c in t:
    need[c] = need.get(c, 0) + 1
    have[c] = 0
  
  left = 0
  right = 0
  count = 0
  min_size = float('inf')
  min_index = -1
  
  while right < len(s):
    c = s[right]
    right += 1
    if c in need:
      have[c] += 1
      if have[c] <= need[c]:
        count += 1
    while count == len(t):
      if right - left < min_size:
        min_size = right - left
        min_index = left
      c = s[left]
      left += 1
      if c in need:
        have[c] -= 1
        if have[c] < need[c]:
          count -= 1
  
  if min_size == float('inf'):
    return ""
  else:
    return s[min_index:min_index + min_size]
