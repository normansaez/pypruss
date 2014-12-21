PyPRUSS
=======
PyPRUSS is a Python binding for controlling the 
PRUs on BeagleBone. 

For examples and inspiration: [http://hipstercircuits.com/?cat=5](http://hipstercircuits.com/?cat=5)  
 
To install from a package on Angstrom: 
--------------------------------------
[http://wiki.thing-printer.com/index.php?title=PyPRUSS_on_BeagleBone](http://wiki.thing-printer.com/index.php?title=PyPRUSS_on_BeagleBone)
 
To install from source:  
----------
    git clone https://bitbucket.org/intelligentagent/pypruss.git  
    cd pypruss
    python setup.py install
    export LD_LIBRARY_PATH=/usr/local/lib  
  
Note that you must load the uio_pruss kernel module. There is a function for 
loading and unloading this in the library called modprobe() with an optional 
argument for the DDR size. To do it manually its "modprobe uio_pruss". This must be done 
on every boot. 

Update: It appears there is trouble with the pasm compiler. The following might not work..

To try the blinkled example:  
----------------------------
    cd PyPRUSS/examples/blinkled  
    make  
    python blinkled.py  

You should then see three of the user leds blink 10 times. 

There are a few other examples in there as well, have a look at them for other functions.

Enabling /dev/uio* in Ubuntu 13.04
==================================
```bash
git clone https://github.com/normansaez/dtc.git
cd dtc/ && make && sudo cp dtc /usr/local/bin
cd /boot/uboot/dtbs/
sudo cp am335x-boneblack.dtb am335x-boneblack.dtb.backup
sudo dtc -I dtb -O dts am335x-boneblack.dtb > /tmp/am335x-boneblack.dts_orig
sudo mv /tmp/am335x-boneblack.dts_orig .
sudo vim am335x-boneblack.dts_orig # see bellow what to edit
sudo dtc -I dts -O dtb am335x-boneblack.dts_orig > /tmp/am335x-boneblack.dtb
sudo mv /tmp/am335x-boneblack.dtb .
```

In the decompressed file, look for something like this:
```dtb
                pruss@4a300000 {
                        compatible = "ti,pruss-v2";
                        ti,hwmods = "pruss";
                        ti,deassert-hard-reset = "pruss", "pruss";
                        reg = <0x4a300000 0x80000>;
                        ti,pintc-offset = <0x20000>;
                        interrupt-parent = <0x1>;
                        status = "dissable";
                        interrupts = <0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b>;
                        linux,phandle = <0x35>;
                        phandle = <0x35>;
                };
```

and replace:
```
                        status = "dissable";
```
by
```
                        status = "okay";
```

