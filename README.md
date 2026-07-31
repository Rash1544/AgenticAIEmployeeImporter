# Agentic AI Employee Importer

An autonomous AI-powered application that accepts natural language instructions, determines the required workflow using a planner, and automates employee data generation, Microsoft Excel processing, and Google Sheets integration.

---

## Features

- Accepts natural language instructions.
- Uses a planner to determine which tools should be executed.
- Generates realistic employee data using the Faker library.
- Creates a CSV file containing 20+ employee records.
- Opens Microsoft Excel automatically.
- Imports the CSV into Microsoft Excel.
- Saves the workbook as an Excel (.xlsx) file.
- Uploads employee data to Google Sheets using the Google Sheets API.
- Displays execution progress and a final execution summary.
- Modular architecture for easy extension.
- Includes graceful error handling.

---

# Project Architecture

```text
                User Prompt
                     │
                     ▼
                 Planner
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
   CSV Generation Tool      Excel Import Tool
                     │
                     ▼
          Google Sheets Upload Tool
                     │
                     ▼
             Execution Summary
```

---

# Project Structure

```text
AgenticAIEmployeeImporter/
│
├── app.py
├── README.md
├── requirements.txt
├── example_prompts.txt
├── .gitignore
│
├── planner/
│   └── planner.py
│
├── tools/
│   ├── csv_tool.py
│   ├── excel_tool.py
│   └── google_sheet_tool.py
│
├── credentials/
│   └── service_account.json
│
├── output/
│   ├── employees.csv
│   └── employees.xlsx
│
├── logs/
├── memory/
├── tests/
└── config/
```

---

# Technologies Used

- Python 3.11
- Faker
- Pandas
- PyWin32
- Google Sheets API
- GSpread
- Loguru

---

# Prerequisites

Before running the project, ensure the following are installed:

- Python 3.11+
- Microsoft Excel
- Google Cloud Project
- Google Sheets API enabled
- Google Drive API enabled
- Google Service Account credentials

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Rash1544/AgenticAIEmployeeImporter.git

cd AgenticAIEmployeeImporter
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Google Sheets Setup

1. Create a Google Cloud Project.
2. Enable:
   - Google Sheets API
   - Google Drive API
3. Create a Service Account.
4. Download the Service Account credentials.
5. Rename the file to:

```
service_account.json
```

6. Place it inside:

```
credentials/
```

7. Share your Google Sheet with the Service Account email.

---

# Running the Project

Run:

```bash
python app.py
```

If using a Conda environment:

```bash
conda activate agentic_ai

python app.py
```

---

# Example Prompts

The planner accepts natural language instructions such as:

- Create a sample employee CSV and import it into Excel and Google Sheets.

- Generate employee data and upload it to Google Sheets.

- Create employee records, save them as Excel, and update Google Sheets.

- Generate at least 20 employee records, convert them into an Excel workbook, and upload them to Google Sheets.

- Generate employee CSV, Excel workbook, and Google Sheet.

---

# Workflow

The application autonomously performs the following steps:

1. Accepts a natural language instruction.
2. Planner determines which tools need to be executed.
3. Generates employee data.
4. Creates a CSV file.
5. Opens Microsoft Excel.
6. Imports the CSV into Excel.
7. Saves the workbook as an Excel file.
8. Connects to Google Sheets.
9. Uploads employee data.
10. Displays an execution summary.

---

# Sample CSV

| Employee ID | Name | Department | Email | Salary |
|-------------|------|------------|------------------|--------|
| EMP001 | John Smith | Sales | john@example.com | 65000 |
| EMP002 | Alice Brown | HR | alice@example.com | 72000 |

---

# Sample Output

```text
==========================================================

            Agentic AI Employee Importer

==========================================================

✓ CSV Generated Successfully

✓ Excel Workbook Created Successfully

✓ Google Sheet Updated Successfully

==========================================================

Execution Summary

CSV File      : output/employees.csv

Excel File    : output/employees.xlsx

Google Sheet  : https://docs.google.com/...

==========================================================
```

---

# Output Files

The generated files are automatically saved inside the **output** directory.

```
output/
│
├── employees.csv
└── employees.xlsx
```

---

# Demo

The demonstration video includes:

- Project overview
- Folder structure
- Planner explanation
- Running the application
- Natural language prompt execution
- CSV generation
- Excel automation
- Google Sheets upload
- Execution summary

---

# Future Improvements

Possible future enhancements include:

- Support for JSON and XML exports.
- Database integration (MySQL/PostgreSQL).
- OpenAI-powered intelligent planning.
- Web interface using Flask or Streamlit.
- PDF report generation.
- Additional productivity tools.

---

# Author

**Rashmi Gulati**

Submitted as part of the **Agentic AI Developer Technical Assessment**.