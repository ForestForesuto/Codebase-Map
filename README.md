<div align="center">

# Codebase-Gitmap
A CLI tool that visualizes the file structure of any codebase.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ruff](https://img.shields.io/badge/Ruff-Code%20Style-D7FF64?style=for-the-badge&logo=ruff&logoColor=black)](https://docs.astral.sh/ruff/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](https://choosealicense.com/licenses/mit/)

</div>

---

## Features
- Visualizes the file structure of any codebase as a ASCII tree.
- Respects `.gitignore` of the directory.
- Auto-exclude hidden files/folders from the output *(Can be overriden by -allowhiddens)*.

---

## Installation
```bash
git clone https://github.com/ForestForesuto/Codebase-Map.git
pip install .
```

#### **OR**

```bash
pip install codebase-gitmap
```

## Usage
#### **Input Example:**
```bash
cv
```

#### **Expected Output:**

![](https://private-user-images.githubusercontent.com/278855612/643255515-64b00c69-fddd-4478-904f-e22e42869983.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODgxMTEwMTAsIm5iZiI6MTc4ODExMDcxMCwicGF0aCI6Ii8yNzg4NTU2MTIvNjQzMjU1NTE1LTY0YjAwYzY5LWZkZGQtNDQ3OC05MDRmLWUyMmU0Mjg2OTk4My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDgzMFQxNzI1MTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hNzdjMzZiMjc1YzE0YWZkYzAzMTlhZWU3MWU0YzI5Mjg1NGRmZGY2YzljZTcxYzAzZWVlMjcwZWE1NzU1ODA3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.ty66Qkc5BCyIIaPklPS9rrFG0ghhs62_5w1QV3byt2E)

#### **Input Example:**
```bash
cv "..\..\YOUTUBE PLAYLIST ACCOUNT EXPORTER\root"
```

#### **Expected Output:**

![](https://private-user-images.githubusercontent.com/278855612/643255545-bc1754f7-f13c-4f98-9d13-9999fe1fc8de.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODgxMTEwMjksIm5iZiI6MTc4ODExMDcyOSwicGF0aCI6Ii8yNzg4NTU2MTIvNjQzMjU1NTQ1LWJjMTc1NGY3LWYxM2MtNGY5OC05ZDEzLTk5OTlmZTFmYzhkZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwODMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDgzMFQxNzI1MjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01OGU0MzJjZjE2NzNmMTAyOWU3MTczMDAxZjQyZDhkZjQ0OWY2Yjc2YWU1MDdiZTdjNWRkYWFhNzJhODVhMTE0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.lGcTQbJPSJWNagQ8RiK2aMoWWsqiARuMdK63EehV0A4)

---

## Tech-stack
- **Language:** Python 3.11+
- **Library:** pathspec (for .gitignore patterns)
- **CLI Framework:** argparse (built-in)

## License
Distributed under the MIT License. See `LICENSE` for more information.