import requests
import json
from pprint import pprint

VIDEO_ID = 'SW14tOda_kI'

WATCH_URL = 'https://www.youtube.com/watch?v={video_id}'

HTTP_CLIENT = requests.Session()


def get_html():
    return HTTP_CLIENT.get(WATCH_URL.format(video_id=VIDEO_ID)).text.replace(
        '\\u0026', '&'
    ).replace(
        '\\', ''
    )


def extract_captions_json(html, video_id):
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


def get_caption_track_url(captions_json):
    for track in captions_object['captionTracks']:
        if 'kind' not in track.keys() and track['baseUrl']:
            return track['baseUrl']
        elif 'kind' in track.keys() and track['baseUrl']:
            return track['baseUrl']
        else:
            return ''


if __name__ == "__main__":
    captions_object = extract_captions_json(get_html(), VIDEO_ID)
    pprint(HTTP_CLIENT.get(get_caption_track_url(captions_object)).text)

    # pprint(captions_object)
    # pprint(captions_object['captionTracks'])
    # for track in captions_object['captionTracks']:
    #     print(track['baseUrl']) if 'kind' not in track.keys() else print('Track ')
