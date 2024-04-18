def filter_posts(posts):
    filtered_posts = []
    for post in posts:
        text = post["text"].lower()
        if "py" in text:
            filtered_posts.append(post)
    return filtered_posts