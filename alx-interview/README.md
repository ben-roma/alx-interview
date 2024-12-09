# Prime Game

## Overview
Maria and Ben are playing a game involving prime numbers. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples. The player who cannot make a move loses the game.

## Objective
Write a function `isWinner(x, nums)` to determine the winner of the game after `x` rounds.

## Requirements
- **Prototype**: `def isWinner(x, nums)`
- **Inputs**:
  - `x`: An integer representing the number of rounds.
  - `nums`: A list of integers, where each integer represents the size of the set for a round.
- **Output**:
  - The name of the player who won the most rounds (`"Maria"` or `"Ben"`).
  - Return `None` if there is no overall winner.

## Rules
1. Maria always goes first.
2. Both players play optimally.
3. A number `n` in the `nums` list will not exceed `10,000`.
4. The function should not use any external libraries.

## Example
### Input
```python
x = 3
nums = [4, 5, 1]
```

### Output
```python
"Ben"
```

### Explanation
1. **First round (`n = 4`)**:
   - Maria picks 2, removes 2 and 4, leaving 1 and 3.
   - Ben picks 3, removes 3, leaving 1.
   - **Winner**: Ben.

2. **Second round (`n = 5`)**:
   - Maria picks 2, removes 2 and 4, leaving 1, 3, 5.
   - Ben picks 3, removes 3, leaving 1, 5.
   - Maria picks 5, removes 5, leaving 1.
   - **Winner**: Maria.

3. **Third round (`n = 1`)**:
   - No prime numbers are available.
   - **Winner**: Ben.

Overall winner: **Ben** (2 wins).

## Constraints
- You must use an efficient algorithm to determine prime numbers (e.g., Sieve of Eratosthenes).
- Ensure the solution handles up to the maximum constraint efficiently.

## Implementation Steps
1. **Generate Primes**:
   Use the Sieve of Eratosthenes to generate all prime numbers up to the largest `n` in the `nums` list.
2. **Count Primes**:
   Precompute the cumulative number of primes up to each number.
3. **Determine Winners**:
   For each round, use the count of primes to decide the winner of the round.
4. **Return Final Winner**:
   Count the total wins for Maria and Ben and return the overall winner.

## Example Usage
### Input
```python
x = 5
nums = [2, 5, 1, 4, 3]
```

### Output
```python
"Ben"
```

## Files
- `0-prime_game.py`: Contains the `isWinner` function implementation.
- `README.md`: Documentation for the project.
- `main_0.py`: Example usage of the function.

## Testing
To test the implementation, create a `main_0.py` file with the following content:
```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```
Run the file to verify the output.

```bash
$ ./main_0.py
Winner: Ben
```

## Resources
- **Prime Numbers**: [Introduction to Prime Numbers](https://en.wikipedia.org/wiki/Prime_number)
- **Sieve of Eratosthenes**: [Algorithm Explanation](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- **Game Theory**: [Basic Concepts](https://en.wikipedia.org/wiki/Game_theory)

