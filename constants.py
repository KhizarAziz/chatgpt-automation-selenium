import os


MAIL = os.getenv('GPT_EMAIL')
PASS = os.getenv('GPT_PASS')

CHROME_OPTIONS_ARGS = [
    '--no-first-run',
    '--no-service-autorun',
    '--password-store=basic',
    '--user-data-dir=./website-data-cookies-etc',
    '--incognito',
    # '--headless'  # Uncomment if headless mode is desired
]

MAIN_URL="https://chat.openai.com/auth/login"
LOGIN_METHOD = "login_normal" # login_with_google

BASELINE_PROMPT = "Please keep the response in 100 words!" # dummy example, not used yet

DEFAULT_WAIT_BEFORE_ACTION_TIME = [0.5, 1]