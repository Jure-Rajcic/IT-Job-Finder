def notify_user(posts, user):
    print(f"User {user} has {len(posts)} new posts")
    for post in posts:
        print(f"Post: {post['text']}")
        print(f"Link: {post['link']}")
        print("----")