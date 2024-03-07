import pandas as pd
import random
import os
from moviepy.editor import VideoClip, ImageClip, CompositeVideoClip, AudioFileClip, TextClip, VideoFileClip
from moviepy.video.fx.all import crop,resize

df = pd.read_csv('content.csv')

videos_directory = os.listdir("Template-Videos")

bgm_directory = os.listdir("Template-bgm")

def create_video_with_video_bgm_text(video_path, music_path, output_path, quote, heading, duration=5):
    video = VideoFileClip(video_path).subclip(0,duration)
    video = resize(video, height = 1920)
    video = crop(video, x1=1166.6,y1=0,x2=2246.6,y2=1920)
    
    music_clip = AudioFileClip(music_path).subclip(0, duration)

    # Create a heading clip
    heading_clip = TextClip(heading, fontsize=80, size=(video.size[0], None), color='white',font='Caladea-Bold', method="caption")

    heading_clip = heading_clip.set_position(('center', 750))
    heading_clip = heading_clip.set_duration(duration)
    # Create a text clip
    text_clip = TextClip(quote, fontsize=50, size=(video.size[0], None), color='white',font='Caladea-Bold-Italic', method="caption")
    
    # Position the text in the center of the screen
    text_clip = text_clip.set_position(('center', 900))

    # Set the duration of the text clip
    text_clip = text_clip.set_duration(duration)

    video_clip = CompositeVideoClip([video.set_audio(music_clip), heading_clip, text_clip])

    # Set the duration of the video
    video_clip = video_clip.set_duration(duration)

    # Write the video file
    video_clip.write_videofile(output_path, fps=24)  # You can adjust the fps as needed

for index, row in df.iterrows():
    video_path = "Template-Videos/" + random.choice(videos_directory)
    music_path = "Template-bgm/" + random.choice(bgm_directory)
    heading = "Deep Quotes..."
    quote = row['Quote']
    output_path = f"Result/quotes_{index}.mp4"
    # print(quote)
    create_video_with_video_bgm_text(video_path, music_path, output_path, quote, heading)