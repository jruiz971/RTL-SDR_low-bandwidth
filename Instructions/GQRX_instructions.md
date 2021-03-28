GQRX Instructions 
- When you open gqrx, select the SDR, it has an identifier similar to the following: *Realtek RTK2838 ...*.
- If the option does not appear:
> - Go to */var/log*.
- more syslog
- Identify the string corresponding to the device `To find it easier, disconnect and connect the SDR before running *more syslog*`.
- Once identified (it looks like `/sys/devices/pci0000:00/0000:00:00:14.0/usb1/1-1/rc/rc0/input14/event12`), put the string in the *device string option of gqrx*.

