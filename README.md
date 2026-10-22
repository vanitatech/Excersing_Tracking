# Exercise Tracking

A command-line exercise tracker that sends exercise descriptions to Nutritionix
and records the resulting activity through Sheety.

## Requirements

- Python 3
- A Nutritionix application ID and API key
- A Sheety endpoint and the authentication details required by your project

Install the dependency with `pip install -r requirements.txt`. Copy
`.env.example` to `.env`, fill in your own values, and load them into the shell
before running either script. For Bash, use `set -a; source .env; set +a`.
Set your own profile values (`ENV_GENDER`, `ENV_WEIGHT_KG`, `ENV_HEIGHT_CM`, and
`ENV_AGE`) for `main2.py`; never commit `.env` or `env.txt`.

Run `python main.py` for the direct exercise tracker or `python main2.py` for
the alternative version. Both scripts make requests to third-party services.