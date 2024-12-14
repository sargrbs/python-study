from abc import ABC, abstractmethod
from typing import List

class LotteryCrawlerInterface(ABC):
    @abstractmethod
    def crawl(self):
        pass