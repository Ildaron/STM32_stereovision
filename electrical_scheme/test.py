import time
import serial
import numpy as np
import pandas as pd
import sys
command1 = "?"
start_time = time.time()
count = 0
row_data = []

final_data = pd.DataFrame({"GTL1": [],"GT2": []}) #,"mount_2_1": [],"mount_2_2": [], "beam_1": [],"beam_2": [], "optical_meter": [],"time": []} )

def init_device(com_port):

    name_device = serial.Serial(
    port = com_port,
    baudrate = 4800,
    parity = serial.PARITY_EVEN,
    stopbits = serial.STOPBITS_TWO,
    bytesize = serial.SEVENBITS)
    name_device.isOpen()
    return name_device
com_port = ['COM9','COM12']

name_device_1 = init_device(com_port[0])
name_device_2 = init_device(com_port[1])
#name_device_3 = init_device(com_port)
#name_device_4 = init_device(com_port)
#name_device_5 = init_device(com_port)
#name_device_6 = init_device(com_port)
#name_device_7 = init_device(com_port)
#name_device_8 = init_device(com_port)
while 1 :
    try:
        count += 1   
        for GTL in [name_device_1,name_device_2]:
            GTL.write(b'?\r')
            data = GTL.readline()
            data = data.decode("utf-8")
            #print("data", data)
            spent_time = time.time() - start_time
            row_data.append(float(data))
            
        #print (row_data)
        data_for_pandas = [row_data[0], row_data[1]]
        final_data.loc[count] = data_for_pandas
        print(final_data)
        row_data = []
        
    except KeyboardInterrupt:
            final_data.to_excel('./dataset.xlsx')
            sys.exit()
