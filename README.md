Sentiment Analysis Project

This project implements a sentiment analysis application using the Groq API for language understanding and TextBlob for sentiment scoring. The application is built with Flask to provide a web-based interface for users to input product reviews and receive sentiment analysis results. The project includes an endpoint for analyzing sentiments and a simple chatbot interface.

Features

Sentiment Analysis:

Uses the Groq API to process user input and generate responses.

TextBlob is employed to calculate sentiment polarity and classify it as positive, negative, or neutral.

Chatbot Interface:

A basic chatbot to handle general queries and echo user inputs.

Error Handling:

Handles various API errors, including invalid API keys, unauthorized access, and unexpected issues.

Provides descriptive error messages for better debugging and user experience.

Project Structure

project-root/
├── src/
│   ├── app.py               # Main Flask application
│   ├── routes.py            # Flask routes for handling requests
│   ├── config/
│   │   └── settings.py      # Configuration file for API keys and endpoints
│   ├── templates/
│   │   └── index.html       # HTML template for the home page
├── .env                     # Environment variables (not included in source control)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

Installation

Prerequisites

Python 3.8 or higher

pip (Python package manager)

Groq API Key

Steps

Clone the Repository:

git clone https://github.com/yourusername/sentiment-analysis.git
cd sentiment-analysis

Set Up Environment:

Create a .env file in the project root with the following content:

GROQ_API_KEY=<your_groq_api_key>

Install Dependencies:

pip install -r requirements.txt

Run the Application:

python src/app.py

Access the Application:

Open your browser and navigate to http://127.0.0.1:5000.

Usage

Navigate to the home page.

Enter a product review in the input field.

Click "Analyze Sentiment" to receive the sentiment classification.

Use the chatbot for additional interactions.

API Details

Analyze Sentiment Endpoint

URL: /analyze_sentiment

Method: POST

Request Body:

{
  "user_input": "The product is amazing!"
}

Response:

{
  "sentiment": "positive 😊",
  "details": "Your detailed analysis..."
}

Chat Endpoint

URL: /chat

Method: POST

Request Body:

{
  "message": "Hello"
}

Response:

{
  "response": "You said: Hello"
}

Dependencies

Flask

requests

TextBlob

python-dotenv

Troubleshooting

Invalid API Key:

Ensure your .env file contains the correct API key.

Verify the API key is active and has the necessary permissions.

Environment Variables Not Loading:

Check that the .env file is in the correct location.

Confirm python-dotenv is installed.

API Errors:

Check the GROQ_API_ENDPOINT in settings.py for correctness.

Inspect error messages for further debugging.

Future Enhancements

Add support for additional models and APIs.

Enhance the chatbot with more advanced NLP capabilities.

Implement a database to store analysis results for future reference.

License

This project is licensed under the MIT License.

Author

Haswin Raj

