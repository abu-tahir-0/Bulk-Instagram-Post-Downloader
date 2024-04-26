# Instagram Bulk Post Downloader

## Overview

This Python script allows you to download Instagram posts (photos and videos) for one or multiple users. It utilizes the Instaloader library to fetch posts from Instagram profiles.

## Prerequisites

- Python 3.x
- Instaloader library: `pip install instaloader`
- Tqdm library: `pip install tqdm`

## Features

- Download Instagram photos or videos (or both) for one or multiple users.
- Simple menu-driven interface for user interaction.
- Error logging for better debugging and error handling.

## How to Use

1. Clone this repository to your local machine.
2. Install the required libraries using pip:

```bash
pip install instaloader tqdm

3. Run the script:

python python instagram_downloader.py

4. Follow the on-screen instructions to choose the desired operation and enter the necessary information.

## Usage Examples

- To download photos from a single user:

1. To Download Instagram Photos
    Enter your choice: 2
    Enter the Instagram username: example_user

2. To download videos from multiple users:
    Enter your choice: 1
    Do you want to download posts from multiple users? (yes/no): yes
    Enter the Instagram usernames (separated by comma): user1,user2,user3


## Note
- Instagram may have rate limits or restrictions on automated access. Use this script responsibly and considerate of Instagram's terms of service.