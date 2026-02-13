import json

def load_data():
    try:
        with open('youtube.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(video):
    with open('youtube.json', 'w') as file:
        json.dump(video, file)

def list_all_videos(video):
    if not video:
        print("No videos found.")
        return

    print("\nYour Favourite Videos:")
    for index, vid in enumerate(video, start=1):
        print(f"{index}. {vid['title']} - {vid['link']}")

def add_videos(video):
    title = input("Enter video title: ")
    link = input("Enter video link: ")

    video.append({"title": title, "link": link})
    save_data(video)
    print("Video added successfully!")

def update_videos(video):
    list_all_videos(video)
    if not video:
        return

    try:
        index = int(input("Enter video number to update: ")) - 1
        if 0 <= index < len(video):
            title = input("Enter new title: ")
            link = input("Enter new link: ")

            video[index] = {"title": title, "link": link}
            save_data(video)
            print("Video updated successfully!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_videos(video):
    list_all_videos(video)
    if not video:
        return

    try:
        index = int(input("Enter video number to delete: ")) - 1
        if 0 <= index < len(video):
            deleted = video.pop(index)
            save_data(video)
            print(f"{deleted['title']} deleted successfully!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    video = load_data()

    while True:
        print("\nYouTube Manager || Choose an option")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos(video)

        elif choice == '2':
            add_videos(video)

        elif choice == '3':
            update_videos(video)

        elif choice == '4':
            delete_videos(video)

        elif choice == '5':
            print("Exiting app...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
