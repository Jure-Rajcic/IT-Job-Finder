import scraper.mock as scraper
import filter.mock as filter
import transformer.mock as transformer
import notifier.mock as notifier

# TODO make something that will chek for users in DB and preform this action for them, over proxies to cash localy .

def main():
    # Scrape Facebook group using Apify
    posts = scraper.scrape_facebook_group()

    # Filter posts using AI
    posts = filter.filter_posts(posts)

    # Transform posts with GPT-3
    posts = transformer.transform_posts(posts)

    # Notify user over WhatsApp
    notifier.notify_user(posts, "Alice")

if __name__ == "__main__":
    main()
