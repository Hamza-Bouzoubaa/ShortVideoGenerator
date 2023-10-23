from Tiktok_uploader import uploadVideo


def TiktokUploads(VidPath,title):
    session_id = "Your Session ID"
    file = VidPath
    title = title
    tags = ["fyp"]
    #schedule_time = 1672592400

    # Publish the video
    uploadVideo(session_id, file, title, tags, verbose=True)
    # Schedule the video
    #uploadVideo(session_id, file, title, tags, schedule_time, verbose=True)

