from xml.dom import minidom
import os as os
from subprocess import call
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from upload import upload

class EventHandler(FileSystemEventHandler):
    def __init__(self, config, name) -> None:
        self.config = config
        self.name = name

        super().__init__()

    def on_moved(self, event):

        if event.dest_path.endswith(self.name) and not event.dest_path.endswith('original-' + self.name):
            # Uploading to server
            print('Uploading to server')
            upload(self.config, event.dest_path)


class Runner:
    def __init__(self, runtime, config) -> None:
        self.runtime = runtime
        self.config = config
        self.name = ''

        super().__init__()

        pom = minidom.parse(self.config['path'] + 'pom.xml')

        name = pom.getElementsByTagName('artifactId')[0].firstChild.nodeValue + '-' + pom.getElementsByTagName('version')[0].firstChild.nodeValue + '.' + pom.getElementsByTagName('packaging')[0].firstChild.nodeValue

        self.name = name

        # Check if target already exists
        if os.path.isdir(self.config['path'] + 'target'):
            return

        if not os.path.isfile(f"{self.config['path']}target/{name}"):
            call(["mvn clean install"], cwd=self.config['path'], shell=True)
            
            upload(self.config, self.config['path'] + 'target/' + name)


    def startListener(self):
        # Watch directory
        observer = Observer()
        observer.schedule(EventHandler(self.config, self.name), self.config['path'], recursive=True)
        observer.start()

        try:
            while observer.is_alive():
                observer.join(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == '__main__':
    runner = Runner(0, {"path": "/home/johannes/Documents/Dev/Java-Kotlin/replace-spawners/", "server": {"local": True, "serverPath": "/home/johannes/Documents/Minecraft/Testserver 1.20.1/", "adress": "0.0.0.0", "port": 80, "username": "USERNAME", "password": "TEST", "method": "ftp"}})
    runner.startListener()
