from langsmith import Client

client = Client()
prompt_template = client.pull_prompt("news-research-prompt")

RAG_PROMPT = prompt_template.messages[0].prompt.template


print(RAG_PROMPT)
print(type(RAG_PROMPT))  