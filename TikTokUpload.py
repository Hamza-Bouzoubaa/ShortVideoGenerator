from Tiktok_uploader import uploadVideo


def TiktokUploads(SessionID,VidPath,title):
    session_id = SessionID
    file = VidPath
    title = title
    tags = ["fyp"]
    #schedule_time = 1672592400

    # Publish the video
    uploadVideo(session_id, file, title, tags, verbose=True)
    # Schedule the video
    #uploadVideo(session_id, file, title, tags, schedule_time, verbose=True)

