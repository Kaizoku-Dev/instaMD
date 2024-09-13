import instaloader
import re

def get_shortcode_from_url(url):
    match = re.search(r'/(p|reel|tv)/([A-Za-z0-9_-]+)/', url)
    if match:
        return match.group(2)
    return None

def download_instagram_post(url):
    L = instaloader.Instaloader(
    download_videos=True,
    download_video_thumbnails=False,
    download_comments=False,
    save_metadata=False,
    post_metadata_txt_pattern=''
    )


    shortcode = get_shortcode_from_url(url)
    
    if shortcode:
        try:
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            L.download_post(post, target="downloads")
            print("Post Downloaded")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid URL or could not extract shortcode.")

while True:
    url = input("Enter the Instagram URL (or type 'exit' to quit): ")
    if url.lower() == 'exit':
        break
    download_instagram_post(url)
