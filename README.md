# Minimal To‑Do App (Flet)

A clean, minimal to‑do list built with Flet (Flutter-like UI for Python). Add, complete, and delete tasks with optional local JSON persistence.

## Features
- Add tasks quickly
- Mark tasks as completed
- Delete tasks
- Optional local persistence (`tasks.json`)
- Minimal, distraction-free UI

## Tech Stack
- Python 3.9+
- [Flet](https://flet.dev/)

## Getting Started

### 1) Install
```bash
pip install flet
2) Run

python main.py
# or
flet run main.py
Note: Icons are specified as strings (e.g., "add", "delete_outline") for compatibility across Flet versions.

Project Structure

.
├─ main.py
├─ tasks.json            # created automatically (optional; ignored by git)
├─ README.md
├─ LICENSE
└─ .gitignore
Configuration
Persistence: The app writes tasks to tasks.json in the project root. It’s ignored by git by default (see .gitignore). You can delete it anytime to reset.
Troubleshooting
AttributeError: module 'flet' has no attribute 'icons'
Use icon strings (already in code), or upgrade Flet: pip install -U flet
