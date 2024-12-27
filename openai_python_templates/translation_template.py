# The following code can be used with different openAI models: gpt-3.5-turbo.

from openai import OpenAI

# replace with your key. remember not to share it. 
client = OpenAI(api_key="your api key")

#copy paste your prompt
system_rule = f""" Translate the following text from English to Spanish make sure to use the formal tones. '''' {text_2_translate}''' """
model_selected = 'gpt-3.5-turbo'

#completions endpoint response
def get_response(prompt):
  response = client.chat.completions.create(
    model= model_selected,
    # Assign the role and content for the message
    messages=[
      {
        "role" : "system", "content" : system_rule,
        "role": "user", "content": prompt 
      }], 
    # Can change max token size based on application demand
     max_tokens=100 
    temperature = 0)
  return response.choices[0].message.content

#user input
user_input = input("Please enter the text to translate to Spanish: ") 
input_string_translate = str(user_input)

response = get_response(input_string_translate)
print(response)
