# Mission 5 — Numbers and data

## 1. Task / objective
Convert between decimal, binary and hexadecimal by hand, verify results using Python, build a small number converter program, and explain text encoding.

## 2. Work completed
- Manually converted seven values between decimal, binary and hexadecimal with working shown.
- Verified each conversion in the Python interactive shell.
- Created `number_converter.py` — a program that asks the user for a decimal number and displays its binary and hexadecimal equivalents.
- Tested the converter with three different numbers and recorded the results.
- Answered text-encoding questions about ASCII and UTF-8.

## 3. Commands / tools used
- `python3` — Opened the interactive Python shell for verification.
- `bin()` — Python built-in that converts an integer to its binary string.
- `hex()` — Python built-in that converts an integer to its hexadecimal string.
- `int('1010', 2)` — Converts a binary string to a decimal integer.
- `int('1F', 16)` — Converts a hexadecimal string to a decimal integer.
- `ord('A')` — Returns the ASCII decimal code for a character.
- `python3 number_converter.py` — Ran the converter from Terminal.

## 4. My understanding

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
|----------|------------------------|
| Convert decimal 13 to binary | 13 ÷ 2 = 6 R1, 6 ÷ 2 = 3 R0, 3 ÷ 2 = 1 R1, 1 ÷ 2 = 0 R1 → Read remainders bottom-up: **1101** |
| Convert decimal 25 to binary | 25 ÷ 2 = 12 R1, 12 ÷ 2 = 6 R0, 6 ÷ 2 = 3 R0, 3 ÷ 2 = 1 R1, 1 ÷ 2 = 0 R1 → **11001** |
| Convert binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 = 8 + 0 + 2 + 0 = **10** |
| Convert binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = 8 + 4 + 0 + 1 = **13** |
| Convert hexadecimal A to decimal | A = **10** |
| Convert hexadecimal 1F to decimal | 1×16 + F×1 = 16 + 15 = **31** |
| Convert binary 1111 to hexadecimal | 1111 in decimal = 15, and 15 in hexadecimal = **F** |

### Task 5.2 — Verify using Python

Opened the Python shell and confirmed:
- `bin(13)` → `'0b1101'` ✓
- `bin(25)` → `'0b11001'` ✓
- `int('1010', 2)` → `10` ✓
- `int('1101', 2)` → `13` ✓
- `int('A', 16)` → `10` ✓
- `int('1F', 16)` → `31` ✓
- `hex(15)` → `'0xf'` ✓

All manual calculations matched the Python results.

### Task 5.3 — Build a small number converter

Created `number_converter.py` (see the file in this folder). The program:
1. Asks the user to enter a decimal number.
2. Converts the input to an integer.
3. Displays the binary equivalent using `bin()`.
4. Displays the hexadecimal equivalent using `hex()`.

**Test results:**

| Test number | Binary output | Hexadecimal output |
|-------------|--------------|-------------------|
| 10 | 0b1010 | 0xa |
| 255 | 0b11111111 | 0xff |
| 42 | 0b101010 | 0x2a |

The `bin()` function converts an integer to a binary string prefixed with `0b`. The `hex()` function converts an integer to a hexadecimal string prefixed with `0x`. Both use Python's built-in base-conversion logic.

### Task 5.4 — How is text stored?

- **ASCII decimal code for uppercase A:** 65
- **ASCII decimal code for lowercase a:** 97
- **Why encoding standards are needed:** A computer stores everything as numbers. An encoding standard maps each character to a specific number so that every computer interprets the same byte values as the same characters. Without a standard, a file saved on one machine could display garbled text on another.
- **A character not in basic ASCII:** The emoji 😊 (or any character beyond code point 127, such as the rupee sign ₹). These require UTF-8 or another extended encoding because basic ASCII only covers 128 characters (0–127).

## 5. Difficulties faced
No major difficulties. Keeping track of remainder order when converting decimal to binary by hand required care to read them bottom-up.

## 6. How I resolved them
Drew out each division step clearly and read the remainders from the last to the first.

## 7. Evidence / files
- `number_converter.py` — The working Python converter program.
- This README.md documents all conversions, verification, test results and encoding answers.

## 8. Commit details
- **Commit message:** "Build number converter and practise data representation"
- **Pushed to GitHub:** Yes
