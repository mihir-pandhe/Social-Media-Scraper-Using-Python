import instaloader


def scrape_instagram_profile(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        print(f"Profile Username: {profile.username}")
        print(f"Profile Full Name: {profile.full_name}")
        print(f"Profile Bio: {profile.biography}")
        print(f"Profile Followers: {profile.followers}")
        print(f"Profile Following: {profile.followees}")
        print(f"Profile Posts: {profile.mediacount}")

        for post in profile.get_posts():
            print(f"Post: {post.url}")
            print(f"Caption: {post.caption}")
            print(f"Likes: {post.likes}")
            print(f"Comments: {post.comments}")
            print("-" * 40)

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile {username} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    username = input("Enter the Instagram username: ")
    scrape_instagram_profile(username)


if __name__ == "__main__":
    main()
