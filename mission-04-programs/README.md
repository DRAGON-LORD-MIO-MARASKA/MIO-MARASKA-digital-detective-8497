# Mission 4 — How programs run

## 1. Task / objective
Create and run a simple Python program, and compare how compilers and interpreters translate and execute code.

## 2. Work completed
- Created `hello.py` containing a one-line program that prints "Hello from Python".
- Ran it using Python 3 from Terminal and confirmed the output appeared.
- Completed the compiler vs interpreter comparison table.
- Wrote a short explanation of the difference in my own words.

## 3. Commands / tools used
- `python3 hello.py` — Ran the Python script from Terminal using the Python 3 interpreter.
- A text editor — Used to create and save the `hello.py` file.

## 4. My understanding

### Task 4.1 — Create and run a Python program

Created a file named `hello.py` with the following content:

```python
print("Hello from Python")
```

Ran it from Terminal:
```
$ python3 hello.py
Hello from Python
```

The message appeared successfully, confirming Python 3 is installed and the script works.

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|-------|---------|-------------|
| When translation / execution happens | Translates the entire source code into machine code before the program runs | Reads and executes the source code line by line at runtime |
| Typical output | A standalone executable file (binary) | No separate output file; the program runs directly from source |
| One example | GCC (compiles C code into a binary) | Python 3 (interprets `.py` files at runtime) |
| One advantage | Compiled programs generally run faster because translation is already done | Easier to test and debug because you can run code immediately without a separate build step |

**Explanation in my own words:**

A compiler reads the entire source code at once, checks it for errors, and translates it into machine code that the computer can run directly. This translation happens before the program executes, so the resulting binary tends to be fast. If there is an error, the compiler reports it during translation and no executable is produced.

An interpreter, on the other hand, processes the code line by line. It reads one instruction, translates it and executes it immediately, then moves to the next line. This makes development quicker because you can test changes instantly, but execution is typically slower since the translation happens every time the program runs. Python uses an interpreter, which is why you can run a `.py` file directly without a compile step.

In practice, many languages blend both approaches — for example, Python first compiles source code to bytecode internally, then interprets that bytecode. But the key distinction remains: a compiler produces a reusable output before execution, while an interpreter works through the code during execution.

## 5. Difficulties faced
No major difficulties. The program was a single line, so there was little room for error.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `hello.py` — The Python program created for this mission.
- This README.md documents the task, output and comparison.

## 8. Commit details
- **Commit message:** "Compare compilers and interpreters"
- **Pushed to GitHub:** Yes
