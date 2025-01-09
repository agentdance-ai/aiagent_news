import schedule
import time
from datetime import datetime
import os
import json
import feedparser
from AIDanceNewsProcessor import AIDanceNewsProcessor
from dotenv import load_dotenv


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


load_dotenv()

# 加载 OpenAI API 密钥
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("Error: OPENAI_API_KEY not found in environment variables")

# 初始化处理器类
processor = AIDanceNewsProcessor(openai_api_key=OPENAI_API_KEY)


def fetch_news_job():

    try:
        print(f"[{datetime.now()}] Starting daily news fetch...")
        processor.fetch_relevant_news()
        print(f"[{datetime.now()}] Daily news fetch completed.")
    except Exception as e:
        print(f"[{datetime.now()}] Error in fetch_news_job: {e}")


def post_tweet_job():

    try:
        print(f"[{datetime.now()}] Starting news posting job...")
        processor.publish_news()
        print(f"[{datetime.now()}] News posting job completed.")
    except Exception as e:
        print(f"[{datetime.now()}] Error in post_tweet_job: {e}")


def main():

    immediate_test = False

    if immediate_test:
        print("Starting immediate test...")
        fetch_news_job()
        post_tweet_job()


    schedule.every().day.at("20:41").do(post_tweet_job)
    schedule.every().day.at("21:00").do(post_tweet_job)
    schedule.every().day.at("21:30").do(post_tweet_job)


    print("Scheduler started. Press Ctrl+C to exit.")

    try:
        while True:
            try:
                schedule.run_pending()
                time.sleep(1)
            except Exception as e:
                print(f"[{datetime.now()}] Error in scheduler loop: {e}")
                time.sleep(60)
    except KeyboardInterrupt:
        print("Scheduler stopped.")


if __name__ == "__main__":
    main()