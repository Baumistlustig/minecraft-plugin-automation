import shutil

def upload(config, path):
    if config['server']['local']:
        name = path.split('/')
        name = name[len(name) - 1]

        shutil.copyfile(path, config['server']['serverPath'] + 'plugins/' + name)

        print('Uploaded to Server')

if __name__ == '__main__':
    upload(
        {"path": "/home/johannes/Documents/Dev/Java-Kotlin/replace-spawners/", "server": {"local": True, "serverPath": "/home/johannes/Documents/Minecraft/Testserver 1.20.1/", "adress": "0.0.0.0", "port": 80, "username": "USERNAME", "password": "TEST", "method": "ftp"}},
        "/home/johannes/Documents/Dev/Java-Kotlin/replace-spawners/target/replace-block-1.0.jar", 
    )
