import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
  base_url= os.getenv('BASE_URL'),
  api_key= os.getenv('API_KEY')
)
messages = []

print('='*40);
print('AI ASSISTANT')
print('='*40);

while True:
  user_input = input('You: ')
  if user_input == 'quit':
    print('good byeeee')
    break
  
  messages.append(
    {
     'role':'user',
      'content':user_input,
    }
  )
  response = client.chat.completions.create(
    model = os.getenv('MODEL'),
    messages= messages
  )
  ai_message =response.choices[0].message.content
  print('AI: ',ai_message)
  messages.append(
    {
      'role':'assistant',
      'content':ai_message
    }

  )

  print("_______Conversation Histoy________")
  for msg in messages:
    print(f'{msg['role'].title()}:{msg['content']}')
