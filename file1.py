from gtts import gTTS
from mutagen.mp3 import MP3
from moviepy import VideoFileClip, AudioFileClip
import os
import edge_tts

# voice_text = input("What do you want to convert to speech? ")t
voice_text = "Deep in a hidden forest, where golden sunlight danced through emerald leaves, there was a secret waiting for those brave enough to seek it. In a nearby village lived a curious boy named Theo, whose heart sparkled with adventure. One summer day, Theo discovered an ancient map tucked away in his attic. The map promised a treasure that could mend the broken spirits of his community.Determined, Theo ventured into the whispering woods. Along the way, he met gentle woodland creatures that shared hints and kind smiles. They led him through winding trails until he reached a clearing bathed in soft, magical light. At its center stood a luminous fountain, its waters glowing with healing energy.Theo filled a small vial with the enchanted water and hurried back to the village. As he shared the gift, a warm hope spread through every home, reminding everyone that even the smallest acts of courage can transform the world."
VOICE = "en-GB-SoniaNeural"
voice_length = len(voice_text)


if voice_length > 1000 :
    print("The text is too big")
    exit()
    
audio = "test.mp3"
SRT_FILE = "test.srt"

# tts = gTTS(text=voice_text, lang="en",tld="us")
# tts.save(audio)
communicate = edge_tts.Communicate(voice_text, VOICE)
submaker = edge_tts.SubMaker()

with open(audio,"wb") as file:
    for chunk in communicate.stream_sync():
        if chunk["type"] == "audio":
            file.write(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            submaker.feed(chunk)
with open(SRT_FILE, "w", encoding="utf-8") as file:
        file.write(submaker.get_srt())

aux = MP3("test.mp3")
duration = aux.info.length
print(duration)

vid = VideoFileClip("test_video.mp4")

audi = AudioFileClip("test.mp3")

vid = vid.without_audio()

video_with_new_audio = vid.with_audio(audi)

final_video = video_with_new_audio.subclipped(0, audi.duration)

final_video.write_videofile("output_video.mp4")
