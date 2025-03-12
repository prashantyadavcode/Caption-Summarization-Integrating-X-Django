*Caption Summarization and X.com API Integration*

1) System Overview

The Caption Summarization and X.com API Integration project is a Django-based service that processes long Instagram captions and generates concise summaries suitable for posting as tweets on X.com (formerly Twitter). The system integrates an LLM (Large Language Model) for text summarization and the X.com API for automated tweet posting.

Architecture
	1.	The client sends a request containing an Instagram caption.
	2.	The system processes the caption using an LLM to generate a summarized version within the X.com character limit.
	3.	The summarized caption is sent to the X.com API for posting.
	4.	The system returns a structured response confirming the tweet’s successful posting or an error message if the process fails.

2) Setup Instructions

Prerequisites
	•	Python 3.8 or higher
	•	Django 4.0 or higher
	•	pip (Python package manager)
	•	OpenAI or another LLM API key for summarization
	•	X.com Developer account and API credentials for tweet posting
	•	Virtual environment (recommended)

Installation
	1.	Clone the repository using Git.
	2.	Navigate into the project directory.
	3.	Create and activate a virtual environment.
	4.	Install dependencies using the requirements.txt file.
	5.	Create an .env file and add the required API keys for LLM and X.com authentication.
	6.	Apply database migrations.
	7.	Run the development server and access the API via the provided endpoint.

3) Project Structure

The project follows Django’s default structure with a main app named summarizer, responsible for handling caption processing and tweet posting.
	•	The summarizer app contains the necessary files for handling API requests, including views.py for request handling and urls.py for defining API endpoints.
	•	The main Django project directory contains the settings and configuration files.
	•	The .env file stores environment variables required for API authentication.
	•	The requirements.txt file lists all required dependencies for setting up the project.

4) API Endpoints

The API provides two main endpoints:
	1.	Summarization Endpoint
	•	Method: POST
	•	Endpoint: /summarizer/summarize/
	•	Description: Accepts an Instagram caption and returns a summarized version suitable for X.com.
	•	Response Format: Returns a JSON response containing the summarized text.
	•	Error Handling: Returns an error message if the summarization process fails.
	2.	Tweet Posting Endpoint
	•	Method: POST
	•	Endpoint: /summarizer/post-tweet/
	•	Description: Accepts a summarized caption and posts it to X.com.
	•	Response Format: Returns a JSON response confirming the tweet’s successful posting.
	•	Error Handling: If the tweet cannot be posted, an error message is returned in JSON format.

5) Configuration

To update API credentials or modify settings, edit the .env file with the following variables:
	•	OPENAI_API_KEY or another LLM API key
	•	X_API_KEY, X_API_SECRET, and authentication tokens for X.com integration

After making changes, restart the server for the updates to take effect.

6) Deployment

Deploying with Docker
	1.	Build the Docker image using the provided Dockerfile.
	2.	Run the container with the necessary environment variables.
	3.	Access the API at the specified local or deployed URL.

7) Automation

Linux/macOS (Cron Job)

To automate tweet posting at regular intervals, a cron job can be set up to send a request to the tweet posting endpoint periodically.

Windows (Task Scheduler)

The Task Scheduler can be used to execute the script at scheduled intervals by creating a new scheduled task that runs the appropriate command.

Contribution
	•	Fork the repository and create a new branch for any modifications.
	•	Submit pull requests for improvements or bug fixes.
	•	Report any issues via the GitHub Issues section.
