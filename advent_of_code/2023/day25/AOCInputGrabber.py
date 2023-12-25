import os
import requests

class AOCInputGrabber:
    def __init__(self, year, day):
        self.year = year
        self.day = day

    def grab_input(self):

        session_key = os.environ.get('AOC_SESSION_KEY')
        
        url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'
        headers = {'cookie': f'session={session_key}'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        
        return "ERROR"