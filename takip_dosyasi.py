import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Log dosyasının yolu
LOG_FILE = "/home/ubuntu/bsm/logs/changes.json"

# Olayları işlemek için sınıf
class WatcherHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        log_entry = {
            "event_type": event.event_type,
            "src_path": event.src_path,
            "is_directory": event.is_directory,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(LOG_FILE, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    path_to_watch = "/home/ubuntu/bsm/test"
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    print(f"Watching directory: {path_to_watch}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
