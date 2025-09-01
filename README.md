# OpenAI Agent Project

This repository contains a small Python project for working with the OpenAI API, organized as three scripts:

- script/model.py — model-related logic (e.g., wrappers/helpers for OpenAI models).
- script/tool.py — utility functions or “tools” used by the project.
- script/orchestrator.py — the entry point that ties everything together and runs the flow.

Note: The exact responsibilities of each file depend on the implementation; open each file for details.

## Prerequisites

- Python 3.9 or newer
- Git
- Git Bash (Windows) or a UNIX-like shell
- An OpenAI API key

## Quick Start (Git Bash on Windows)

1) Clone the repository
```
git clone <your-repo-url>.git
cd <your-cloned-folder>
```

2) Create and activate a virtual environment (Git Bash on Windows)
```
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
```

3) Install dependencies
- If the repo has a requirements.txt:
```
pip install -r requirements.txt
```

- If there’s no requirements.txt, install the minimum expected libraries:
```
pip install openai python-dotenv
```

4) Create a .env file with your OpenAI API key (see next section for how to get a key)
```
# From the project root:
printf "OPENAI_API_KEY=sk-REPLACE_WITH_YOUR_KEY\n" > .env
```

5) Run the orchestrator
```
python script/orchestrator.py
```

If the orchestrator accepts command-line arguments, run:
```
python script/orchestrator.py --help
```

## Creating the .env File

This project expects an environment file named .env in the project root containing your OpenAI API key:

Example .env:
```
OPENAI_API_KEY=sk-REPLACE_WITH_YOUR_KEY
```

Security tips:
- Never commit .env files. Add the following to your .gitignore if it’s not already there:
```
.env
```
- Treat your API key like a password. Rotate it if it’s ever exposed.

If your code does not automatically load .env, ensure it calls python-dotenv early in execution, for example:
```python
# near the top of orchestrator.py (or main entrypoint)
from dotenv import load_dotenv
load_dotenv()
```
Otherwise, export the variable in your shell before running Python:
```
export OPENAI_API_KEY=sk-REPLACE_WITH_YOUR_KEY
```

## How to Get an OpenAI API Key

1) Go to https://platform.openai.com/ and sign in (or sign up).
2) (If required) Set up billing to enable API usage.
3) Navigate to the API keys page: https://platform.openai.com/api-keys
4) Click “Create new secret key,” copy it once, and store it securely.
5) Put it in your .env file as:
```
OPENAI_API_KEY=sk-REPLACE_WITH_YOUR_KEY
```

You can revoke or rotate keys anytime from the same page.

## Working with Git Bash on Windows

- Virtual environment activation:
  - Git Bash on Windows:
    ```
    source .venv/Scripts/activate
    ```
  - To deactivate:
    ```
    deactivate
    ```

- Running the orchestrator:
  ```
  python script/orchestrator.py
  ```

If you prefer running as a module (ensures imports work from project root):
```
python -m script.orchestrator
```

## Troubleshooting

- ModuleNotFoundError or import errors:
  - Make sure you run commands from the project root.
  - Try running with module syntax: `python -m script.orchestrator`
  - Ensure your virtual environment is activated and dependencies are installed.

- OPENAI_API_KEY not found:
  - Verify .env exists at the project root and contains the key.
  - Ensure python-dotenv is installed and `load_dotenv()` is called before reading environment variables.
  - Alternatively, export the key in your shell (`export OPENAI_API_KEY=...`) for the current session.

- Permission or SSL issues on Windows:
  - Update pip and certifi:
    ```
    python -m pip install --upgrade pip certifi
    ```

## Suggested Repository Layout

Your repo may look like this:
```
.
├─ script/
│  ├─ orchestrator.py
│  ├─ model.py
│  └─ tool.py
├─ .env                # not committed
├─ requirements.txt    # if present
└─ README.md
```

If requirements.txt is not present, consider creating one for reproducible installs, for example:
```
openai
python-dotenv
```

## Notes

- Keep your API key private; do not share it in screenshots, code samples, or commits.
- Check orchestrator.py for any CLI flags, input files, or configuration options specific to your use case.
- For PowerShell users: virtual environment activation differs:
  ```
  .\.venv\Scripts\Activate.ps1
  ```
  But this README focuses on Git Bash per the setup instructions above.

Happy building!
