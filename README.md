
# Network Packet Sniffer with Alert System
A Python-based real-time network packet sniffer with anomaly detection and live traffic visualization. This project helps detect suspicious activities like port scanning or flooding by monitoring packet behavior on a local network.

## 🔧 Tools & Technologies Used

- **Python 3.10**
- **Scapy** – For capturing network packets
- **SQLite3** – For storing packet logs
- **Matplotlib** – For real-time traffic graphing
- **Threading** – To run sniffer and graph together

## 📂 Project Structure
network-packet-sniffer-with-alert-system/
│
├── sniffer.py # Captures live packets
├── database.py # Saves packet data into SQLite
├── alert.py # Detects anomalies and raises alerts
├── visualize.py # Real-time graphing using matplotlib
├── main.py # Runs sniffer and graph in parallel
└── README.md # Project overview (this file)

## 🧪 How to Run

1. **Install the required libraries:**
pip install scapy matplotlib
Run the project:python main.py

## Features:
Live packet sniffing
Detection of flooding or scanning behavior
Alerts shown in terminal
Real-time graph updates every 5 seconds

## Example Output
Terminal Alert:
[ALERT] Possible scan detected from 192.168.0.106 - 2232 packets in 10 seconds
Graph Output:
<img width="473" alt="image" src="https://github.com/user-attachments/assets/e537d205-7b7e-4bf2-bb46-daa86ec769d8" />

✍️ Author
Maheshwari Patil
Internship Project

📌 Notes
traffic.db is not included in the repo. It will be created automatically when the program runs.
You can tweak the alert threshold inside alert.py



