class Solution:
    def maxDiff(self, num: int) -> int:
        # num = 151, [1, 5, 1]
        num_digits: list[int] = []
        while num > 0:
            num_digits.append(num % 10)
            num //= 10
        num_digits.reverse()  # num_digits will be storing the "maximum" value I can get
        
        num_digits_copy: list[int] = num_digits.copy()  # that will be storing the "minimum" value I can get
        
        # Max (num_digits)
        digit_to_transform: int = -1
        for i in range(len(num_digits)):
            if num_digits[i] != 9:
                digit_to_transform = num_digits[i]
                break
        for i in range(len(num_digits)):
            if num_digits[i] == digit_to_transform:
                num_digits[i] = 9
        
        # Min (num_digits_copy)
        digit_to_transform = -1
        transform_to_one: bool = False
        for i in range(len(num_digits_copy)):
            if num_digits_copy[i] > 1:
                digit_to_transform = num_digits_copy[i]
                if i == 0:
                    transform_to_one = True
                break
        for i in range(len(num_digits_copy)):
            if num_digits_copy[i] == digit_to_transform:
                num_digits_copy[i] = 1 if transform_to_one else 0
        
        # Return
        big_number: int = int(''.join(map(str, num_digits)))
        small_number: int = int(''.join(map(str, num_digits_copy)))
        
        return big_number - small_number
    