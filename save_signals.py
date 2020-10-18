import time
from argparse import ArgumentParser
from mpu6050_i2c import *

time.sleep(1) # delay to let mpu6050 to settle

def save_signal(filepath, total_time=2, t_delta=0.01):
    f = open(filepath, 'w')
    n_steps = int(total_time / t_delta)
    print('start')
    for i in range(n_steps):
        try:
            ax, ay, az, wx, wy, wz = mpu6050_conv()
        except:
            continue

        f.write('{}\n'.format(t_delta * i))
        f.write('accel [g]: x = {}, y = {}, z = {}\n'.format(ax, ay, az))
        f.write('gyro [dps]: x = {}, y = {}, z = {}\n'.format(wx, wy, wz))
        time.sleep(t_delta)
    print('end')
    f.close()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', required=True, help='filepath')
    parser.add_argument('-tt', required=False, help='total time')
    parser.add_argument('-td', required=False, help='time delta')
    args = parser.parse_args()

    save_signal(args.f)