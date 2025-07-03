import os
from dotenv import load_dotenv
load_dotenv()

# API keys are not needed for local mock version
PORT = os.getenv('PORT')