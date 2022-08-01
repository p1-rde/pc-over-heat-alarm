#!/usr/bin/env python3
import subprocess as sp
import notify2
import time

while(True):
    cpuTemp = sp.run("sensors | grep -w 'CPU'|awk '{print $2}'", shell=True, capture_output=True)
    cpuTemp = cpuTemp.stdout[0]

    if cpuTemp>50:
        notify2.init('Alarm')
        n = notify2.Notification("Overheat Alarm!",
                                "CPU is "+str(cpuTemp)+"\N{DEGREE SIGN}C",
                                "notification-message-im"
                                )
        n.show()
    time.sleep(300)
