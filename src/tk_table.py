import openpyxl
from logging import getLogger
from src.tk_logger import initialize_logger

logger = getLogger(__name__)

def table():
    book = openpyxl.load_workbook('../menu.xlsx')
    active_sheet = book.active

    name_col = active_sheet.cell(column=2, row=1).value
    print(name_col)

    print("--------------------------")
    for column in active_sheet.columns:
        for cell in column:
            print(cell.value)

    logger.debug(active_sheet.columns)

if __name__ == "__main__":
    initialize_logger()
    table()
