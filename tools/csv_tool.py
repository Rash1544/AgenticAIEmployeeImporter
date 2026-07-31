import os
import pandas as pd
from faker import Faker
from loguru import logger

# Initialize Faker
fake = Faker()


def generate_employee_csv(output_folder="output", num_rows=20):
    """
    Generate a CSV file containing realistic employee data.
    """

    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        employees = []

        departments = [
            "HR",
            "Sales",
            "Finance",
            "Marketing",
            "IT",
            "Operations",
        ]

        # Generate employee records
        for i in range(1, num_rows + 1):
            employees.append(
                {
                    "Employee ID": f"EMP{i:03}",
                    "Name": fake.name(),
                    "Department": fake.random_element(departments),
                    "Email": fake.email(),
                    "Salary": fake.random_int(
                        min=40000,
                        max=120000,
                    ),
                }
            )

        # Create DataFrame
        df = pd.DataFrame(employees)

        # Output CSV path
        csv_path = os.path.abspath(
            os.path.join(output_folder, "employees.csv")
        )

        # Save CSV
        df.to_csv(csv_path, index=False)

        # Return CSV path
        return csv_path

    except Exception as e:
        logger.error(f"CSV Generation Error: {e}")
        return None