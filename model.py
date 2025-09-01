from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Create the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_answer(
    prompt: str,
    system_message: str = "You are a helpful code assistant for a business intelligence analyst.",
    reasoning: str = "high",     # options: "minimal", "low", "medium", "high"
    verbosity: str = "high"      # options: "low", "medium", "high"
) -> str:
    """
    Sends a prompt to the OpenAI API and returns the model's response as text.
    
    Arguments:
        prompt (str): The user's input prompt.
        system_message (str): The role/system instruction for the assistant.
        reasoning (str): Effort level for reasoning.
        verbosity (str): Verbosity level for the text output.
    
    Returns:
        str: The model's response or an error message.
    """
    try:
        response = client.responses.create(
            model="gpt-5",
            input=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            reasoning={"effort": reasoning},
            text={"verbosity": verbosity}
        )
        return response.output_text
    except Exception as e:
        return f"Error: {e}"