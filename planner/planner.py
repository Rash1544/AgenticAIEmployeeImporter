from tools.csv_tool import generate_employee_csv
from tools.excel_tool import import_csv_to_excel
from tools.google_sheet_tool import upload_to_google_sheet


def execute_plan(prompt):
    """
    Executes tools based on a natural language prompt.
    """

    prompt = prompt.lower()

    csv_file = None
    excel_file = None
    sheet_url = None

    # Generate CSV if requested
    if "csv" in prompt or "employee" in prompt:
        csv_file = generate_employee_csv()
        print("✓ CSV Generated Successfully")

    # Create Excel if requested
    if "excel" in prompt:
        if csv_file is None:
            csv_file = generate_employee_csv()
            print("✓ CSV Generated Successfully")

        excel_file = import_csv_to_excel(csv_file)
        print("✓ Excel Workbook Created Successfully")

    # Upload to Google Sheets if requested
    if "google" in prompt or "sheet" in prompt:
        if csv_file is None:
            csv_file = generate_employee_csv()
            print("✓ CSV Generated Successfully")

        sheet_url = upload_to_google_sheet(csv_file)
        print("✓ Google Sheet Updated Successfully")

    return csv_file, excel_file, sheet_url