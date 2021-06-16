import requests
import json
from pprint import pprint

video_id = 'SW14tOda_kI'

WATCH_URL = 'https://www.youtube.com/watch?v={video_id}'

http_client = requests.Session()


def get_html():
    return http_client.get(WATCH_URL.format(video_id=video_id)).text.replace(
        '\\u0026', '&'
    ).replace(
        '\\', ''
    )


def _extract_captions_json(html, video_id):
    splitted_html = html.split('"captions":')

    if len(splitted_html) <= 1:
        if 'class="g-recaptcha"' in html:
            print("TooManyRequests(video_id)")
        if '"playabilityStatus":' not in html:
            print("VideoUnavailable(video_id)")

            print("TranscriptsDisabled(video_id)")

    # print(splitted_html[1])
    captions_json = json.loads(splitted_html[1].split(',"videoDetails')[0].replace('\n', ''))[
        'playerCaptionsTracklistRenderer']
    return captions_json


if __name__ == "__main__":
    pprint(_extract_captions_json(get_html(), video_id))
