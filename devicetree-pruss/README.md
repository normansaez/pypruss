dtc -O dtb -o BB-PRU-00A0.dtbo -b o -@ BB-PRU-00A0.dts
sudo cp BB-PRU-00A0.dtbo /lib/firmware
sudo ln -s /lib/firmware/BB-PRU-00A0.dtbo  /lib/firmware/BB-PRU-00A0-00A0.dtbo
sudo echo BB-PRU-00A0 > /sys/devices/bone_capemgr.9/slots
