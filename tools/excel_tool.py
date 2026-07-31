import os
import time
import win32com.client
from loguru import logger


def import_csv_to_excel(csv_path):

    try:

        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = True
        excel.DisplayAlerts = False

        workbook = excel.Workbooks.Open(csv_path)

        time.sleep(2)

        xlsx_path = os.path.splitext(csv_path)[0] + ".xlsx"

        workbook.SaveAs(xlsx_path, FileFormat=51)

        workbook.Close(False)

        excel.Quit()

        return xlsx_path

    except Exception as e:
        logger.error(e)
        return None