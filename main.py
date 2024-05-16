from auto_gpt import AutoGPT
import os


MAIL = os.getenv('GPT_MAIL')
PASS = os.getenv('GPT_PASS')

if MAIL and PASS:
    print("GPT_MAIL and GPT_PASS are available!")
else:
   print("GPT_MAIL or GPT_PASS not available...!") 
   exit()

MAIN_URL="https://chatgpt.com/"

LOGIN_METHOD = ("login_normal","login_with_google")[0] # choose your option

LOGIN_NEEDE = False

# Example usage:
auto_gpt = AutoGPT(MAIN_URL, MAIL, PASS, LOGIN_METHOD,LOGIN_NEEDE)
conversation_list = auto_gpt.enter_prompt("what is the value of 233 + 67?")

print("Conversation list:", conversation_list)
auto_gpt.quit()