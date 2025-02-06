from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class USBHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        elif '/Volumes' in event.src_path:
            print(f"File {event.src_path} has been transferred to USB device.")

observer = Observer()
observer.schedule(USBHandler(), path='/Volumes', recursive=False)
observer.start()


