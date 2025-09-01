from model import get_answer
from tool import read_dataframe
import pandas as pd

system_message = "Write your system message here."

reasoning="high"     # options: "minimal", "low", "medium", "high"
verbosity="high"      # options: "low", "medium", "high"

df = read_dataframe(r"enter your csv route path here", max_rows=25000)
output_route = r"enter your output route path here"

# Prompt: tell the model to query the dataframe and save results
prompt = (
    f"Write your prompt here. For example, analyze the following dataframe and save the results to {output_route}.\n\n"
)

response = get_answer(
    prompt=prompt,
    system_message=system_message,
    reasoning=reasoning,
    verbosity=verbosity
)
print(response)