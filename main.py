from server_socket import ServerSocket
from pixhawk import Pixhawk
import time
import threading

Sobek = ServerSocket(5555)
Sobek.accept()

while True:
    try:
        pix = Pixhawk()
        print("done")
        break
    except:
        print("No pixhawk connected")

Heeartbeat_thread = threading.Thread(target=pix.heartbeat)
Heeartbeat_thread.start()

while True:
   
    ControlMessage = Sobek.receive(24)
    Sobek.send(pix.get_sensor().encode())

    if ControlMessage is not None:
        pix.ControlPixhawk(ControlMessage)
        print(ControlMessage)

    time.sleep(0.01)
