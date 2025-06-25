import matplotlib.pyplot as plt
import matplotlib.animation as animation
from database import conn
from datetime import datetime, timedelta

packet_counts = []

def get_packet_count_last_n_seconds(n=10):
    cursor = conn.cursor()
    time_limit = (datetime.now() - timedelta(seconds=n)).strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("SELECT COUNT(*) FROM packets WHERE timestamp >= ?", (time_limit,))
    return cursor.fetchone()[0]

def animate(i):
    count = get_packet_count_last_n_seconds(5)
    packet_counts.append(count)
    if len(packet_counts) > 20:
        packet_counts.pop(0)

    plt.cla()
    plt.plot(packet_counts, label="Packets per 5 sec", color="blue")
    plt.xlabel("Time (x 5 sec)")
    plt.ylabel("Packet Count")
    plt.title("Real-Time Network Traffic")
    plt.legend(loc="upper left")
    plt.tight_layout()

def start_graph():
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, animate, interval=5000)  # every 5 seconds
    plt.show()
