from socket   import *
from KBLS0101 import *
from KBLS0102 import *
from KBLS0104 import *
from KBLS0105 import *
from KBLS0106 import *
from KBLS0109 import *
from RYS4812S import *
from KACI0101 import *
from KACI0102 import *
from KACI0103 import *

def decodeFlash ( device, flash ):
  nameA                                 =   "".join ( chr ( char  ) for char  in  flash [ 0 : 3 ] )
  nameB                                 =   nameA [ 0 : 2 ]
  softVersion                           =   ( flash [ 16  ] <<  8 ) + flash [ 17  ]
  config                                =   None
  configName                            =   "????"
  if    nameA ==  "RYS":
    configName                          =   "RYS4812S"
    config                              =   RYS4812S
  elif  nameA ==  "BLS" or  nameB ==  "LS" or nameA == "BSS":
    if    softVersion >=  265:
      configName                        =   "KBLS0109"
      config                            =   KBLS0109
    elif  softVersion >=  262:
      configName                        =   "KBLS0106"
      config                            =   KBLS0106
    elif  softVersion >=  261:
      configName                        =   "KBLS0105"
      config                            =   KBLS0105
    elif  softVersion >=  260:
      configName                        =   "KBLS0104"
      config                            =   KBLS0104
    elif  softVersion >=  258:
      configName                        =   "KBLS0102"
      config                            =   KBLS0102
    elif  softVersion >=  257:
      configName                        =   "KBLS0101"
      config                            =   KBLS0101
    else:
      print("version bullshit 1: ›{}‹".format   ( nameA ) )
  elif  nameA !=  "ACS" and nameB !=  "PS":
    if nameA == "ACI" or nameB == "AC":
      if    softVersion >=  259:
        configName                      =   "KACI0103"
        config                          =   KACI0103
      elif  softVersion >=  258:
        configName                      =   "KACI0102"
        config                          =   KACI0102
      elif  softVersion >=  257:
        configName                      =   "KACI0101"
        config                          =   KACI0101
      else:
        print("version bullshit 2: ›{}‹".format ( nameA ) )
    else:
      print("version bullshit 3: ›{}‹".format   ( nameA ) )
  else:
    print("version bullshit 0: ›{}‹".format     ( nameA ) )
  for field                             in  config:
    if    field [ FIELD_TYPE  ] ==  TYPE_BITS:
      length                            =   1
    else:
      length                            =   field [ FIELD_LENPOS  ]
    value                               =   [ flash [ i ]       for i in range  ( field [ FIELD_OFFSET  ],  field [ FIELD_OFFSET  ] + length  ) ]
    if    field [ FIELD_TYPE  ] ==  TYPE_ASCII:
      field [ FIELD_VALUE ]             =   "".join ( chr ( i ) for i in value                                                                  )
    elif  field [ FIELD_TYPE  ] ==  TYPE_HEX:
      if value  !=  [ 0 ] * length:
        field [ FIELD_VALUE ]           =   int ( value,  16  )
      else:
        field [ FIELD_VALUE ]           =   0
    elif  field [ FIELD_TYPE  ] ==  TYPE_UNSIGNED:
      field [ FIELD_VALUE ]             =   int.from_bytes  ( value,  byteorder = "little", signed  = False )
    elif  field [ FIELD_TYPE  ] ==  TYPE_SIGNED:
      field [ FIELD_VALUE ]             =   int.from_bytes  ( value,  byteorder = "little", signed  = True  )
    elif  field [ FIELD_TYPE  ] ==  TYPE_BITS:
      orMask                            =   1 <<  field [ FIELD_LENPOS  ]
      andMask                           =   255 - orMask
      if  value [ 0 ] & orMask  ==  0:
        field [ FIELD_VALUE ]           =   False
      else:
        field [ FIELD_VALUE ]           =   True
    elif  field[FIELD_TYPE] ==  TYPE_BYTES:
      field [ FIELD_VALUE ]             =   value
  return  configName, config

def encodeFlash ( config,flash):
  for field                             in  config:
    if    field [ FIELD_TYPE  ] ==  TYPE_BITS:
      length                            =   1
    else:
      length                            =   field [ FIELD_LENPOS  ]
    integer                             =   None
    value                               =   field [ FIELD_VALUE ]
    if    field [ FIELD_TYPE  ] ==  TYPE_ASCII:
      integer                           =   False
      value                             =   bytes ( value,                    "ascii" )
    elif  field [ FIELD_TYPE  ] ==  TYPE_HEX:
      integer                           =   False
      value                             =   bytes("{:04x}".format ( value ),  "ascii" )
    elif  field [ FIELD_TYPE  ] ==  TYPE_UNSIGNED or field  [ FIELD_TYPE  ] ==  TYPE_SIGNED:
      integer                           =   True
      min                               =   field [ FIELD_MIN   ]
      max                               =   field [ FIELD_MAX   ]
      if value  > max or  value < min:
        print("warn: value {} = {} ({}) out of bounds [ {}, {} ]".format  ( field [ FIELD_NAME  ],  value, typeName ( field [ FIELD_TYPE  ] ),  min,  max ) )
    elif  field [ FIELD_TYPE  ] ==  TYPE_BITS:
      integer                           =   True
      value                             =   flash [ field [ FIELD_OFFSET  ] ]
      orMask                            =   1 <<  field [ FIELD_LENPOS  ]
      andMask                           =   255 - orMask
      if  field [ FIELD_VALUE ]:
        value                           |=  orMask
      else:
        value                           &=  andMask
    elif  field [ FIELD_TYPE  ] ==  TYPE_BYTES:
      integer                           =   False
    else:
      print ( "unknown type"  )
      return  None
    count                               =   0
    for offset                          in  range ( field [ FIELD_OFFSET  ],  field [ FIELD_OFFSET  ] + length  ):
      if  integer:
        flash [ offset  ]               =   value & 0xff
        value                           >>= 8
      else:
        flash [ offset  ]               =   value [ count ]
        count                           +=  1
  return  flash

def openFlash   ( socket  ):
  return  trySendCommand  ( socket, CMD_FLASH_OPEN, [ ] )

def readFlash   ( socket, length  ):
    flash                               =   [ 0 ] * length
    if  None  ==  openFlash ( socket  ):
      return  [ ]
    for count                           in  range ( int ( ( 15  + length  ) / 16  ) ):
      result                            =   trySendCommand  ( socket, CMD_FLASH_READ, [ ( count * 16  ) & 0xff, 16, ( ( count * 16  ) >>  8 ) & 0xff  ] )
      if    result  ==  None:
        print ( "error while sending" )
        return  [ ]
      elif  len ( result  ) < 16:
        print ( "expected 16 bytes, received {}".format ( len ( result  ) ) )
        return  [ ]
      else:
        for byte                        in  range ( 16  ):
          flash [ 16  * count + byte  ] =   result  [ byte  ]
    if  None  ==  closeFlash  ( socket  ):
      return  [ ]
    return  flash

def sendFlash   ( socket, flash ):
  if  None  ==  openFlash ( socket  ):
    return    False
  for count                             in  range ( 39  ):
    data                                =   [ ( count * 13  ) & 0xff, 13, ( ( count * 13  ) >>  8 ) & 0xff  ]
    for byte                            in  range ( 13  ):
      data                              +=  [ flash [ count * 13  + byte  ] ]
    if  None  ==  trySendCommand  ( socket, CMD_FLASH_WRITE,  data  ):
      return  False
  data                                  =   [ 0xfb,  5,  0x01 ]
  for byte                              in  range ( 5 ):
    data                                +=  [ flash [ 39  * 13  + byte  ] ]
  if  None  ==  trySendCommand  ( socket, CMD_FLASH_WRITE,  data  ):
    return    False
  if  None  ==  closeFlash  ( socket  ):
    return    False
  return      True

def closeFlash    ( socket  ):
  return  trySendCommand  ( socket, CMD_FLASH_CLOSE,  [ ] )
