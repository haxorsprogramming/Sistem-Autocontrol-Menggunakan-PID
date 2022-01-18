from time import sleep
import numpy as np
import pandas as pd

data_driving = pd.read_excel("data_driving.xlsx")

def PID_Controller(Kp=1, Ti=1, t_initial=0, u_bar=0, control_type='pid'):
    print("Inisialisasi ...")
    sleep(1)
    print("Mulai jalan ..")
    arr_data = data_driving.to_numpy()
    # print(arr_data)
    for x in arr_data:
        direction = x[1]
        flow = 'maju'

        if x[1] < x[2]:
            direction = x[2]
            flow = "mundur"
        elif x[2] < x[3]:
            direction = x[2]
            flow = "kiri"
        elif x[3] < x[4]:
            direction = x[3]
            flow = "kanan"

        vTemp = car_dynamics(x[1], x[2], x[3], x[4], x[2])
        print("Result : "+str(vTemp)+" - Arah : "+flow)
        sleep(0.2)

def car_dynamics(b, v_in, u, m, dt):
    temp = (-b*v_in + u)/m
    v_out = temp*dt + v_in
    return v_out

PID_Controller()