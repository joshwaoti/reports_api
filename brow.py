# from gpt4all import GPT4All

# model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
# with model.chat_session():
#     print(model.generate("How can I run LLMs efficiently on my laptop", max_tokens=1024))

from datetime import datetime, timedelta

yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
print(yesterday.split('-')[-1])


yesterday_date = datetime.strptime(yesterday, "%Y-%m-%d").strftime("%d-%b-%Y")
print(yesterday_date)
