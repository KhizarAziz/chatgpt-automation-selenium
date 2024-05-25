from auto_gpt import AutoGPT

# i have updated the auto_gpt.py script so this sample might not work as expected...!

MAIN_URL="https://chatgpt.com/"

LOGIN_METHOD = ("login_normal","login_with_google")[0] # choose your option

LOGIN_NEEDED = False

# Example usage:
auto_gpt = AutoGPT(MAIN_URL, LOGIN_METHOD, LOGIN_NEEDED)
conversation_list = auto_gpt.enter_prompt("what is the value of 233 + 67?")

print("Conversation list:", conversation_list)
auto_gpt.quit()