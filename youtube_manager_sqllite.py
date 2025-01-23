import sqlite3

con=sqlite3.connect("youtube_manager.db")
cur=con.cursor()
cur.execute('''
            CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration TEXT NOT NULL
            )
''')
def list_videos():
    print("\n Listing all videos...\n")
    cur.execute("SELECT * FROM videos")
    result=cur.fetchall()
    if len(result)==0:
        print(" *" * 70)
        print("\nNo videos found!\n")
        print(" *" * 70)
        return
    print(" *" * 70)
    nums=1
    for row in result:
        print(f"{nums}- Id: {row[0]} | Name: {row[1]} | Duration: {row[2]}")
        nums+=1
    print(" *" * 70)
def add_video(name,duration):
    
    cur.execute("INSERT INTO videos(name,duration) VALUES(?,?)",(name,duration))
    con.commit()
    
    print("\n Video added successfully!\n")
    
def update_video(video_id,new_name,new_duration):

        """
        Updates the name and/or duration of a video in the database.
        Parameters:
        video_id (int): The unique identifier of the video to be updated.
        new_name (str): The new name for the video. If None, the name will not be updated.
        new_duration (int): The new duration for the video in seconds. If None, the duration will not be updated.
        Returns:
        None
        """
    # it's one way to upate the video
    # if new_name and new_duration:
    #     cur.execute("UPDATE videos SET name=?, duration=? WHERE id=?", (new_name, new_duration, video_id))
    # elif new_name:
    #     cur.execute("UPDATE videos SET name=? WHERE id=?", (new_name, video_id))
    # elif new_duration:
    #     cur.execute("UPDATE videos SET duration=? WHERE id=?", (new_duration, video_id))
    # else:
    #     print("No updates provided.")
    #     return
    
    # we have another way to update the video
        if not video_id:
            print("Please provide a video ID.")
            return
        update=[]
        params=[]
        if new_name:
            update.append("name=?")
            params.append(new_name)
        if new_duration:
            update.append("duration=?")
            params.append(new_duration)
        
        update_str=", ".join(update)
        params.append(video_id)
        cur.execute("Update videos SET "+update_str+" where id=?", tuple(params))
        con.commit()
        print("\n Video updated successfully!\n")
def remove_video(video_id):
    if video_id is None:
        print("Please provide a video ID.")
        return
    cur.execute("DELETE FROM videos WHERE id=?",(video_id,))
    con.commit()
    print("\n Video removed successfully!\n")

def main():
    while True:
        print("\n Youtube Manager | Choose an option:\n")
        print("1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Remove video")
        print("5. Exit")
        choice=input("Enter your choice: ")
        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input('Enter the name of the video: ')
            duration=input('Enter the duration of the video: ')
            add_video(name,duration)
        elif choice=='3':
            list_videos()
            Id=input('Enter the id of the video: ')
            name=input('Enter the name of the video: ')
            duration=input('Enter the duration of the video: ')
            update_video(Id,name,duration)
        elif choice=='4':
            list_videos()
            id=input('Enter the id of the video: ')
            remove_video(id)
        elif choice=='5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=='__main__':
    main()