class Solution:
    def minWindow(self, s: str, t: str) -> str:
        store = {}
        for c in t:
            store[c] = store.get(c, 0) + 1

        count = 0
        res = None
        l = 0
        for r in range(0, len(s)):
            if s[r] in store:
                store[s[r]] -= 1
                if store[s[r]] == 0:
                    count += 1  # is valid
            while count == len(store):
                if s[l] in store:
                    if store[s[l]] + 1 > 0:
                        break   # window would become invalid -> not an option so break
                    else:
                        store[s[l]] += 1
                        l += 1
                else:
                    l += 1
            if count == len(store) and (not res or res[1] - res[0] > r - l):
                res = [l, r]
        return s[res[0]:res[1] + 1] if res else ""