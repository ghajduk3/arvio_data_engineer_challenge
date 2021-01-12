import csv
import logging
import os
import re
logger = logging.getLogger(__name__)


def read_url_list(input_path):
    if os.path.exists(input_path):
        logger.info("")
    try:
        with open(input_path, 'r') as csv_file:
            url_list = [row[0] for row in csv.reader(csv_file)]
            return url_list
    except IOError:
        logger.exception("I/O error")
    except FileNotFoundError:
        logger.exception("FileNotFoundError")
    except Exception:
        logger.exception("Unexpected error")


def validate_property(property_id):
    return True if re.match(r"^\d{1,10}-\d{1,10}-\d{1,10}$",property_id) else False
