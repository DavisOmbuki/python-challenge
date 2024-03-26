def solution(A):
    total_bricks = sum(A)
    num_boxes = len(A)

    if total_bricks % num_boxes != 0:
        return -1

    target_bricks = 10
    differences = [abs(target_bricks - bricks) for bricks in A]
    max_difference = max(differences)

    moves = max_difference // 2
    return moves