import requests
from marshmallow import fields, Schema, validate, ValidationError
from my_test_app.config import GOOGLE_API_KEY
from pprint import pprint


class YoutubeVideoItems(Schema):
    kind = fields.Str()
    etag = fields.Str()
    id = fields.Str()


class YoutubeVideoPageInfo(Schema):
    totalResults = fields.Int()
    resultsPerPage = fields.Int()


class YoutubeVideo(Schema):
    kind = fields.Str()
    etag = fields.Str()
    items = fields.Nested(YoutubeVideoItems, many=True, validate=validate.Length(min=1))
    pageInfo = fields.Nested(YoutubeVideoPageInfo)


def validate_youtube_id(youtube_id):
    r = requests.get(f'https://www.googleapis.com/youtube/v3/videos?id={youtube_id}&key={GOOGLE_API_KEY}')

    try:
        result = YoutubeVideo().loads(r.text)
        pprint(result)
    except ValidationError as err:
        print(err.messages)
        print(err.valid_data)
        return 'invalid'
    return 'valid'
