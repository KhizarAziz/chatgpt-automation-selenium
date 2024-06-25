from auto_gpt import AutoGPT

# i have updated the auto_gpt.py script so this sample might not work as expected...!

LOGIN_METHOD = ("login_normal","login_with_google")[0] # choose your option

LOGIN_NEEDED = False

# Example usage:
auto_gpt = AutoGPT(LOGIN_NEEDED, LOGIN_METHOD)
conversation_list = auto_gpt.enter_prompt("what is the value of 233 + 67? \n") # make sure to append \n as suffix to submit prompt

print("Conversation list:", conversation_list)
auto_gpt.quit()