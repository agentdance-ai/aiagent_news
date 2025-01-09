🤖 AI Dance News Bot
Show Image
Show Image
An intelligent bot that automatically fetches and posts AI dance-related news 🎭
✨ Features

🔄 Automatically fetches latest AI dance news on schedule
🧠 Intelligent content processing using OpenAI
📢 Automated news posting to social media
⏰ Flexible scheduling mechanism
🛡️ Robust error handling for stable operation

🚀 Getting Started
Prerequisites

Python 3.6+
OpenAI API key
Required Python packages (see requirements.txt)

Installation

Clone the repository:

bashCopygit clone https://github.com/yourusername/ai-dance-news-bot.git
cd ai-dance-news-bot

Install dependencies:

bashCopypip install -r requirements.txt

Configure environment variables:
Create a .env file and add:

CopyOPENAI_API_KEY=your_openai_api_key_here
🎯 Usage
Running the Bot
bashCopypython main.py
The bot will run automatically according to the following schedule:

20:41 - First post
21:00 - Second post
21:30 - Third post

Test Mode
To test functionality immediately, set immediate_test to True:
pythonCopyimmediate_test = True  # in main() function
🛠 Project Structure
Copyai-dance-news-bot/
├── main.py              # Main entry point
├── AIDanceNewsProcessor.py  # Core news processing class
├── .env                 # Environment variables
└── README.md           # Documentation
📝 Configuration

Adjust posting times: Modify schedule.every().day.at() in main.py
Customize processing logic: Update methods in AIDanceNewsProcessor.py
Environment variables: Add required API keys and configs in .env

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details
🙏 Acknowledgments

OpenAI API for intelligent processing
Python Schedule library for task scheduling
Feedparser for RSS parsing

📞 Contact
For questions or suggestions:

Open an issue
Email: [your-email@example.com]
Follow our social media


Made with ❤️ for the AI dance community
