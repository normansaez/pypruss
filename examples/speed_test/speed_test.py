import pypruss
import os

print "This example toggles pin P8.12 as fast as it can, 5ns pr cycle."
print "It muxes the pin to mode 6 and does not stop, so use Ctrl-c to end the script."
#P8.12 = gpio_num = 44
gpio_num = 44

#os.system("echo 6 > /sys/kernel/debug/omap_mux/gpmc_ad12")
open("/sys/class/gpio/export","w").write(str(gpio_num))
open("/sys/class/gpio/gpio%d/direction"%gpio_num,"w").write("out")
open("/sys/class/gpio/gpio%d/value"%gpio_num,"w").write("1")


pypruss.modprobe(1000)
pypruss.init()										# Init the PRU
pypruss.open(0)										# Open PRU event 0 which is PRU0_ARM_INTERRUPT
pypruss.pruintc_init()								# Init the interrupt controller
pypruss.exec_program(0, "./speed_test.bin")			# Load firmware "blinkled.bin" on PRU 0
pypruss.wait_for_event(0)							# Wait for event 0 which is connected to PRU0_ARM_INTERRUPT

