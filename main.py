import sys
from summarizer import Summarizer

API_KEY = 'YOUR_OPENAI_API_KEY'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<URL or text content>\"")
        sys.exit(1)

    # Input can be URL or raw text content
    input_content = sys.argv[1]
    summarizer = Summarizer(api_key=API_KEY)

    if input_content.startswith('http://') or input_content.startswith('https://'):
        summary = summarizer.summarize_url(input_content)
    else:
        summary = summarizer.summarize_text(input_content)

    print("Summary:", summary)