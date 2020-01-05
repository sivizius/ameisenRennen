import serial
import struct
from test import *

CMD_WATCHDOG_TEST                       =   0x10
CMD_CODE_VERSION                        =   0x11

CMD_A2D_BATCH_READ                      =   0x1b
CMD_GPIO_PORT_INPT                      =   0x1e
CMD_GPIO_PIN_INPUT                      =   0x1f

CMD_MONITOR                             =   0x33
CMD_MONITOR1                            =   0x34
CMD_GET_PHASE_I_AD                      =   0x35

CMD_USER_MONITOR1                       =   0x3a
CMD_USER_MONITOR2                       =   0x3b
CMD_USER_MONITOR3                       =   0x3c

CMD_QUIT_IDENTIFY                       =   0x42
CMD_ENTRY_IDENTIFY                      =   0x43
CMD_CHECK_IDENTIFY_STATUS               =   0x44

CMD_GET_PMSM_PARM                       =   0x4b
CMD_WRITE_PMSM_PARM                     =   0x4c
CMD_GET_RESOLVER_INIT_ANGLE             =   0x4d
CMD_GET_HALL_SEQUENCE                   =   0x4e

CMD_ERASE_FLASH                         =   0xb1
CMD_BURNT_FLASH                         =   0xb2
CMD_BURNT_CHECKSUM                      =   0xb3
CMD_BURNT_RESET                         =   0xb4
CMD_CODE_END_ADDRESS                    =   0xb5

CMD_GET_SEED                            =   0xe1
CMD_VALIDATE_SEED                       =   0xe2

CMD_FLASH_OPEN                          =   0xf1
CMD_FLASH_READ                          =   0xf2
CMD_FLASH_WRITE                         =   0xf3
CMD_FLASH_CLOSE                         =   0xf4

TYPE_ASCII                              =   0
TYPE_HEX                                =   1
TYPE_UNSIGNED                           =   2
TYPE_SIGNED                             =   3
TYPE_BITS                               =   4
TYPE_BYTES                              =   5

def typeName          ( type  ):
  if    type  ==  TYPE_ASCII:
    return "ASCII"
  elif  type  ==  TYPE_HEX:
    return "HEX"
  elif  type  ==  TYPE_UNSIGNED:
    return "UNSIGNED"
  elif  type  ==  TYPE_SIGNED:
    return "SIGNED"
  elif  type  ==  TYPE_BITS:
    return "BITS"
  elif  type  ==  TYPE_BYTES:
    return "BYTES"

FIELD_OFFSET                            =   0
FIELD_TYPE                              =   1
FIELD_LENPOS                            =   2
FIELD_NAME                              =   3
FIELD_MIN                               =   4
FIELD_MAX                               =   5
FIELD_VALUE                             =   6
FIELD_EDITABLE                          =   7
FIELD_DESCRIPTION                       =   8

def calculateCheckSum ( command,  data  ):
  return  ( command + len ( data  ) + sum ( data  ) ) & 0xff

def sendCommand       ( socket, command,  data  ):
  checkSum                              =   calculateCheckSum ( command,                          data                          )
  length                                =   len               ( data                                                            )
  rawData                               =   bytes             ( data                                                            )
  message                               =   struct.pack       ( "B{}pB".format  ( length  + 1 ),  command,  rawData,  checkSum  )
  socket.write  ( message     )
  recv                                  =   socket.read ( )
  if  recv  [ 0 ] ==  command:
    length                              =   socket.read ( ) [ 0 ]
    if length > 0:
      result                            =   socket.read ( length )
    else:
      result                            =   [ ]
    check                               =   socket.read ( ) [ 0 ]
    comp                                =   calculateCheckSum ( command, result )
    if  comp  ==  check:
      return  True,   result
    else:
      return  False,  "wrong checksum {}, received {} (difference: {})".format  ( check,    comp, ( check - comp  ) )
  else:
    return    False,  "send command {:02x}, received {:02x}".format             ( command,  recv                    )

def trySendCommand    ( socket, command,  data  ):
  for tries                           in  range ( 5 ):
    success, result                   =   sendCommand ( socket, command,  data  )
    if success == True:
      break
  if success  ==  False:
    print ( "could not send command [ {:02x}, {:02x}, {}, {:02x} ]".format      ( command,  len ( data  ),  data, calculateCheckSum ( command,  data  ) ) )
    return  None
  else:
    return  result

def openSocket        ( port  ):
  if port == "test":
    return  testSocket  ( )
  else:
    with serial.Serial  ( port  )         as  socket:
      socket.baudrate                     =   19200
      socket.bytesize                     =   8
      socket.stopbits                     =   1
      socket.parity                       =   "N"
      return  socket

def getVersion        ( socket  ):
  return  trySendCommand ( socket, CMD_CODE_VERSION, [ ] )
