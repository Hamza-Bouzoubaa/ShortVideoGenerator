from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import pandas as pd
import moviepy.editor as mp
import openai

from TikTokUpload import TiktokUploads
import os
import uuid
from pytube import YouTube

import whisper
from moviepy.editor import *
from whisper.utils import get_writer

def AudioToText(Audio, model):
    model = whisper.load_model(model)
    result = model.transcribe(Audio, fp16=False)
    
    print("Video transcribed")
    df = pd.DataFrame(columns=['file', 'speaker','start', 'end', 'utterance'])
    text = result["text"]
    result =  (result["segments"])
    for segment in result :
        utterence = (segment["text"])
        start = (segment["start"]) 
        end = (segment["end"]) 

        Row = {"file" : Audio ,"speaker": "NA", "start":start, "end":end,"utterance":utterence}
        df.loc[len(df)] = Row
        
    ExcelFile = "DataFrame.xlsx"
    df.to_excel(ExcelFile,index = False)
    print(f'DataFrame saved to {ExcelFile}')

    


    return text


def download_highest_resolution(video_url):
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the stream with the highest resolution
    stream = yt.streams.get_highest_resolution()

    # Generate a unique filename using UUID
    unique_filename = str(uuid.uuid4())+".mp4"
    video_file_path = os.path.join("videos", f"{unique_filename}")

    # Ensure the "videos" folder exists, create it if it doesn't
    os.makedirs("videos", exist_ok=True)

    # Download the video to the "videos" folder with the unique filename
    stream.download(output_path="videos", filename=unique_filename)

    print("Video downloaded in the highest resolution and saved as:", video_file_path)

    # Convert the video to MP3
    mp3_file_path = os.path.join("videos", "audio.mp3")
    video = VideoFileClip(video_file_path)
    audio = video.audio
    audio.write_audiofile(mp3_file_path)

    print("Video converted to MP3 and saved as:", mp3_file_path)
    print(video_file_path)
    
    return video_file_path


def FindClip(Key,text):
        
    openai.api_key = Key

    # Define the system message
    system_msg = "Your are a professional content creator."
    # Define the user message
    user_msg = user_msg = f"""Please analyze the provided script and identify the most captivating and high-quality segments within {text}:

    1. The clips should be distinct and self-contained, with a minimum duration of 30s and max of 120s.
    2. Each segment should be engaging and have the potential to go viral.
    3. Categorize each clip into one of the following types: Inspirational/Motivational, Funny, or Informative/Documentary.
        

    To ensure a seamless viewing experience, select natural breaks or pauses in the conversation to determine the start and end times for each segment. Additionally, provide a meaningful video title that best represents the content of that segment.

    Here's the format I need for the output:

    | Start Time (s) | End Time (s) | Video Title | Clip Type | 
    |----------------|------------|------------|-----------|

    For example:
    best clips:
    | 30.2s | 64.3s | "Achieving the Impossible" | Inspirational |
    | 150s | 190s | "Hilarious Comedy Skit" | Funny |
    |------|----------|------------------------|-----------|

    Please provide me with the best clips.

    Thank you for your assistance!"""




    
    

    # Create a dataset using GPT
    response = openai.ChatCompletion.create(model="gpt-4",
                                            messages=[{"role": "system", "content": system_msg},
                                                      {"role": "user", "content": user_msg}])

    return response.choices[0].message['content']
    

def GetTextDataFrame():
    dataFrame = "DataFrame.xlsx"
    text=""
    # Read the XLSX file into a DataFrame
    data = pd.read_excel(dataFrame)
    utterance = data["utterance"]
    start = data["start"]
    end = data["end"]

    for i in range(len(data["utterance"])):
        text += f" {start[i]}s to {end[i]}s: {utterance[i]} \n"
        
    return(text)

def SavingSegmentsToDataframe(segments):
    rows = segments.split("\n")
        #print((rows[17]))
    df = pd.DataFrame(columns=[ 'start time','end time','title'])
    Row = { "start time":"____","end time":"____","title" :"____"}
    df.loc[len(df)] = Row

    for i in range(1,len(rows),1):
        try:
            row = rows[i]
            content = (row.split("|"))
            print(content)
            start = float(content[1].replace('s', '').strip())
            Row = { "start time":content[1],"end time":content[2],"title" :content[3]}
            df.loc[len(df)] = Row
            
        except:
            print("couldn't catch:")
            print(content)

    ExcelFile = "Segments.xlsx"
    df.to_excel(ExcelFile,index = False)
    print(f'Segments saved to {ExcelFile}')
    
def CreateSubDataFrames(DataFrame, Segments, output_dir):
    # Load the Segments and DataFrame
    df_segments = pd.read_excel(Segments)  # Skip the header row
    df_data = pd.read_excel(DataFrame)

    sub_dataframes = []

    # Iterate through the segments and extract corresponding data
    for i in range(len(df_segments)):
        start_time_str = df_segments.iloc[i]['start time'].replace('s', '').strip()
        end_time_str = df_segments.iloc[i]['end time'].replace('s', '').strip()

        # Check for non-numeric values and skip them
        if not start_time_str.replace(".", "").isdigit() or not end_time_str.replace(".", "").isdigit():
            continue

        start_time = float(start_time_str)
        end_time = float(end_time_str)

        # Extract rows within the specified time range
        sub_df = df_data[(df_data['start'] >= start_time) & (df_data['end'] <= end_time)]

        sub_dataframes.append(sub_df)

        # Save the sub-DataFrame to an Excel file
        sub_df.to_excel(f"{output_dir}/sub_dataframe_{i}.xlsx", index=False)

    return sub_dataframes

def CutSegments(File, videoPath):
    # Read the Excel file and create a DataFrame
    df = pd.read_excel(File)
    start = []
    end = []
    
    for i in range(1,len(df["start time"]),1):
        start.append(float(df["start time"][i].replace('s',"").strip()))
        end.append(float(df["end time"][i].replace('s',"").strip()))
        

    
    video = videoPath
    video = VideoFileClip(videoPath)

    print(start)
    print(end)
    for i in range(len(start)):
        print(start[i])
        print(end[i])
        cut_video = video.subclip(start[i], end[i])
        
        output_path = os.path.join("segments", f"segment{i}.mp4")
        cut_video.write_videofile(output_path)
        
    return len(start)

def FormatForTikTok(video_path, output_path):
    # Load the video file
    video_clip = VideoFileClip(video_path)

    # Resize the video to TikTok's 9:16 aspect ratio (portrait mode)
    tiktok_width, tiktok_height = 720, 1280  # TikTok's preferred resolution
    video_clip = video_clip.resize(height=tiktok_height)

    # Center the resized video on a black background
    background_color = (0, 0, 0)  # Black
    video_clip = video_clip.set_position("center").on_color(color=background_color, size=(tiktok_width, tiktok_height))

    # Export the final TikTok-formatted video
    video_clip.write_videofile(output_path, codec="libx264")      
   

def split_text(text, max_length):
    lines = []
    line = []

    for word in text.split():
        word = word.strip()  # Strip leading and trailing spaces
        if len(' '.join(line + [word])) <= max_length:
            line.append(word)
        else:
            lines.append(' '.join(line))
            line = [word]

    if line:
        lines.append(' '.join(line))

    return lines






def generate_and_burn_subtitles(video_path, excel_file, output_video_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file, header=None, names=['start', 'end', 'utterance'])
    dt = pd.read_excel("Segments.xlsx")
    number = (video_path.replace("segments/TiktokSegment",""))
    number = number.replace(".mp4","")
    number = int(number) + 1
    first_start = float(dt["start time"][number].replace('s',"").strip())
    
    # Load the video
    video_clip = mp.VideoFileClip(video_path)

    subtitle_clips = []

    max_chars_per_line = 30  # Maximum characters per line

    for i in range(1, len(df["start"]), 1):
        start_time = df["start"][i] - first_start
        end_time = df["end"][i] - first_start
        subtitle_text = df["utterance"][i]
        # Split text into two lines if it exceeds the maximum character limit
        subtitle_text = split_text(subtitle_text, max_chars_per_line)
        subtitle_text = '\n'.join(subtitle_text)
        

        # Create a TextClip for each subtitle with a custom font and no background
        #text_clip = mp.TextClip(subtitle_text, fontsize=40, color='white', font="Ariel")
        text_clip = mp.TextClip(subtitle_text, color='black', align='Center',bg_color="white" ,fontsize=40, font='Font\RobotoSlab-VariableFont_wght.ttf', method='label')


        # Set the duration and position for the subtitle clip
        text_clip = text_clip.set_start(start_time).set_duration(end_time - start_time)

        # Position the subtitle as needed
        text_clip = text_clip.set_position(("center", 1000))  # You can modify the Y coordinate as needed

        subtitle_clips.append(text_clip)

    # Overlay the subtitle clips on the video
    video_with_subtitles = mp.CompositeVideoClip([video_clip] + subtitle_clips)

    # Write the video with burned-in subtitles to the output file
    video_with_subtitles.write_videofile(output_video_path, codec='libx264')

    print("Subtitles generated and burned into the video successfully.")




def TiktokCuterAndSubs(TiktokCuterAndSubs,NumberOfSegments):
    videos = []
    for i in range(NumberOfSegments):
        videoId = uuid.uuid4()
        FormatForTikTok(f"segments/segment{i}.mp4", f"segments/TiktokSegment{i}.mp4")
        generate_and_burn_subtitles(f"segments/TiktokSegment{i}.mp4",f"output_dataframes/sub_dataframe_{i+1}.xlsx",f"FinalVids/video{i}{videoId}.mp4")
        UploadVideosTiktok(TiktokCuterAndSubs,f"FinalVids/video{i}{videoId}.mp4",i)
        videos.append(f"FinalVids/video{i}{videoId}.mp4")

    return videos



def UploadVideosTiktok(TiktokCuterAndSubs,Video,i):
    titles=[]
    df = pd.read_excel("segments.xlsx")
    for k in range(1,len(df["title"]),1):
        titles.append(df["title"][k])
    print(titles[i])
    TiktokUploads(TiktokCuterAndSubs,Video,titles[i])

 # You can replace with a different language model if needed

def split_text_tokens(text, max_tokens_per_segment):
    import nltk
    from nltk.tokenize import word_tokenize

    nltk.download('punkt')  # Download the NLTK tokenizer data if not already done.

    # Tokenize the input text
    tokens = word_tokenize(text)

    # Initialize variables
    segments = []
    current_segment = []
    current_segment_length = 0

    # Iterate through the tokens
    for token in tokens:
        token_length = len(token)

        # If adding the token to the current segment doesn't exceed the limit
        if current_segment_length + token_length <= max_tokens_per_segment:
            current_segment.append(token)
            current_segment_length += token_length
        else:
            # Start a new segment if adding the token exceeds the limit
            segments.append(' '.join(current_segment))
            current_segment = [token]
            current_segment_length = token_length

    # Add the last segment if there's any remaining text
    if current_segment:
        segments.append(' '.join(current_segment))

    return segments
def pipeline(OpenAIKey,TikTokSessionID,videoURL): 
    
    videoPath = download_highest_resolution(videoURL)
    text = AudioToText("videos/audio.mp3","small")  # can change to tiny/medium/large
    text = GetTextDataFrame()
    texts = split_text_tokens(text,10000)
    for i in range (0,len(texts),1):
        segments = FindClip(OpenAIKey,texts[i])
        print(segments)
        SavingSegmentsToDataframe(segments)
        data_frames = CreateSubDataFrames("DataFrame.xlsx", "Segments.xlsx", "output_dataframes")
        Segments = CutSegments("Segments.xlsx", videoPath)
        VideosPath = TiktokCuterAndSubs(TikTokSessionID,Segments)
        



