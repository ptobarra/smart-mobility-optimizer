"""Smart mobility optimizer.

This module computes how much distance can be traveled on scooters before
reaching a finish line.
"""


def solution(finish, scooters):
    """Return total scooter distance covered before reaching `finish`.

    Rules:
    - Start at position 0.
    - Scooters are considered in ascending position order.
    - Ignore scooters located behind the current position.
    - At each scooter, ride at most 10 distance units, or less if `finish` is closer.
    - Stop once the finish line is reached or passed.

    Args:
        finish (int): Finish line position (distance from start).
        scooters (list[int]): Positions where scooters are available.

    Returns:
        int: Total distance traveled using scooters.
    """
    current_position = 0
    scooters_distance = 0

    for position in sorted(scooters):
        # Skip scooters behind us
        if position < current_position:
            continue

        # Move to scooter position
        current_position = position

        # Calculate how far we can go
        remaining = finish - current_position

        if remaining <= 0:
            break

        ride = min(10, remaining)

        scooters_distance += ride
        current_position += ride

        if current_position >= finish:
            break

    return scooters_distance


# Example usage:
# finish = 100
# scooters = [10, 20, 30, 40, 50, 60, 70, 80, 90]

input_finish = int(input("Enter the finish line distance: "))
input_scooters = list(
    map(int, input("Enter the scooter positions (comma separated): ").split(","))
)
print(
    f"The distance travelled on scooter is: {solution(input_finish, input_scooters)}"
)  # Output: 20
