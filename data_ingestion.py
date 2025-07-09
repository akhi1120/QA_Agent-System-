# data_ingestion.py
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[-1]
    return url.split("v=")[-1].split("&")[0]

def get_transcript(video_url):
    """Get transcript from YouTube video"""
    try:
        video_id = get_video_id(video_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([line["text"] for line in transcript])
    except Exception as e:
        print(f"Error getting transcript: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    url = "https://www.youtube.com/watch?v=IK62Rk47aas"  # Recruter.ai video
    transcript = get_transcript(url)
    if transcript:
        with open("transcript.txt", "w", encoding="utf-8") as f:
            f.write(transcript)
        print("Transcript saved to transcript.txt")