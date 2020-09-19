import time
from mpu6050_i2c import *

time.sleep(1) # delay to let mpu6050 to settle

print('recording data')
while True:
    try:
        ax, ay, az, wx, wy, wz = mpu6050_conv()
    except:
        continue

    print('{}'.format('-'*30))
    print('accel [g]: x = {:.2f}, y = {:.2f}, z = {:.2f}'.format(ax, ay, az))
    print('gyro [dps]: x = {:.2f}, y = {:.2f}, z = {:.2f}'.format(wx, wy, wz))
    print('{}'.format('-'*30))
    time.sleep(1)
