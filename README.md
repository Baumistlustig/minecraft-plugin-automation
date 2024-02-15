# Minecraft Plugin Development

## Idee

- Nach Kompilieren des Java-Projekts wird die .jar Datei automatisch auf den Server geladen
- Lokaler & FTP- bzw. SFTP Server unterstützt
- Programm erkennt, wann das Plugin kompiliert wurde
- Durch JSON Konfigurationsdatei werden alle notwendigen Daten festgelegt

## Konfigurationsdatei

- JSON
- Daten:
    - Projekt Pfad
    - lokaler Server Pfad / FTP Zugangsdaten

## Sonstiges

- Kann auf Windows und Linux über Kommandozeile verwaltet werden
- Nutzt watchdog zum überwachen der Dateien
- Lädt automatisches reload plugin auf server
