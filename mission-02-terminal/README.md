# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use the command-line interface to inspect folders, create and manage practice files, understand options and pipes, and explain package managers.

## 2. Work completed
- Practised nine basic Terminal operations and recorded each command, its purpose, and what I observed.
- Created a `terminal-practice` folder, wrote and appended to a text file, made a backup copy, and renamed it.
- Explored flags (`-a`, `-l`, `-lh`) and used a pipe to send output through `head`.
- Investigated the Homebrew package manager on macOS.

## 3. Commands / tools used
- `pwd` — Print working directory.
- `ls` — List files and folders.
- `ls -l` — Detailed listing with permissions, size and date.
- `ls -la` — Detailed listing including hidden files.
- `ls -lh` — Human-readable file sizes.
- `cd ..` — Move to the parent directory.
- `cd <folder>` — Move into a named directory.
- `mkdir` — Create a new directory.
- `touch` — Create an empty file.
- `cp` — Copy a file.
- `mv` — Move or rename a file.
- `cat` — Display the contents of a file.
- `echo "text" > file` — Write text to a file (overwrites).
- `echo "text" >> file` — Append text to a file.
- `ls -l | head -5` — Pipe the detailed listing to show only the first five lines.
- `brew --version` — Check if Homebrew is installed.
- `brew list` — View packages managed by Homebrew.

## 4. My understanding

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
|-------------------------|-------------|----------------|
| Current-directory display (`pwd`) | Prints the full path of the folder I am currently in | Showed the absolute path to my assignment repository |
| Directory listing (`ls`) | Lists all visible files and folders in the current location | Displayed the mission folders and README.md |
| Detailed listing (`ls -l`) | Shows permissions, owner, size, date and name for each item | Each line started with permission letters like `drwxr-xr-x` for folders |
| Change directory (`cd ..`) | Moves up one level to the parent folder | The path returned by `pwd` shortened by one folder |
| Create directory (`mkdir terminal-practice`) | Creates a new empty folder with the given name | A new folder appeared in the listing |
| Create empty file (`touch notes.txt`) | Creates a file with zero bytes if it does not exist | `ls -l` showed `notes.txt` with size 0 |
| Copy file (`cp notes.txt notes-copy.txt`) | Makes a duplicate of the file with a new name | Both files appeared in the listing with identical sizes |
| Move / rename file (`mv notes-copy.txt backup.txt`) | Changes the file's name (or location) | `notes-copy.txt` disappeared and `backup.txt` appeared |
| Display file contents (`cat notes.txt`) | Prints the entire contents of the file to the Terminal | The text I had written earlier was printed on screen |

### Task 2.2 — Practise file changes safely

Inside the `terminal-practice` folder:

1. Created a text file and wrote one line: `echo "First line of my practice file" > practice.txt`
2. Appended a second line without removing the first: `echo "Second line added later" >> practice.txt`
3. Displayed the file: `cat practice.txt` — both lines were visible.
4. Made a backup: `cp practice.txt practice-backup.txt`
5. Renamed the backup: `mv practice-backup.txt safe-copy.txt`

**Answers:**

- **Replacing vs appending:** Using `>` replaces the entire file content, while `>>` adds new text at the end without touching existing content.
- **Copying vs moving:** `cp` creates a second independent copy of the file, leaving the original in place. `mv` relocates or renames the file — the original path no longer exists.
- **What `pwd` provides:** It shows the absolute path to your current working directory, which helps you confirm where you are in the file system.
- **Why directory listing is useful:** It lets you verify which files and folders exist before running commands, preventing mistakes like overwriting or deleting the wrong file.

### Task 2.3 — Understand flags and pipes

- `ls` shows file names only. `ls -la` adds hidden files (those starting with `.`), permissions, owner, size and modification date. The `-h` flag makes sizes human-readable (e.g., `4.0K` instead of `4096`).
- **Pipe example:** `ls -l | head -5` sends the full detailed listing into `head`, which keeps only the first five lines. The pipe symbol `|` connects the output of the left command to the input of the right command, letting you chain tools together.

### Task 2.4 — Understand package managers

A package manager automates installing, updating and removing software. Instead of downloading files from websites and manually setting them up, a package manager handles dependencies, versions and cleanup in one command.

On macOS, Homebrew is the most common package manager. I checked its version with `brew --version` and listed managed packages with `brew list`. Package managers are useful because they keep software organised, make updates easy, and reduce the risk of installing conflicting or outdated versions.

## 5. Difficulties faced
No major difficulties. Remembering the difference between `>` (overwrite) and `>>` (append) required careful attention to avoid accidental data loss during practice.

## 6. How I resolved them
Tested both operators on a practice file first and confirmed the result with `cat` before using them on important files.

## 7. Evidence / files
- This README.md documents all tasks, commands, tables and answers.

## 8. Commit details
- **Commit message:** "Complete Terminal and file management mission"
- **Pushed to GitHub:** Yes
