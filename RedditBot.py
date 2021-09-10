import praw
import os


def writePosts(path):
    with open(path, 'w') as f:
        for post_id in old_posts:
            f.write(post_id + "\n")


# Create a Reddit instance
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("subredditname")  # CHANGE

# file for the posts, they have already been read
if not os.path.isfile("path/to/file.txt"):
    old_posts = []
else:
    with open("path/to/file.txt", "r") as f:  # CHANGE
        old_posts = f.read()
        old_posts = old_posts.split("\n")
        old_posts = list(filter(None, old_posts))

for submission in subreddit.hot(limit=5):  # You can set your limit
    if submission.id in old_posts:
        print("There is no new subreddits.")
        exit()
    else:
        answer = input(
            "There is a new subreddit. Do you want to read it?(yes or no)\n").lower()
        if 'y' in answer:
            print("Title: ", submission.title, "\n")
            print("By: ", submission.author, "\n")
            print(submission.selftext, "\n")
            print("-----------------------------------------------")
            old_posts.append(submission.id)
        elif 'n' in answer:
            con = input("Do you want to continue?(yes or no)\n").lower()
            if 'y' in con:
                continue
            else:
                writePosts("path/to/file.txt")  # CHANGE
                exit()
        else:
            print("Invalid Input.")
            writePosts("path/to/file.txt")  # CHANGE
            exit()

writePosts("path/to/file.txt")  # CHANGE
