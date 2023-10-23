from Tiktok_uploader import uploadVideo


def TiktokUploads(VidPath,title):
    session_id = "ad1ec589663bcd13676bbfad0ef72330"
    file = VidPath
    title = title
    tags = ["crazy", "scary", "fyp"]
    #schedule_time = 1672592400

    # Publish the video
    uploadVideo(session_id, file, title, tags, verbose=True)
    # Schedule the video
    #uploadVideo(session_id, file, title, tags, schedule_time, verbose=True)

