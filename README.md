# Smart Mobility Optimizer

A simple Python project that calculates how much total distance can be traveled using scooters before reaching a finish line.

## Overview

The optimizer follows these rules:

- Start at position `0`
- Scooters are processed in ascending order
- Ignore scooters behind the current position
- At each scooter, ride up to `10` units (or less if the finish line is closer)
- Stop when the finish line is reached or passed

## Project Structure

- `smart_mobility_optimizer.py` — main Python script with the `solution(finish, scooters)` function and CLI input handling
- `run_smart_mobility_optimizer.sh` — shell script to run the Python program

## Requirements

- Python 3.x
- Linux/macOS shell (for `.sh` script)

## Run the Project

### Option 1: Run with Python directly

```bash
python3 smart_mobility_optimizer.py
```

### Option 2: Run with shell script

```bash
chmod +x run_smart_mobility_optimizer.sh
./run_smart_mobility_optimizer.sh
```

## Input Format

When prompted:

1. Enter finish line distance as an integer
2. Enter scooter positions as comma-separated integers

Example:

- Finish: `100`
- Scooters: `10,20,30,40,50,60,70,80,90`

## Example Output

```text
The distance travelled on scooter is: 20
```

## License

MIT.
