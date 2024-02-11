from app import app
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    # Change the port number as desired
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))