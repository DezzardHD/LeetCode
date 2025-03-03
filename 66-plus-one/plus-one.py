class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        uebertrag = 0
        for i in reversed(range(0, len(digits))):
            print(i)
            if i == len(digits) - 1 or uebertrag == 1:
                digits[i] += 1
                if digits[i] < 10:
                    uebertrag = 0
                else:
                    digits[i] = 0
                    uebertrag = 1
            else:
                break
        if uebertrag == 1:
            digits = [1] + digits
        return digits
