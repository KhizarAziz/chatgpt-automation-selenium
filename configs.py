CHROME_OPTIONS_ARGS = [
    '--no-first-run',
    '--no-service-autorun',
    '--password-store=basic',
    # '--user-data-dir=/Users/khizer/Library/Application Support/Google/Chrome', # to use default chrome window
    '--user-data-dir=./website-data-cookies-etc', # open a fresh tab
    "--profile-directory=Default",
    '--disable-blink-features=AutomationControlled',
    "--remote-debugging-port=9222"
    # '--incognito',

    # '--headless',  # Uncomment if headless mode is desired
    # '--disable-gpu',  # Uncomment if headless mode is desired
    # '--window-size=1920,1080'  # Uncomment if headless mode is desired
]


# "--user-data-dir=/path/to/your/chrome/user/data")


BASELINE_PROMPT = "Please keep the response in 100 words!" # dummy example, not used yet

DEFAULT_WAIT_BEFORE_ACTION_TIME = [5, 10]