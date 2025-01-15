import requests
    import os

    # Load environment variables from .env file
    from dotenv import load_dotenv
    load_dotenv()

    # Get the API URL from environment variable
    API_URL = os.getenv("API_URL")

    def query(payload):
        response = requests.post(API_URL, json=payload)
        return response.json()

    output = query({
        "question": "Hey, how are you?",
    })

    print(output)
