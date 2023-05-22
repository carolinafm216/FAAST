import pandas as pd
from abc import ABC, abstractmethod


# FileProcessor
class file_processor:
    def __init__(self, file_path, strategy):
        self._file_path = file_path
        self._strategy = strategy

    def load_data(self):
        # read_file = pd.read_csv(path, sep="\t")
        data = self._strategy.read_file(self._file_path)
        df = pd.DataFrame(data)
        return df


# Define the interface for the strategies
class FileReadingStrategy(ABC):
    @abstractmethod
    def read_file(self, file_path):
        pass


# Define the concrete strategies
class CSVReadingStrategy(FileReadingStrategy):
    def read_file(self, file_path):
        data = pd.read_csv(file_path, sep="\t")
        return data


class JSONReadingStrategy(FileReadingStrategy):
    def read_file(self, file_path):
        data = pd.read_json(file_path)
        return data
