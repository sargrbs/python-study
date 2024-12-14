import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from datetime import datetime

class LotteryCrawler:
    def __init__(self, base_url: str):
        self.base_url = base_url
        
    def fetch_page(self, url: str) -> str:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    
    def parse_lottery_results(self, html: str) -> List[Dict]:
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        
        for row in soup.select('tr:has(div.draw-number)'):
            draw_data = {
                'draw_number': self._extract_draw_number(row),
                'date': self._extract_date(row),
                'balls': self._extract_balls(row),
                'prize': self._extract_prize(row),
                'result': self._extract_result(row)
            }
            results.append(draw_data)
            
        return results
    
    def _extract_draw_number(self, row) -> str:
        draw_div = row.select_one('div.draw-number a')
        if draw_div:
            return draw_div.text.replace('Concurso ', '')
        return ''
    
    def _extract_date(self, row) -> str:
        date_div = row.select_one('div.date')
        if date_div:
            return date_div.text.strip()
        return ''
    
    def _extract_balls(self, row) -> List[int]:
        balls = row.select('ul.balls li.ball')
        return [int(ball.text.strip()) for ball in balls]
    
    def _extract_prize(self, row) -> str:
        prize_cell = row.select_one('td[data-title="Prêmio principal"]')
        if prize_cell:
            return prize_cell.text.strip()
        return ''
    
    def _extract_result(self, row) -> str:
        result_cell = row.select_one('td:last-child')
        if result_cell:
            return result_cell.text.strip()
        return ''
    
    def crawl(self) -> List[Dict]:
        try:
            html = self.fetch_page(self.base_url)
            return self.parse_lottery_results(html)
        except Exception as e:
            raise Exception(f"Error crawling lottery results: {str(e)}")