from math import sqrt, floor

def solution(N):
    square_root = floor(sqrt(N))
    difference = N - square_root**2
    letters_per_group = square_root // 2 + difference

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = alphabet[:letters_per_group]

    result = ''
    for letter in letters:
        result += letter * (2 * letters_per_group)

    return result