
from os import path, getenv


CHROME_OPTIONS_ARGS = [
    '--no-first-run',
    '--no-service-autorun',
    '--password-store=basic',
    '--user-data-dir=/Users/khizer/Library/Application Support/Google/Chrome', # to use default chrome window
    "--profile-directory=Default",
    '--disable-blink-features=AutomationControlled',
    '--blink-settings=imagesEnabled=false',
    '--disable-extensions',
    '--disable-plugins-discovery',
    '--disable-popup-blocking',
    '--log-level=3',
    '--disable-dev-shm-usage',
    '--no-sandbox',
    # '--disable-gpu',
    # '--incognito',
    # '--headless',  # Uncomment if headless mode is desired
]


"""---------------------- PATHS ----------------------"""
 # Get the project root directory (please note that this wont be root if you using this project as module)
PROJECT_ROOT = path.abspath(path.dirname(path.abspath(__file__)))
ELEMENT_SELECTORS_YAML_PATH = path.join(PROJECT_ROOT, 'element_selectors.yaml')

"""---------------------- CREDENTIALS ----------------------"""
BASE_URL = "https://chatgpt.com/?temporary-chat=true&model=gpt-4"
GPT_EMAIL = getenv('GPT_MAIL')
GPT_PASSWORD = getenv('GPT_PASS')


"""---------------------- APP CONFIGS ----------------------"""
BASELINE_PROMPT = "Please keep the response in 100 words!" # dummy example, not used yet

#Frame prompts:
""" SAMPLE PROMPT for generating frame from a paragraph.
Highlight 3 main keywords (named entities preffered separated by ,) from the given news:
Meta is reportedly working on AI-powered earphones equipped with cameras. Internally codenamed 'Camerabuds', the earphones will leverage AI capabilities for real-time object identification and foreign language translation. Meta's leadership sees AI-powered earphones as the next logical step in the evolution of wearable technology. It has partnered with Kansas-based electronics company Ear Micro to explore the possibilities of this emerging technology.

Generate 1 Square, Dark, Fade, Bluescale, Sci-fi, AI, Futuristic image, strictly having the following text/logo/girl: Reddit, OpenAI, Data API
"""

# TODO: Use following prompt for improving news:
"""
Make this news as easy as possible with some added background information for the highly technical or uncommon jorgons/names used in the news.
Make it very noob friendly. Feel free to use internet for gaining knowledge but dont tell me sources.
Keep everything in a paragraph:
"""