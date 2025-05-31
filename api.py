
import requests
from .auth import authenticate

class UnusualWhales:
    def __init__(self, username: str, password: str):
        self.session = authenticate(username, password)

    def get_option_flow(self, ticker: str, limit: int = 100) -> dict:
        url = f"https://api.unusualwhales.com/option-flow/{ticker}?limit={limit}"
        r = self.session.get(url)
        r.raise_for_status()
        return r.json()
