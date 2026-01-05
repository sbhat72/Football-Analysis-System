from utils import read_video, save_videos
from trackers import Tracker
def main():
    #Read Video
    video_frames = read_video('08fd33_4.mp4')
 
    #Save Video
    save_videos(video_frames,'output_videos/output_video.avi')
    
    #Initialize Tracker 
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames)
    
if __name__ == '__main__':
    main()