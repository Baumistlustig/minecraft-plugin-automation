from xml.dom import minidom
import os as os
from subprocess import call
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils import changeDir
from upload import upload

class EventHandler(FileSystemEventHandler):
    def __init__(self, config) -> None:
        self.config = config

        super().__init__()

    def on_moved(self, event):
        print(event.src_path, "moved to", event.dest_path)
        
        if event.dest_path.endswith('.jar'):
            # Uploading to server
            print('Uploading to server')
            upload(self.config, event.src_path)



class Runner:
    def __init__(self, runtime, config) -> None:
        self.runtime = runtime
        self.config = config

        super().__init__()

        # Check if target already exists
        if os.path.isdir(self.config['path'] + 'target'):
            print('test')
            return
        pom = minidom.parse(self.config['path'] + 'pom.xml')

        name = pom.getElementsByTagName('artifactId')[0].firstChild.nodeValue + '-' + pom.getElementsByTagName('version')[0].firstChild.nodeValue + '.' + pom.getElementsByTagName('packaging')[0].firstChild.nodeValue

        if not os.path.isfile(f"{self.config['path']}target/{name}"):
            call(["mvn clean install"], cwd=self.config['path'], shell=True)
            
            upload(self.config, self.config['path'] + 'target/' + name)


    def startListener(self):
        # Watch directory
        observer = Observer()
        observer.schedule(EventHandler(self.config), self.config['path'], recursive=True)
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