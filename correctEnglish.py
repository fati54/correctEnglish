import os
import openai
import json
import argparse

parser = argparse.ArgumentParser(description='OpenAI Text Correction')
parser.add_argument('-i', '--input', default='input.txt', help='input file name')
parser.add_argument('-o', '--output', default='output.txt', help='output file name')
args = parser.parse_args()

# Option 1 : Use a configuration file: You can create a separate configuration file that contains your API key,
#  and then read it in your code. This way, the key is not stored in the code itself,
#  and can be easily updated or changed. You could use a json or yaml file.
with open("config.json") as json_file:
    config = json.load(json_file)

openai.api_key = config["openai_api_key"]

# Option 2: Use the OPENAI_API_KEY environment variable
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Read the input text from a file
with open(args.input, "r") as file:
    prompt = file.read()

# Get the corrected text from OpenAI API
''' 
here is an explanation of each of the parameters used:

- model: The name of the model to use for the completion. In this case, it's "text-davinci-003", which is a very large and powerful language model trained by OpenAI.
- prompt: The input text that the model will use to generate a response. The value of this variable is not shown in the code snippet.
- temperature: Controls the "creativity" or "divergence" of the model's output. A higher temperature will result in more varied and diverse responses, while a lower temperature will produce responses that are more similar to the training data. In this case, it is set to 0.
- max_tokens: The maximum number of tokens (words or word pieces) that the model will generate in its response. In this case, it is set to 60
- top_p: Controls the proportion of the mass of the distribution that is retained in the generated sequence. 1.0 means that the model will keep all the mass and will generate the sequence of tokens with 100% probability of the most likely tokens.
- frequency_penalty: A value that penalizes the model if it generates tokens that were not frequent in the training data. This can help to reduce repetition and generate more varied output. In this case, it is set to 0.0
- presence_penalty: A value that penalizes the model if it generates tokens that were not present in the input sequence. This can help to ensure that the generated text is relevant to the input prompt. In this case, it is set to 0.0'''


response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

# Write the corrected text to an output file
with open(args.output, "w") as file:
    file.write(response["choices"][0]["text"])
