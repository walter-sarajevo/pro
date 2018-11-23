#encoding=utf-8
import serial
import serial.tools.list_ports

class ComCommand(object):
    pass

class Clear(ComCommand):
    pass

class Size16(ComCommand):
    pass

class Size24(ComCommand):
    pass

class Size8(ComCommand):
    pass
