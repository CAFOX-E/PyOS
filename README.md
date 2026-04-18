# PyOS 2.0

> A fully-featured simulated operating system built in Python — run directly from your terminal.

PyOS is a command-line environment that mimics the experience of a real operating system. It supports file management, user accounts, AI conversations, encryption, local servers, mini-games, audio playback, and much more — all from a single Python script.

---

## Requirements

Install the required third-party packages before running:

```bash
pip install psutil pygame pyttsx3 google-generativeai beautifulsoup4 Pillow cryptography deep-translator
```

> **Note:** You'll also need a [Google Gemini API key](https://aistudio.google.com/) to use the `ai` command.

---

## Getting Started

```bash
python os.py
```

On first launch, PyOS will ask for a username and prompt you to create a password. Returning users are authenticated via the local `database/users_db.json` file.

---

## Commands

Once inside PyOS, type `help` to explore command categories:

| Category | Command |
|---|---|
| General | `help`, `help-basics`, `help-web`, `help-archives`, `help-office`, `help-config` |
| Navigation | `cd`, `list`, `tree`, `search` |
| File Operations | `mkdir`, `rmdir`, `delete`, `empty`, `open`, `read`, `write` |
| Web & Network | `browse`, `wiki`, `news`, `translate`, `track`, `ping`, `server` |
| Security | `lock`, `unlock`, `hide` |
| System | `status`, `devices`, `date`, `time`, `clear`, `logout`, `quit` |
| User Management | `adduser`, `dltuser` |
| Entertainment | `play`, `play_audio`, `speak` |
| AI | `ai` |

---

## Changelog

### v2.0 — Executable Update
- Added `compile.py` to package PyOS as a standalone `.exe` via PyInstaller. The compiled executable is output to the `dist/` folder.

### v1.0 — Games, Audio & Weather Update
- **Mini-games:** Type `play` to access *Guess the Number*, *Rock Paper Scissors*, and *Hangman*.
- **Weather:** Type `time` to see local weather in ASCII art, or `time <city>` for a specific location.
- **Audio:** `speak <text>` reads text aloud via TTS; `play_audio` plays an MP3 in the background.
- **Tree view:** `tree` recursively draws a visual map of your file structure using recursion.
- **Self-destruct:** Added the `self-destruct` command — initiates the Omega Protocol, permanently erasing all PyOS files. Use with caution.

### v0.9 — Server, Encryption & Hardware Update
- **Local servers:** `server web` or `server ftp` spins up a local file-sharing server (LAN only).
- **File encryption:** `lock <file>` encrypts any file with a password; `unlock <file>` decrypts it.
- **Hardware monitor:** `status` shows CPU and RAM usage; `devices` lists connected peripherals.

### v0.8 — AI Update
- Integrated Google Gemini AI via `import google.generativeai`.
- Type `ai` to start a conversation with the AI directly from the terminal.

### v0.7 — User Database & Settings Update
- Added `import json` and a local JSON-based user database (`database/users_db.json`).
- Stores usernames, hashed passwords, and per-user display color preferences.
- `adduser <name>` — creates a new user account from the terminal.
- `dltuser <name>` — deletes a user (with a safety lock preventing self-deletion).

### v0.6 — Text Management Update
- `read <file>` — displays the contents of `.txt` and other text files.
- `write <file>` — creates a new text file and lets you type content directly into it.

### v0.5 — List Update
- Improved `list` command output, now distinguishing between `[FOLDER]` and `[ARCHIVE]` entries with clean formatting.
- Added `import subprocess` and the ability to execute any file type using the OS default handler.

### v0.4 — File Management Update 2
- Added `import stat`.
- `mkdir <name>` — creates a new directory.
- `rmdir <name>` — deletes a directory.

### v0.3 — Login Update
- Introduced a login loop that prevents empty usernames.
- Personalized welcome message: *Welcome to PyOS, [Name]!*
- Dynamic prompt: the terminal now displays `Name@PyOS>` instead of the generic `PyOS>`.

### v0.2 — File Management Update
- Added `import shutil`.
- `cd <folder>` — navigate into local directories.
- `disk` — displays total and available storage space on your drive.

### v0.1 — Base
- Initial release: a simulated command-line shell in Python.
- Supported basic commands for file navigation, time display, and system interaction.

---

## Author

Created by **CAFOX-E**.
