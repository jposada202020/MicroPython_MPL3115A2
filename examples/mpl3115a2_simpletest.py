# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_mpl3115a2 import mpl3115a2

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
mpl = mpl3115a2.MPL3115A2(i2c)

while True:
    print(f"Pressure: {mpl.pressure:.2f}Hpa")
    print(f"Altitude: {mpl.altitude:.2f}mts")
    print(f"Temperature: {mpl.temperature:.2f}°C")
    print()
    time.sleep(0.5)
