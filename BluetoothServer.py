from bluedot.btcomm import BluetoothServer
from signal import pause
import subprocess


def data_received(data):
    print(data)
    
    if(data == "StartCar"):
        s.send("Now Starting Car...")
        result = subprocess.run(['sh', '/home/vignesh/OpenCV_Vignesh_Start.sh'])


s = BluetoothServer(data_received)
pause()
