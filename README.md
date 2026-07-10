# 🛡️ Basic Network Sniffer

A Python-based Basic Network Sniffer developed using **Scapy**. This project captures live network packets and displays useful packet information such as source IP, destination IP, protocol type, and payload preview.

This project was developed as part of a **Cyber Security Internship** to understand how data flows through a network and how packets are analyzed.

---

## Features

- Capture live network traffic
- Detect TCP packets
- Detect UDP packets
- Detect ICMP packets
- Display Source IP Address
- Display Destination IP Address
- Display Protocol Type
- Display Packet Payload
- Lightweight and Beginner Friendly

---

## Technologies Used

- Python 3
- Scapy
- Colorama
- Kali Linux

---

## Project Structure

```
Basic-Network-Sniffer/

├── main.py
├── packet_sniffer.py
├── packet_analyzer.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── screenshots/
│   └── Screenshot.png
└── sample_output/
    └── output.txt
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Seajon2002/Basic-Network-Sniffer.git
```

Go to the project directory

```bash
cd Basic-Network-Sniffer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
sudo python3 main.py
```

---

## Sample Output

```
Packet Number : 1

Source IP      : 192.168.1.5

Destination IP : 192.168.0.1

Protocol        : TCP

Payload Preview:
b'...'
```

---

## Learning Objectives

- Understand Packet Sniffing
- Learn TCP/IP Protocol Analysis
- Analyze Network Traffic
- Work with Scapy Library
- Understand Packet Structures

---

## Future Improvements

- Save packets as PCAP
- Export packets to CSV
- Packet filtering
- Protocol statistics
- Command-line arguments
- Real-time dashboard

---

## Author

**Ektearul Haque**

Cyber Security Enthusiast

GitHub:
https://github.com/Seajon2002

