from auto_gpt import AutoGPT

# Example usage:
auto_gpt = AutoGPT()
conversation_list = auto_gpt.enter_prompt("what is the value of 233 + 67?")
auto_gpt.quit()
print(conversation_list[-1])