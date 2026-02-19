# 🛴 Smart Mobility Optimizer

## Overview

As part of a reasoning engine simulation, you must model constrained movement along a one-dimensional path using available scooters.

This problem evaluates algorithmic thinking, greedy reasoning, state management, and clean Python implementation.

---

## 📘 Problem Description

You are given:

- An integer `finish`, representing the target destination on a number line.
- A list of integers `scooters`, representing positions where electric scooters are available.

You start at position `0`.

---

## 🚦 Rules

1. You may only use scooters located at or ahead of your current position.
2. When you reach a scooter at position `p`, you may ride it forward **up to 10 units**.
3. You cannot exceed the `finish` position.
4. Each scooter can be used at most once.
5. Scooters located behind your current position cannot be used.
6. You may use multiple scooters in sequence.
7. You stop once you reach or pass `finish`.

---

## 🎯 Objective

Return the **total distance traveled using scooters** until you reach the destination.

If the destination cannot be reached, return the total scooter distance accumulated before no further movement is possible.

---

## 📌 Function Signature (Python)

```python
def solution(finish: int, scooters: list[int]) -> int:
```

## 🔎 Example

Input

```python
finish = 23
scooters = [14, 7, 4]
```

Explanation

Sorted scooters: [4, 7, 14]

1. Move to scooter at position 4
   - Ride 10 units → reach position 14
   - Scooter distance: 10
2. Scooter at 7 is behind current position → skip
3. Move to scooter at position 14
   - Remaining distance to finish = 9
   - Ride 9 units → reach position 23
   - Scooter distance: 10 + 9 = 19

```python
19
```

## 📊 Constraints

- 1 ≤ finish ≤ 10^9
- 0 ≤ len(scooters) ≤ 10^5
- 0 ≤ scooters[i] ≤ 10^9

Your solution should run in O(n log n) time or better.

---

## 🧠 What This Tests

- Greedy algorithm design
- State tracking
- Correct ordering logic
- Edge case handling
- Clean, readable Python code
- Time complexity awareness

---

## ⚠️ Edge Cases to Consider

- No scooters available
- Scooter positions all behind start
- Finish reachable in a single ride
- Duplicate scooter positions
- Large input size
- Finish equals 0
- Finish smaller than first scooter position

---

## 💡 Implementation Notes

- Sorting scooters is typically required.
- Ensure you do not reuse scooters.
- Carefully update current position after each ride.
- Stop immediately once finish is reached.
