# Mission 3 — Understand the operating system

## 1. Task / objective
Explore the operating system environment, examine running processes, understand paths and permissions, and describe the core responsibilities of an OS.

## 2. Work completed
- Gathered system information: OS version, current user, storage, and a snapshot of running processes.
- Explored processes, identified PIDs, and gave examples.
- Explained absolute and relative paths with examples from the assignment folder.
- Reviewed file permissions using `ls -l` output.
- Completed the OS responsibilities table with explanations and examples.

## 3. Commands / tools used
- `uname -a` — Display OS kernel and system details.
- `sw_vers` — Show macOS version information.
- `whoami` — Print the current logged-in username.
- `df -h` — Display available and used disk space in human-readable form.
- `top -l 1 | head -15` — Capture a brief snapshot of system activity and resource usage.
- `ps aux` — List all running processes with details.
- `ls -l` — View file permissions, owner and size.

## 4. My understanding

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
|---------------------|-------------------|-------------------------------|
| Operating system / system details | The OS name, version and kernel build | macOS with Darwin kernel, running on an Apple Silicon Mac |
| Current account identity | Which user account is active | Showed the currently logged-in user via `whoami` — [redacted] |
| Available and used storage | How much disk space is free and occupied | The main volume had several hundred GB total with a healthy amount of free space remaining |
| System activity snapshot | CPU usage, memory pressure and top processes | A few background processes (WindowServer, kernel_task) used the most resources; overall CPU load was low |

### Task 3.2 — Understand processes

A **process** is a program that is currently running in memory. Every active application and background service is a process.

The **PID (Process ID)** is a unique number the OS assigns to each running process. It lets the system and the user identify, monitor or stop a specific process.

**Two examples of processes:**
1. **WindowServer** — the macOS process responsible for drawing everything on the screen (windows, menus, animations).
2. **Google Chrome Helper** — a child process created by Chrome to run individual tabs or extensions in isolation.

### Task 3.3 — Understand paths and permissions

- **Absolute path:** Starts from the root of the file system. Example: `/Users/[redacted]/digital-detective-8497/mission-03-operating-system/README.md`
- **Relative path:** Starts from the current working directory. Example: `mission-03-operating-system/README.md` (when already inside the project folder).

When I navigate into a subfolder with `cd mission-03-operating-system`, `pwd` shows a longer absolute path. When I go back up with `cd ..`, it shortens by one folder.

**File permissions (from `ls -l`):**

| Permission | Meaning | Example |
|-----------|---------|---------|
| r — Read | Allows a file's contents to be read | Opening a text file |
| w — Write | Allows a file to be changed | Editing a text file |
| x — Execute | Allows a file to be run; on a directory, allows access/traversal | Running a script |

Viewing a file inside the practice area showed permissions like `-rw-r--r--`, meaning the owner can read and write, while group and others can only read.

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
|------------------|-----------------|---------|
| Process management | The OS decides which programs get CPU time and in what order, starts and stops processes, and prevents them from interfering with each other | When I open Chrome and a text editor at the same time, the OS shares CPU time between them so both respond smoothly |
| Memory management | The OS allocates RAM to running programs and reclaims it when they close, ensuring no process reads or writes another's memory | Opening a large document makes the OS give that application more RAM; closing it frees that memory for others |
| Device management | The OS communicates with hardware through drivers so applications do not need to know the low-level details of each device | When I plug in a USB drive, the OS loads the correct driver and mounts the volume automatically |
| File management | The OS organises data into files and directories, tracks where each file is stored on disk, and enforces permissions | Creating a folder with `mkdir` or saving a document — the OS decides where on the SSD to write the data |
| User interface / shell | The OS provides a way for users to interact with the computer, either graphically (GUI) or through text (Terminal/shell) | The macOS Finder is a graphical interface; Terminal provides a text-based shell (zsh) |
| Security and permissions | The OS controls who can access files, run programs and change settings, protecting the system from unauthorised use | File permission bits (rwx) determine whether a user can read, modify or execute a file |

## 5. Difficulties faced
No major difficulties. Remembering to redact personal details (username, device name) from command outputs required care.

## 6. How I resolved them
Replaced all identifying information with `[redacted]` before saving any output.

## 7. Evidence / files
- This README.md contains all tables, explanations and observations.

## 8. Commit details
- **Commit message:** "Document operating system and file management"
- **Pushed to GitHub:** Yes
