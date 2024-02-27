# Minecraft Plugin Development

## Installation

GitHub repository klonen:

```git clone https://github.com/hoellwerth/minecraft-plugin-automation && cd minecraft-plugin-automation```

Installationsskript ausführen:

```sudo sh install.sh```

## Nutzung

### Starten des Service

```mcauto start```

### Stoppen des Service

```mcauto stop```

### Konfigurieren

```mcauto configure <arguments>```

**Argumente:**
- Pfad: `--path <path>`
- Serverpfad: `--serverpath <serverpath>`

## Idee

- Nach Kompilieren des Java-Projekts wird die .jar Datei automatisch auf den Server geladen
- Programm erkennt, wann das Plugin kompiliert wurde
- Durch JSON Konfigurationsdatei werden alle notwendigen Daten festgelegt

## Konfigurationsdatei

- JSON
- Daten:
    - Projekt Pfad
    - lokaler Server Pfad / FTP Zugangsdaten

## Sonstiges

- Kann auf Linux über Kommandozeile verwaltet werden
- Nutzt watchdog zum überwachen der Dateien
- Lädt automatisches reload plugin auf server
