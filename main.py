import threading
import sniffer
from visualize import start_graph

# Start sniffing in a thread so UI doesn't block
t = threading.Thread(target=sniffer.main_sniff)
t.daemon = True
t.start()

# Start real-time graph
start_graph()
