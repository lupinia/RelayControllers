# RelayControllers
Files to control four Sainsmart 16 port USB relay boards from a Raspberry Pi


This is part of a project to integrate a modern control system with a a 1980s GE Low Energy Lighting relay control system.
This relies on four 16 port relay boards attached to a Raspberry Pi 3+.  The frontend runs on a Django server on the Pi and runs the script on the backend.

Don't run this on a public facing server... seriously... it isn't locked down and allows execution of scripts on a local system.  Don't be stupid, use this at your own risk.
