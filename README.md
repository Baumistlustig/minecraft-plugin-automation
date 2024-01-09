# Minecraft Plugin Development

## Idee

- Nach Kompilieren des Java-Projekts wird die .jar Datei automatisch auf den Server geladen
- Lokal & FTP- bzw. SFTP Server unterstützt
- Programm erkennt, wann das Plugin kompiliert wurde
- Durch JSON Konfigurationsdatei werden alle notwendigen Daten festgelegt

## Konfigurationsdatei

- JSON
- Daten:
    - Projekt Pfad
    - lokaler Server Pfad / FTP Zugangsdaten

## Sonstiges

- Programm wird in eine ausführbare Datei kompiliert
- Kann auf Windows und Linux über Kommandozeile verwaltet werden
- Läuft über Linuxservice bzw. Windows Systemdienst