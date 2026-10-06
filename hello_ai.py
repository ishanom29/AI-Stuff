from openai import OpenAI
from dotenv import load_dotenv
import os #can access the operating system
load_dotenv()
client = OpenAI(
  base_url = os.getenv('BASE_URL'),
  api_key = os.getenv('API_KEY'),
)
response = client.chat.completions.create(
  model=os.getenv('MODEL'),
  messages =[
    {
      'role':'user',
      'content':'Explain me python like 12th year old'
    }
  ]
)
print(response.choices[0].message.content)
