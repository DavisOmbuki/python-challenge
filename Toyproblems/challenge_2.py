def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    digit_sums = set()

    for num in A:
        digit_sum_value = digit_sum(num)

        # If we find a pair with equal digit sum, calculate the sum and return it
        if digit_sum_value in digit_sums:
            return num + max(A)

        digit_sums.add(digit_sum_value)

    # If no pair is found, return -1
    return -1