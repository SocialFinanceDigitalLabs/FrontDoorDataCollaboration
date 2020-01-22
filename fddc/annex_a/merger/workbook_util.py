import logging
from dataclasses import dataclass
from typing import List
from xlrd import open_workbook

from fddc.annex_a.merger import FileSource

logger = logging.getLogger('fddc.annex_a.merger.workbook_util')


@dataclass
class WorkSheetDetail(FileSource):
    sheetname: str = None
    header_row_index: int = None
    header_values: List = None


def find_worksheets(source: FileSource) -> WorkSheetDetail:
    data_sources = []  # type: List[WorkSheetDetail]
    logger.debug("Opening {}".format(source.filename))
    workbook = open_workbook(filename=source.filename)

    for sheet_name in workbook.sheet_names():
        logger.debug("Checking sheet {} in {}".format(sheet_name, source.filename))
        sheet = workbook.sheet_by_name(sheet_name)

        # We search for first row with more than 3 non-null values
        header_row_index = None
        header_values = []
        for ix, row in enumerate(sheet.get_rows()):
            row_length = 0
            for col in row:
                if col.value is not None and len(col.value.strip()) > 0:
                    header_row_index = ix + 1
                    row_length += 1
            if row_length > 3:
                header_values = [col.value for col in row]
                break

        source_info = WorkSheetDetail(source)
        source_info.sheetname = sheet_name
        source_info.header_row_index = header_row_index
        source_info.header_values = header_values

        data_sources.append(source_info)

    return data_sources
