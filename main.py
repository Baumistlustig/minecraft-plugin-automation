import os as os
import json
import typer
from typing_extensions import Annotated
from typing import Optional
from ftplib import FTP

app = typer.Typer()

configurationFile = open('config.json')
config = json.load(configurationFile)
configurationFile.close()

working_path = config['path']

@app.command()
def configure(
    path: Annotated[Optional[str], typer.Option()] = working_path,
    local: Annotated[Optional[bool], typer.Option()] = config['server']['local'],
    localServerPath: Annotated[Optional[str], typer.Option()] = config['server']['localServerPath'],
    adress: Annotated[Optional[str], typer.Option()] = config['server']['adress'],
    port: Annotated[Optional[int], typer.Option()] = config['server']['port'],
    username: Annotated[Optional[str], typer.Option()] = config['server']['username'],
    password: Annotated[Optional[str], typer.Option()] = config['server']['password'],
    method: Annotated[Optional[str], typer.Option()] = config['server']['method']):

    file = open('config.json', 'w')

    # Validate input
    if not os.path.isfile(path + 'pom.xml'):
        print('\033[91m' + '\033[1m' + 'Path is not valid!' + '\033[0m')

        file.write(json.dumps(config))

        return
    
    if local:
        if not os.path.isdir(localServerPath + 'plugins'):
            print('\033[91m' + '\033[1m' + 'Local server path is not valid!' + '\033[0m')
            
            return
    else:
        # Try to connect to server
        ftp = FTP(
            adress + ':' + port,
            username,
            password
        )

        if not ftp.login():
            print('\033[91m' + '\033[1m' + 'Server login is not valid!' + '\033[0m')

            return

    file.write(json.dumps({
        "path": path,
        "server": {
            "local": local,
            "localServerPath": localServerPath,
            "adress": adress,
            "port": port,
            "username": username,
            "password": password,
            "method": method
        }
    }))

    file.close()

    print('\033[92m' + '\033[1m' + 'Saved configuration ' + u'\u2713' + '\033[0m')

if __name__ == '__main__':
    app()