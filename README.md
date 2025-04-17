# 📚 Assignment Tracker App

A personal Python-based tool to manage assignments and reminders using a clean GUI or CLI. Includes system tray notifications using Plyer or Win10Toast and optional packaging into an executable. Built to automate productivity for students.

## 🔧 Features

- Add and remove assignments with due dates
- Set custom reminders (minutes, hours, or days before deadline)
- Get desktop notifications on Windows
- GUI app built with `tkinter`
- CLI version available for fast terminal use
- Auto-install and executable support via PyInstaller

## 💻 Usage

### 1. Install dependencies
```
pip install -r requirements.txt
```

Or use the included installer scripts:
- `Install Schedule.py`
- `Installing Plyer.py`

### 2. Run the GUI app
```
python GUIAssingmentTracker.py
```

### 3. Or run the CLI version
```
python CLIAssingmentTracker.py
```

### 4. Build an executable (optional)
```
python Executable.py
```

## 📁 Files

| File | Description |
|------|-------------|
| `GUIAssingmentTracker.py` | Main GUI version with form-based task input |
| `CLIAssingmentTracker.py` | Command-line version with typed input |
| `Toast.py` | Notification handler |
| `Install Schedule.py`, `Installing Plyer.py` | Setup scripts for dependencies |
| `Executable.py` | Builds `.exe` using PyInstaller |

## ✅ Example Use Case

> Add "CS 171 Homework" due in 3 hours → Get a desktop reminder in 2.5 hours.

This tool was built for personal use but is fully customizable and open-source for anyone to improve.

## 🧠 Author

**Samuel de Souza**  
Biomedical Engineering @ Drexel | Data Engineering Intern  
[GitHub](https://github.com/SamAugusto) · [LinkedIn](https://www.linkedin.com/in/samuel-de-souza-0b1302226)

---
