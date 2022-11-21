from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, reqparse
from pytube import YouTube
import os

app = Flask(__name__)
api = Api(app)

# directs where the downloads will be outputted
DIRECTORY = "%s\\output" % os.getcwd()

# video_post_args = reqparse.RequestParser()
# video_post_args.add_argument(
#     "url",
#     type=str,
#     help='Missing Video URL',
#     required=True
# )

# gets a search query and returns all results to user
# class GetVideoResults(Resource):
#     def get(self):

#         videoName = request.args.get('video_name')
#         videoName = videoName.replace(' ', '+')

#         # url = 'https://www.youtube.com/results?search_query=%s+official' % videoName

#         test = 'https://www.youtube.com/watch?v=zNyYDHCg06c'

#         # yt = YouTube(test)
#         # yt = yt.get('mp4')
#         # yt.download('/')

#         # returns results of the search
#         return


# receive a video id to be downloaded and converted to mp4
class DownloadAudioFromVideo(Resource):

    def get(self):

        videoId = request.args.get('id')

        video = YouTube('https://www.youtube.com/watch?v=%s' % videoId).streams.filter(
            file_extension='mp4').get_audio_only()

        video.download(output_path=DIRECTORY)

        return send_from_directory(DIRECTORY, "%s.mp4" % video.title, as_attachment=True)


# api.add_resource(GetVideoResults, "/video_results")
api.add_resource(DownloadAudioFromVideo, "/download")

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=9100)
