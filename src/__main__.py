from utils.youtube import YouTubeDownLoad
from utils.traverse import VideoClass
from utils.urlutils import url_valid
import argparse


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url", help="The url from which the video will be downloaded from"
    )
    parser.add_argument(
        "-y",
        "--type",
        help="Declares the type of url the parser is like",
        choices=["T"],
        required=True,
    )

    youtube_parser = parser.add_argument_group(
        description="This is an argument parser for youtube"
    )
    youtube_parser.add_argument(
        "-A",
        "--audio_only",
        help="Declares whether to sownload the video with or without audio",
        action="store_true",
    )
    youtube_parser.add_argument(
        "-P",
        "--progressive",
        help="Declare out to be progressive or not",
        action="store_true",
    )
    youtube_parser.add_argument(
        "-F", "--file_extention", help="Declare the file extention"
    )
    youtube_parser.add_argument(
        "-S", "--save_directory", help="Directory for download to be saved"
    )
    youtube_parser.add_argument(
        "-N", "--filename", help="filename for the downloaded file"
    )
    youtube_parser.add_argument(
        "-R", "--resolution", help="DEclare the resolution of the downloaded file"
    )
    args = parser.parse_args()
    if url_valid(args.url):
        if args.type == "T":
            print(f"Checking youtube{args}")
            vid = YouTubeDownLoad(
                args.url,
                audio_only=args.audio_only if args.audio_only else False,
                progressive=args.progressive if args.progressive else False,
                filename=args.filename if args.filename else None,
                resolution=args.resolution if args.resolution else "360p",
            )
    # print(url)
    # print("[+] - URL Is Valid" if url_valid(url) else "[-] - URL Is Invalid")


if __name__ == "__main__":
    # there should be option of changing where the videos are downloaded
    cli()
