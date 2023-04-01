# coding=utf-8
import os
import openai
import cv2

openai.api_key = os.getenv("OPENAI_API_KEY")

print('input prompt:')
gpt_prompt = input()

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print(response)
print(response['choices'][0]['text'])

response = openai.Image.create(
    prompt=gpt_prompt,
    n=4,
    size="512x512"
)
print(response)
#cv2.imwrite('res.jpg',response)
