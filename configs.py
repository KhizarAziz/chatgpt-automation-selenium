CHROME_OPTIONS_ARGS = [
    '--no-first-run',
    '--no-service-autorun',
    '--password-store=basic',
    '--user-data-dir=/Users/khizer/Library/Application Support/Google/Chrome', # to use default chrome window
    "--profile-directory=Default",
    '--disable-blink-features=AutomationControlled',
    # '--incognito',
    '--headless',  # Uncomment if headless mode is desired
]

BASELINE_PROMPT = "Please keep the response in 100 words!" # dummy example, not used yet

DEFAULT_WAIT_BEFORE_ACTION_TIME = [2, 5]