import instaloader
import pandas as pd
from datetime import datetime


def func(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        profile_data = {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Bio": profile.biography,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Posts": profile.mediacount,
        }

        for key, value in profile_data.items():
            print(f"{key}: {value}")

        posts_data = []
        for post in profile.get_posts():
            post_info = {
                "URL": post.url,
                "Caption": post.caption,
                "Likes": post.likes,
                "Comments": post.comments,
                "Hashtags": post.caption_hashtags,
                "Date": post.date_utc.strftime("%Y-%m-%d %H:%M:%S"),
            }
            posts_data.append(post_info)
            loader.download_post(post, target=profile.username)

        df = pd.DataFrame(posts_data)
        df.to_csv(f"{username}_posts.csv", index=False)
        print(f"Saved posts data to {username}_posts.csv")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile {username} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    username = input("Enter the Instagram username: ")
    func(username)


if __name__ == "__main__":
    main()
