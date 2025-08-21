

# CLI File Explorer

A simple **command-line file explorer** built in Python. It allows you to navigate through a structured directory tree (e.g., `Categories → Years → Months → Dates → Files`) and open folders directly in your file explorer.

---

## 📂 Project Structure

```
CLI_fileExp/
│── DirExplorer.py         # Main CLI program
│── my_modules/
│   └── dir_utils.py       # Utility functions for directory handling
│── Categories/            # Example root directory
│   ├── 2024/
│   │   ├── 01_January/
│   │   │   ├── 01/ [files]
│   │   │   ├── 02/ [files]
│   │   └── 02_February/ ...
```

---

## ⚙️ Features

* Browse directories step by step:
  **Categories → Years → Months → Dates**
* View **file counts** and **directory sizes** with pretty tables (via [Rich](https://github.com/Textualize/rich)).
* **Fuzzy search & substring matching**: type partial names, and it finds the closest match.
* **Open directories** directly in your system’s file explorer (`open`, `xdg-open`, or `startfile`).
* **Back / Exit navigation** to move around easily.

---

## 🚀 Installation

1. Clone this repository or download the files:

   ```bash
   git clone https://github.com/hostaweba/CLI_fileExp.git
   cd CLI_fileExp
   ```

2. Install dependencies:

   ```bash
   pip install rich
   ```

---

## ▶️ Usage

Run the main script:

```bash
python DirExplorer.py
```

Then:

* Type the **name (or partial name)** of the folder you want to navigate.
* Use:

  * `back` → go one level up
  * `open` → open the current folder in your file explorer
  * `exit` → quit the program

---

## 📸 Example

```
Categories in 'CLI_fileExp'
+-------+-------------+-------+-----------+
| Index | Directory   | Files | Size (MB) |
+-------+-------------+-------+-----------+
| 1     | Work        | 10    | 1.23      |
| 2     | Personal    | 5     | 0.54      |
+-------+-------------+-------+-----------+

Enter the name of the category you want to choose, or 'exit' to quit:
```

---

## 🛠️ Requirements

* Python 3.7+
* [Rich](https://pypi.org/project/rich/)

---

## 📌 Notes

* Works on **Windows, macOS, and Linux**.
* Designed for **hierarchical folder structures** (Category → Year → Month → Date).
* If you want to list from the current directory, enter:

  ```python
  os.getcwd()
  ```


