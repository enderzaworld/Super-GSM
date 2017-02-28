from gpiozero import LightSensor, Buzzer
from time import sleep

buzzer = Buzzer(19)
ldr = LightSensor(5)


while True:
    sleep(0.1)
    if ldr.value < 0.5:
        buzzer.on()
        sleep(10)
    else:
        buzzer.off()
