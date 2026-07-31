from planner.planner import execute_plan


def main():

    print("\n" + "=" * 70)
    print("               Agentic AI Employee Importer")
    print("=" * 70)

    prompt = input(
        "\nEnter your instruction:\n> "
    )

    csv_file, excel_file, sheet_url = execute_plan(prompt)

    print("\n" + "=" * 70)
    print("                Execution Summary")
    print("=" * 70)

    if csv_file:
        print(f"CSV File      : {csv_file}")

    if excel_file:
        print(f"Excel File    : {excel_file}")

    if sheet_url:
        print(f"Google Sheet  : {sheet_url}")

    print("=" * 70)


if __name__ == "__main__":
    main()