import instaloader
from tqdm import tqdm
import os
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def download_instagram(usernames, download_photos=False, download_videos=True):
    """
    This function downloads Instagram posts based on the provided parameters.
    """
    for username in usernames:
        try:
            loader = instaloader.Instaloader(download_pictures=download_photos, download_videos=download_videos, download_video_thumbnails=False, download_geotags=False, download_comments=False, save_metadata=False, compress_json=False, post_metadata_txt_pattern="", dirname_pattern=os.path.join(os.getcwd(), 'downloads', '{profile}'))
            profile = instaloader.Profile.from_username(loader.context, username)
            total_posts = profile.mediacount
            progress_bar = tqdm(total=total_posts, desc="Downloading", ncols=100)
            for post in profile.get_posts():
                loader.download_post(post, target=profile.username)
                progress_bar.update(1)
            progress_bar.close()
        except Exception as e:
            logging.error(f"Exception occurred while downloading posts for {username}", exc_info=True)


def validate_input(choice):
    """
    This function validates the user input.
    """
    if choice not in ['1', '2', '3']:
        raise ValueError("Invalid choice. Please enter a number between 1 and 3.")

def menu():
    """
    This function displays the menu to the user.
    """
    print("1. Download Instagram Videos")
    print("2. Download Instagram Photos")
    print("3. Exit")
    choice = input("Enter your choice: ")

    try:
        validate_input(choice)
        if choice in ['1', '2']:
            multiple_users = input("Do you want to download posts from multiple users? (yes/no): ")
            if multiple_users.lower() == 'yes':
                usernames = input("Enter the Instagram usernames (separated by comma): ").split(',')
            else:
                usernames = [input("Enter the Instagram username: ")]
            download_instagram(usernames, download_photos=choice=='2', download_videos=choice=='1')
        elif choice == '3':
            print("Exiting the program...")
            exit()
    except ValueError as e:
        print(e)
        logging.error("Exception occurred", exc_info=True)

if __name__ == "__main__":
    menu()