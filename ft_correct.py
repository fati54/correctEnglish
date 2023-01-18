import os
import openai
import json
import argparse

def correct_text(input_file, output_file):
    parser = argparse.ArgumentParser(description='OpenAI Text Correction')
    parser.add_argument('-i', '--input', default=input_file, help='input file name')
    parser.add_argument('-o', '--output', default=output_file, help='output file name')
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



    