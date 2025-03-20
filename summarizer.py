import openai
import requests
from bs4 import BeautifulSoup

class Summarizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize_text(self, text):
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Summarize the following text:\n{text}\n",
            max_tokens=150
        )
        summary = response.choices[0].text.strip()
        return summary

    def summarize_url(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            text_content = ' '.join(p.text for p in paragraphs)
            return self.summarize_text(text_content)
        except Exception as e:
            return f"An error occurred while processing the URL: {str(e)}"