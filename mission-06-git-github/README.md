# Mission 6 — Git and GitHub

## 1. Task / objective
Understand version control, stage and commit changes, create a branch, open a Pull Request and explain the collaboration workflow.

## 2. Work completed
- Inspected repository status, staged files, committed with a meaningful message, and viewed commit history.
- Created a branch named `update-about`, added a "My Learning" section to the root README, committed and pushed the branch.
- Created a Pull Request from `update-about` into `main` on GitHub.
- Built a Git command glossary.

## 3. Commands / tools used
- `git status` — Check which files are staged, modified or untracked.
- `git add <file>` — Stage a specific file for the next commit.
- `git commit -m "<message>"` — Save a snapshot of staged changes with a description.
- `git log --oneline` — View a compact list of recent commits.
- `git branch update-about` — Create a new branch.
- `git checkout update-about` — Switch to the new branch.
- `git push -u origin update-about` — Publish the branch to GitHub.
- `git checkout main` — Switch back to the main branch.
- `git pull origin main` — Bring the latest remote changes into the local main branch.

## 4. My understanding

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
|--------------|-------------------------------|
| Check repository status (`git status`) | Shows which files have been changed, which are staged and ready to commit, and which are not being tracked yet |
| Stage selected changes (`git add`) | Marks specific files to be included in the next commit — like putting items in a box before sealing it |
| Create a commit (`git commit -m`) | Takes a permanent snapshot of everything that is staged, along with a message explaining what changed and why |
| View commit history (`git log`) | Displays a list of all past commits, showing who made each change, when, and the message they wrote |

**Staging vs committing:** Staging selects which changes go into the next commit. Committing actually records those changes permanently in the project history. This two-step process lets you group related changes together even if you modified many files.

### Task 6.2 — Create and use a branch

1. Created the branch: `git branch update-about`
2. Switched to it: `git checkout update-about`
3. Added a "My Learning" section to the root README listing two or three things learned so far.
4. Staged and committed: `git add README.md` → `git commit -m "Add My Learning section to README"`
5. Pushed to GitHub: `git push -u origin update-about`

### Task 6.3 — Create a Pull Request

1. Opened the repository on GitHub.
2. GitHub showed a prompt to compare the `update-about` branch with `main`.
3. Created a Pull Request with a short description explaining the README update.
4. The PR is visible on GitHub. If the instructor has asked to merge it, it has been merged; otherwise, its status is noted as open.
5. After merging (if applicable): switched to `main` locally and ran `git pull origin main` to sync.

**What is a branch?** A branch is a separate line of development. It lets you work on a feature or change without affecting the main version of the project. When the work is ready, you merge the branch back into main.

**What is a Pull Request?** A Pull Request is a GitHub feature that lets you propose merging changes from one branch into another. Team members can review the differences, leave comments, and approve or request changes before the merge happens. This is useful when people work on the same project because it prevents untested or unreviewed code from going directly into the main branch.

### Task 6.4 — Git command glossary

| Git operation | One-line explanation |
|--------------|---------------------|
| `git init` | Initialises a new Git repository in the current folder |
| `git status` | Shows the current state of tracked, modified and staged files |
| `git add` | Stages files so they will be included in the next commit |
| `git commit` | Records a snapshot of all staged changes with a message |
| `git log` | Displays the history of commits in the repository |
| `git branch` | Creates or lists branches |
| `git checkout` | Switches to a different branch or restores a file |
| `git push` | Uploads local commits to a remote repository like GitHub |
| `git pull` | Downloads and merges remote changes into the local branch |

## 5. Difficulties faced
No major difficulties. Understanding the difference between `git add` (staging) and `git commit` (saving) took a moment, but the box-and-seal analogy helped.

## 6. How I resolved them
Thought of staging as selecting items and committing as packing and labelling the box — two distinct steps that give you control over what goes into each snapshot.

## 7. Evidence / files
- This README.md documents all Git operations, the branch workflow and the Pull Request.
- The `update-about` branch and Pull Request are visible on GitHub.

## 8. Commit details
- **Commit message:** "Complete Git and GitHub collaboration mission"
- **Pushed to GitHub:** Yes
