from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Create the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

system_message = "Enter your system message here."
prompt = "wtite your prompt here."


response = client.responses.create(
    model="gpt-5",

    input=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ],
    reasoning={"effort": "high"}, # options: "minimal", "low", "medium" (default), "high"
    text={"verbosity": "high"}  # options: "low", "medium" (default), "high"


)

print(response.output_text)