import os
import argparse
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
client = genai.Client(api_key=api_key)


def main():
    print("Hello from bootdevai!")
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

response = client.models.generate_content(
    model='gemini-2.5-pro', contents=args.user_prompt
)
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)
print(response.text)

if __name__ == "__main__":
    main()

if api_key := None:
    raise RuntimeError("API Key nicht gefunden")