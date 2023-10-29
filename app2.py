

# Install WSL DEBIAN or LINUX in your WIN10
# Open and run command below under WSL to create app2.env file,
#   >> sudo nano app2.env (or .env)
# Copy n paste below content to your env file without '#' and left-handed spaces! (ALL JUSTIFIED LEFT)
#       API_KEY=app2_api_key
#       SECRET_KEY=app2_secret_key
#       DEBUG=True
# Save file ctrl-x, y, ENTER

from dotenv import load_dotenv
import os
import sys

if sys.platform.startswith('linux'):
    print("Running on Linux")
    wsl_env_path = r"app2.env"  # use this format if app run under linux
elif sys.platform.startswith('win'):
    print("Running on Windows")
    # Define the path to the WSL ".env" file using the network share path
    # wsl_env_path = r"\\wsl.localhost\Debian\home\han\.env"
    wsl_env_path = r"\\wsl.localhost\Debian\home\han\app2.env"  # use this format if app run under win10


# Load environment variables from the WSL ".env" file
load_dotenv(dotenv_path=wsl_env_path)

# Access environment variables
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
debug = os.getenv("DEBUG")

print(f"API_KEY: {api_key}")
print(f"SECRET_KEY: {secret_key}")
print(f"DEBUG: {debug}")

E = 1
