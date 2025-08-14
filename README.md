# Medical Records Tracker CLI

A command-line interface (CLI) tool written in Python for managing medical records using a relational database (e.g., MySQL). This includes functionality to create, view, update, and delete records—ideal for doctors, clinics, or small-scale healthcare setups.

---

##  Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  

---

## Features

- Uses a SQL database to store medical-related information  
- CLI interaction through a Python script (`index.py`)  
- Supports running pre-built SQL scripts to initialize the database  
- Modular and extensible—ideal for further expansion

---

## Prerequisites

- Python 3.x installed on your system  
- MySQL (or any compatible DBMS) installed and running  
- Basic familiarity with SQL and command-line usage

---

## Getting Started

1. **Clone the repository**
   ``bash
   git clone https://github.com/Adarsh-P-Thomson/Medical-Records-Tracker-PythonCLI.git
   cd Medical-Records-Tracker-PythonCLI
``

2. **Set up the database**

   * Open **MySQL Workbench** (or your preferred SQL client)
   * Run `CREATE DATABASE.sql` to initialize the schema
   * Run `DOCTOR DETAILS INSERT.sql` to populate initial data

3. **Configure the Python script**

   * Open `index.py` and adjust connection settings (e.g., host, port, database name, username, password)
   * Make any necessary adjustments to match your local setup

4. **Run the application**

   ```bash
   python index.py
   ```

---

## Usage

* Launches an interactive CLI that may allow:

  * Viewing all patients or doctors
  * Adding new patient or record entries
  * Searching and filtering records
  * Editing or deleting records
* *(Customize this section with specific commands or sample interactions if they exist in `index.py`.)*

---

## Project Structure

```
Medical-Records-Tracker-PythonCLI/
├── index.py                        # Main Python CLI application
├── CREATE DATABASE.sql             # SQL script for setting up schema
├── DOCTOR DETAILS INSERT.sql       # SQL script to insert sample data
├── .gitignore                      # Files to ignore in Git
└── README.md                       # Project documentation
```

---

## Contributing

Contributions, issues, and suggestions are welcome! To contribute:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes and push to your branch
4. Open a pull request describing your changes

---

