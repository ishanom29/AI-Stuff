from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url= os.getenv('BASE_URL'),
  api_key= os.getenv('API_KEY')
)

print('='*40);
print('AI ASSISTANT')
print('='*40);
while True:
  user_input = input("(type 'quit' to exit): ")
  if(user_input=='quit'):
    print("Goodbye!")
    break
  response = client.chat.completions.create(
    model = os.getenv('MODEL'),
    messages = [
      {
        'role':'user',
        'content':user_input
      }
    ]
    
  )
  print(response.choices[0].message.content)