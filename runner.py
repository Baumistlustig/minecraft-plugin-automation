from xml.dom import minidom
import os as os
from subprocess import call
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils import changeDir

class EventHandler(FileSystemEventHandler):

        def on_moved(self, event):
            print(event.src_path, "moved to", event.dest_path)

            if event.dest_path.endswith('.jar'):
                # Uploading to server
                print('Uploading to server')


class Runner:
    def __init__(self, runtime, config) -> None:
        self.runtime = runtime
        self.config = config

        super().__init__()

        # Check if target already exists
        if not os.path.isdir(self.config['path'] + 'target'):
            return
        pom = minidom.parse(self.config['path'] + 'pom.xml')

        if not os.path.isfile(f"{self.config['path']}target/{pom.getElementsByTagName('artifactId')[0].firstChild.nodeValue}-{pom.getElementsByTagName('version')[0].firstChild.nodeValue}.{pom.getElementsByTagName('packaging')[0].firstChild.nodeValue}"):
            with changeDir(self.config['path']):
                call(["mvn", "clean", "install"], shell=True)

    def onModified(self, event):
        print(event.src_path, "modified")


    def startListener(self):
        # Watch directory
        observer = Observer()
        observer.schedule(EventHandler(), self.config['path'] + 'target/', recursive=True)
        observer.start()

        try:
            while observer.is_alive():
                observer.join(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()