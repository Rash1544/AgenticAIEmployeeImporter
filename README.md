#  Agentic AI Employee Importer

An autonomous AI agent that accepts a natural language instruction, determines which tools to execute, and automates the process of generating employee data, importing it into Microsoft Excel, and uploading it to Google Sheets.

---

#  Features

- Accepts natural language commands.
- Uses a planner to decide which tools to execute.
- Generates realistic employee data using Faker.
- Creates a CSV file with 20+ employee records.
- Opens Microsoft Excel automatically.
- Imports the CSV into Excel.
- Saves the workbook as an XLSX file.
- Uploads the same data to Google Sheets using the Google Sheets API.
- Displays execution progress and a final execution summary.
- Handles errors gracefully.

---

#  Project Architecture

```
User Prompt
      │
      ▼
 Planner
      │
      ├───────────────┐
      │               │
      ▼               ▼
 CSV Tool        Excel Tool
      │               │
      └──────┬────────┘
             ▼
      Google Sheets Tool
             │
             ▼
      Execution Summary
```

---

#  Project Structure

```
AgenticAIEmployeeImporter/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env
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
├── memory/
├── logs/
├── tests/
└── config/
```

---

#  Technologies Used

- Python 3.11
- Pandas
- Faker
- PyWin32
- Google Sheets API
- GSpread
- Loguru

---

#  Prerequisites

- Python 3.11+
- Microsoft Excel (installed)
- Google Cloud Project
- Google Sheets API enabled
- Google Drive API enabled
- Service Account credentials (`service_account.json`)

---

#  Installation

Clone the repository:

```bash
git clone <repository-url>
cd AgenticAIEmployeeImporter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

#  Google Sheets Setup

1. Create a Google Cloud Project.
2. Enable:
   - Google Sheets API
   - Google Drive API
3. Create a Service Account.
4. Download the credentials JSON file.
5. Rename it to:

```
service_account.json
```

6. Place it inside:

```
credentials/
```

7. Share your Google Sheet with the Service Account email address.

---

# ▶ Running the Project

Run:

```bash
python app.py
```

Enter a natural language command such as:

```
Create a sample employee CSV and import it into Excel and Google Sheets.
```

or

```
Generate employee CSV, Excel and Google Sheet.
```

---

#  Workflow

The AI Agent performs the following steps autonomously:

1. Accepts a natural language instruction.
2. Determines which tools need to be executed.
3. Generates employee CSV data.
4. Opens Microsoft Excel.
5. Imports the CSV into Excel.
6. Saves the workbook.
7. Connects to Google Sheets.
8. Uploads the CSV data.
9. Displays an execution summary.

---

#  Sample CSV

| Employee ID | Name | Department | Email | Salary |
|-------------|------|------------|-------|--------|
| EMP001 | John Smith | Sales | john@example.com | 65000 |
| EMP002 | Alice Brown | HR | alice@example.com | 72000 |

---

#  Example Prompts

```
Create a sample employee CSV and import it into Excel and Google Sheets.
```

```
Generate employee CSV, Excel and Google Sheet.
```

```
Create employee data and upload it to Google Sheets.
```

---

#  Sample Output

```
Agentic AI Employee Importer

✓ CSV Generated Successfully

✓ Excel Workbook Created Successfully

✓ Google Sheet Updated Successfully

Execution Summary

CSV File      : output/employees.csv

Excel File    : output/employees.xlsx

Google Sheet  : https://docs.google.com/...
```

---

#  Demo

The demo video demonstrates:

- Running the application
- Entering a natural language prompt
- Automatic CSV generation
- Excel import
- Google Sheets upload
- Execution summary

---

# Author

**Rashmi Gulati**

Agentic AI Developer Technical Assessment