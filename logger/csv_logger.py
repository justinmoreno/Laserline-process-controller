"""CSV logger for process data."""
import csv


class CSVLogger:
    def __init__(self, filename):
        self.filename = filename

    def log(self, row):
        with open(self.filename, mode="a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)
