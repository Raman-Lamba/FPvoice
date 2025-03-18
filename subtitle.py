from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy import TextClip
from moviepy import CompositeVideoClip
ddd = "./samplefont.ttf"
generator = lambda text: TextClip("./samplefont.ttf",text,font_size=100,stroke_width=2,stroke_color='yellow', color='white',text_align="center",horizontal_align='center', vertical_align='center')
srt_file = "./test.srt"
sub = SubtitlesClip(srt_file,make_textclip = generator, encoding='utf-8')
sub = sub.with_position(("center",0.5),relative=True)
myvideo = VideoFileClip("output_video.mp4")
subbed = CompositeVideoClip([myvideo,sub])
subbed.write_videofile("subbed.mp4", fps=myvideo.fps)
