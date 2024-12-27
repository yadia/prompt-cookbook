# OpenAi API Template Collection 
These templates are crafted to cover a wide range of use cases, ensuring you can find the right starting point for your project. Whether you need a conversational agent, a text generator, or a practical tool we have a template for you.
 
> [!NOTE]
> All the templates are written in Python. 

-- 

## Getting Started
To begin using the prompt templates, you will need:

- OpenAi API key. You can get one by signing up at [OpenAI's website]().
- Install openai package on your enviroment.
```
pip install openapi 
```
- Install python3 
```
pip install python3
```
- A basic understanding of how to make API calls to OpenAI. Refer to the OpenAI API documentation for more details.

## Available Templates 
Below is a list of available prompt templates, categorized by their primary use case:
1. Prompt Templates
2. Python Scripts
    _ Content Generation
    _ Summarization
    _ Translation
    _ Segment Analysis

##  How to Use the Templates
1. Select a Template: Choose a template from the list that suits your project needs.
2. Customize the Prompt: Modify the template prompt to better fit your specific use case. Each template comes with placeholders and examples to guide customization.
3. API Call: Use the customized prompt in your API call to OpenAI. 

The prompt section can be copied and pasted directly on ChatGPT. Pick this option if you are looking test the prompt for customization debugging. 

## Open AI Models
There is a variety of Open Ai Models available to use with with different capabilities and price points. 

Models which were used for evaluation purposes of this templates:
| --- | ---- | --- |
| Model | Description | Training Data |
|------- | ------|  ---- |
| GPT-4o | 	The fastest and most affordable flagship model. Multimodal model (accepting text or image inputs and outputting text) that can solve difficult problems with greater accuracy  |  up to 2023 OCT |
| gpt-3.5-turbo | this points to gpt-3.5-turbo-0125, can understand and generate natural language or code and have been optimized for chat | up to 2021 SEP |
| text-moderation-007 | Model which can be used for moderation of comments based on pre-defined categories by Open AI | N/A |


# Best Practices
**Clarity**:Make sure to customize the prompts based on your application and remember to be clear.
**Iteration**: Iteratively refine your prompts based on the responses you receive.
**Context**: Provide sufficient context in the prompts to guide the AI effectively.
**Tokens**: Be mindful of the token limits for both prompts and responses to manage API costs and efficiency. Depending on your application you can toggle the amount of tokens to use per response. Try this during iteration stages. 

--
# System Instructions
This section covers how to create system role instructions. 

## Instruction templates
 > You will be provided with text delimited by triple quotes.
 > If the text does not contain a sequence of instructions then simply write \" Please provide text\"

-- 

# User Prompt Templates for Chat
The prompts on this section can be copy/pasted directly on chatpgt or run via the OpenAI API.

POST request using v1 API.
```
https://api.openai.com/v1/chat/completions

```

### Python Code for prompt
Make sure to add your API key.
```
from openai import OpenAI
client = OpenAI(api_key="_YOUR__KEY__")

user_prompt = " COPY PROMPT" 

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": "{user_prompt}"}
  ]
)

print(completion.choices[0].message)


```

## Creative Content Generation
### Linkedin Post Generator
 Helps generating attractive linkedin post based on the content you want to share. 

  **Prompt** 

 > You are an expert content marketing consultant. You are task with assisting the user with crafting professional linkedIn post using that should sound approacheable, tell a story, and have an engageable call to action. To help the user target better their key audience please modify the tone for {AUDICE TYPE}. 
 The topic of the post should be { POST TOPIC}
 The call to action is asking users to comment their opinion. 

### Instagram Post and Hashtag generator
 Helps creating engabeble and positive captions for your posts. 

-- 

##  Productivity Tools
### Summarizer
 Summarizes long texts into concise summaries.

 **Prompt** 
 >  Please provide in a concise format a summary of the the text provided


### Translation
 Helps you translate from one language to another.

  **User Prompt** 
 > Translate the following text from English to Spanish make sure to use the formal tones.


