# Network-Accessible Input Logger

A Python-based administration tool designed to monitor and log local keyboard inputs for auditing purposes. The application stores the recorded data locally and hosts a background file server to allow remote retrieval within the same local area network (LAN).

**Important**: This tool is developed strictly for **educational purposes, academic research, and authorized security auditing**.

* The author does not condone, support, or encourage the unauthorized or malicious use of this software.

* Users are fully responsible for ensuring compliance with all applicable local, national, and international laws regarding privacy and unauthorized monitoring before deployment.

* Use with caution and only on systems where you have explicit, written authorization.

## Features
* **Input Logging:** Automatically records keyboard interactions and appends them to a local text file.
* **Structured Storage:** Saves all logged content directly into an `output.txt` file inside src folder.
* **Background File Server:** Spawns a background HTTP service to expose the generated log file.
* **Remote Retrieval:** Allows network administrators to access the log file remotely via the machine's local IP address, provided they are on the same LAN.

## System Architecture
1. **Logger Module:** Runs locally to capture keystrokes and continuously append them to `output.txt`.
2. **Server Module:** Initializes a background web server bound to the local network interface, enabling log file downloads or viewing via a web browser.

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Access logs remotely:
   Open your browser and navigate to `http://<TARGET_IP_ADDRESS>:80` from any device connected to the same LAN.