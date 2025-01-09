🤖 AgentDance News Bot

Welcome to the AgentDance News Bot! This repository contains a Python script designed to fetch, process, and publish news to Twitter, keeping the crypto and tech communities updated with the latest trends. 🚀

🌟 Features
	•	AI-Driven News Processing: Uses OpenAI’s API to analyze and curate news articles.
	•	Daily Automation: Fetches relevant news and posts to Twitter on a schedule.
	•	Customizable Scheduling: Easily configure when to fetch and post news.
	•	Error Handling: Logs errors for smooth operation and debugging.

🛠️ Installation
	1.	Clone the repository:

git clone https://github.com/your-username/agentdance-news-bot.git
cd agentdance-news-bot


	2.	Set up the environment:
	•	Install dependencies:

pip install -r requirements.txt


	•	Create a .env file:

touch .env


	•	Add your OpenAI API key to the .env file:

OPENAI_API_KEY=your_openai_api_key


	3.	Run the bot:

python main.py

🕒 How It Works
	1.	Fetch News: The bot pulls the latest news articles and processes them with the AIDanceNewsProcessor.
	2.	Post to Twitter: News is automatically tweeted using scheduled jobs.
	3.	Scheduler: The script runs jobs daily at predefined times (configurable).

⚙️ Configuration

Schedule Jobs

Edit the main() function in main.py to adjust the posting schedule:

schedule.every().day.at("20:41").do(post_tweet_job)
schedule.every().day.at("21:00").do(post_tweet_job)
schedule.every().day.at("21:30").do(post_tweet_job)

Immediate Testing

Set immediate_test to True to run the fetch and post jobs immediately:

immediate_test = True

🐛 Troubleshooting
	•	OPENAI_API_KEY not found: Ensure your .env file contains the correct API key.
	•	Scheduler Errors: Check your Python environment and ensure all dependencies are installed.

📄 Example Output

Fetching News

[2025-01-08 20:00:00] Starting daily news fetch...
[2025-01-08 20:01:00] Daily news fetch completed.

Posting News

[2025-01-08 21:00:00] Starting news posting job...
[2025-01-08 21:01:00] News posting job completed.

🚀 Contributing

Contributions are welcome! Feel free to fork the repository, create issues, or submit pull requests.

📜 License

This project is licensed under the MIT License.

💡 Let’s keep the world updated—one tweet at a time! 🕺🎉
