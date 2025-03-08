from bluedot.btcomm import BluetoothClient
from signal import pause

def data_received(data):
    print(data)

c = BluetoothClient("raspberrypi", data_received)
c.send("StartCar")

pause()