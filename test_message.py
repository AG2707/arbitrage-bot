# Import necessary libraries
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Test reading the variables
print("Testing .env File...")
print("API Key:", os.getenv("OXR_API_KEY"))
print("Email User:", os.getenv("EMAIL_USER"))
print("Email Password:", os.getenv("EMAIL_PASS"))

# Check if values are None (this means the .env file isn't being read)
if not os.getenv("OXR_API_KEY"):
    print("❌ ERROR: .env file not found or API Key is missing!")
if not os.getenv("EMAIL_USER"):
    print("❌ ERROR: .env file not found or Email User is missing!")
if not os.getenv("EMAIL_PASS"):
    print("❌ ERROR: .env file not found or Email Password is missing!")
