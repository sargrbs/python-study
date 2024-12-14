from src.app.interfaces.LotteryCrawlerInterface import LotteryCrawlerInterface
from typing import List

class LotteryUseCase:
    def __init__(
        self,
        crawler: LotteryCrawlerInterface
    ):
        self.crawler = crawler
    
    async def get_lottery_data(self):
        result = self.crawler.crawl()
        return result