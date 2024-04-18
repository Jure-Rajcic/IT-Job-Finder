# 45$ per month
# https://console.apify.com/actors/2chN8UQcH1CfxLRNE/console
# https://console.apify.com/account/integrations


# https://www.facebook.com/groups/2158108910905022/
# https://www.facebook.com/groups/1470658223200432/
# https://www.facebook.com/groups/1872700822929795/


import os
from dotenv import load_dotenv
from apify_client import ApifyClient


def scrape_facebook_group():
    # Load environment variables from .env file
    load_dotenv()

    # Access your API key
    APIFY_API_KEY = os.getenv('APIFY_API_KEY')
    if APIFY_API_KEY is None:
        raise ValueError("API key is not set in environment variables")

    # Initialize the ApifyClient with your API token
    client = ApifyClient(APIFY_API_KEY)

    # Prepare the Actor input on today's date
    run_input = {
        "startUrls": [{ "url": "https://www.facebook.com/groups/2158108910905022" }],
        "resultsLimit": 2, # TODO somhow make them fetch posts from whole week
        "viewOption": "CHRONOLOGICAL",
    }

    # Run the Actor and wait for it to finish
    run = client.actor("2chN8UQcH1CfxLRNE").call(run_input=run_input)

    # Fetch and store Actor results from the run's dataset (if there are any)
    results = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        results.append(item)

    # Return the results
    return results