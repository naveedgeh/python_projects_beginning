import json
def fetch_videos():
    try:
        with open("youtube.txt","r") as file:
            result= json.load(file)
            if len(result)==0:
                return []
            return result
    except FileNotFoundError:
        return []

def list_videos(videos):
    print("\nListing all videos...\n")
    print("*" * 70)
    for index, video in enumerate(videos,start=1):
        print(f"{index} - name:{video["name"]} | duration: {video["time"]}")
    print("\n")
    print("*" * 70)
def add_video(videos):
    print('\nadding video....\n')
    name=input('Enter the name of the video: ')
    duration=input('Enter the duration of the video: ')
    videos.append({"name":name,"time":duration})
    print("\n Video added successfully!\n")
    save_videos(videos)
    fetch_videos()
   


def update_video(videos):
    print("\nUpdating video...\n")
    video_index=int(input("Enter video you want to update: "))
    print(f"Updating video :{videos[video_index -1]["name"]} | {videos[video_index-1]["time"]}")
    name=input("Enter the new name: ")
    duration=input("Enter the new duration: ")
    videos[video_index-1]["name"]=name if name else videos[video_index-1]["name"]
    videos[video_index-1]["time"]=duration if duration else videos[video_index-1]["time"]
    print("\n Video updated successfully!\n")
    save_videos(videos)
    fetch_videos()

def remove_video(videos):
    print("\nRemoving video...\n")
    video_index=int(input("Enter video you want to remove: "))
    print(f"Removing video :{videos[video_index -1]["name"]} | {videos[video_index-1]["time"]}")
    # filtered_videos=[video for index,video in enumerate(videos,start=1) if index!=video_index]
    del videos[video_index-1]
    print("\n Video removed successfully!\n")
    save_videos(videos)
    fetch_videos()
   
def save_videos(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
    
def main():
  videos=fetch_videos()
  while True:

    print("\n Youtube Manager | Choose an option:\n")
    print("1. List all videos")
    print("2. Add a video")
    print("3. Update a video")
    print("4. Remove a video")
    print("5. Exit")

    option = input("Enter your option: ")
    match option:
        case "1":
            list_videos(videos)
        case "2":
            add_video(videos)
        case "3":
            update_video(videos)
        case "4":
            remove_video(videos)
        case "5":
            print("Exiting...")
            break
        case _:
            print("Invalid option. Please try again.")

if __name__=='__main__':
    main()

