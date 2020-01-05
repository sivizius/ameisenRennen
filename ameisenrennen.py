#!/usr/bin/env python
import pathlib
import sys

from flash    import *
from socket   import *

# These files are derived from the Disassembly of the Android Application by Kelly Controller
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

def isInt       ( value ):
  try:
    int(value)
    return True
  except:
    return False

def getFileName ( ):
  fileName                              =   input ( "/ "  )
  if  fileName  [ 0 ] ==  "~":
    fileName                            =   "{}{}".format ( pathlib.Path.home ( ),  fileName  [ 1 : ] )
  return  fileName

def modifyEntry ( config  ):
  if  config  is  None:
    print ( "config not loaded. _read_ flash and _decode_ first"  )
  else:
    field                               =   int ( command )
    if  field >=  len ( config  ):
      print ( "cannot modify entry {}, because there are only {} entries".format  ( field,  len ( config  ) ) )
    else:
      print ( "Name:            ›{}‹".format                    ( config            [ field ] [ FIELD_NAME        ]   ) )
      print ( "Offset:          0x{:04x}".format                ( config            [ field ] [ FIELD_OFFSET      ]   ) )
      print ( "Length/Position: {}".format                      ( config            [ field ] [ FIELD_LENPOS      ]   ) )
      print ( "Type:            <{}>".format                    ( typeName( config  [ field ] [ FIELD_TYPE        ] ) ) )
      print ( "Minimum:         {}".format                      ( config            [ field ] [ FIELD_MIN         ]   ) )
      print ( "Maximum:         {}".format                      ( config            [ field ] [ FIELD_MAX         ]   ) )
      print ( "Value:           {}".format                      ( config            [ field ] [ FIELD_VALUE       ]   ) )
      print ( "›Editable‹:      {} (will modify anyway)".format ( config            [ field ] [ FIELD_EDITABLE    ]   ) )
      print ( "Description:     ›{}‹".format                    ( config            [ field ] [ FIELD_DESCRIPTION ]   ) )
      print ( "let this empty and press <ENTER> to leave value unchanged")
      value                             =   input ( "= "  )
      fv                                =   FIELD_VALUE
      if    value ==  "True":
        config  [ field ] [ fv  ]       =   True
      elif  value ==  "False":
        config  [ field ] [ fv  ]       =   False
      elif  isInt(value):
        config  [ field ] [ fv  ]       =   int   ( value )
      elif  value !=  "":
        config  [ field ] [ fv  ]       =   value
      else:
        print ( "field unchanged" )
  return  config

def findOption  ( config  ):
  if  config  is  None:
    print ( "config not loaded. _read_ flash and _decode_ first"  )
  else:
    value                               =   input ( "? "  ).lower ( )
    count                               =   0
    for field                           in  config:
      if field  [ FIELD_NAME  ].lower ( ).find  ( value ) !=  -1  or  field [ FIELD_DESCRIPTION ].lower ( ).find  ( value ) !=  -1:
        print( "{:02d}. {}: {} ({})".format ( count,  field [ FIELD_NAME  ],  field [ FIELD_VALUE ],  field [ FIELD_DESCRIPTION ] ) )
      count                             +=  1

def printHelp   ( ):
  print ( "{} [device/test]".format ( sys.argv  [ 0 ] )                                           )
  print ( "Ameisen Rennen is a tool to modify Ameisen."                                           )
  print ( "NO WARRANTIES FOR ANYTHING. ALWAYS MAKE BACKUPS!"                                      )
  print ( "NOT AN OFFICIAL APPLICATION BY KELLY CONTROLLER, JUST A REVERSE ENGINEERED PROGRAMME." )
  print ( "Commands:"                                                                             )
  print ( "<number>:  edit field"                                                                 )
  print ( "(d)ecode:  decode flash to config"                                                     )
  print ( "(e)ncode:  encode config to flash"                                                     )
  print ( "(f)lash:   print flash"                                                                )
  print ( "(h)elp:    print this"                                                                 )
  print ( "(i)mport:  import flash from file"                                                     )
  print ( "(l)ist:    print config"                                                               )
  print ( "(m)ore:    read up to 64 kiB flash from device"                                        )
  print ( "(p)rint:   export config to file"                                                      )
  print ( "(q)uit:    quit"                                                                       )
  print ( "(r)ead:    read flash from device"                                                     )
  print ( "(s)earch:  search for option"                                                          )
  print ( "(w)rite:   write flash to device"                                                      )
  print ( "e(x)port:  export flash to file"                                                       )

def toPrintable ( char  ):
  if  char  >=  0x20  and char  < 0x7f:
    return  chr ( char  )
  else:
    return  "¤"

def listConfig  ( configName, config  ):
  if  config  is  None:
    print ( "config not loaded. _read_ flash and _decode_ first"  )
  else:
    output                              =   ""
    count                               =   0
    for field                           in  config:
      output                            +=  "{:02d}. {}: {} ({})\n".format  ( count,      field [ FIELD_NAME  ],  field [ FIELD_VALUE ],  field [ FIELD_DESCRIPTION ] )
      count                             +=  1
    output                              +=  "Config: {}".format         ( configName                                                                              )
    return  output

if  __name__  ==  "__main__":
  config                                =   None
  configName                            =   ""
  flash                                 =   [ ]
  if len  ( sys.argv  ) > 1:
    device                              =   sys.argv  [ 1 ]
  else:
    device                              =   input ( "$ "  )
  with openSocket ( device  )           as  socket:
    version                             =   getVersion  ( socket  )
    printHelp ( )
    print ( "version: {}".format  ( version ) )
    while True:
      command                           =   input ( "> "  )
      if    isInt ( command ):
        config                          =   modifyEntry ( config  )
      elif  command ==  "d" or  command ==  "decode":
        configName, config              =   decodeFlash ( device, flash )
        print ( "Config: {}".format ( configName  ) )
      elif  command ==  "e" or  command ==  "encode":
        newFlash                        =   encodeFlash ( config, flash )
        if  newFlash  is  not None:
          flash                         =   newFlash
      elif  command ==  "f" or  command ==  "flash":
        if  len ( flash ) ==  0:
          print ( "flash not loaded. _read_ flash first"  )
        else:
          print ( "        {}".format           ( " ".join  ( "{:02x}".format ( byte  ) for byte  in  range ( 32  ) ) ) )
          for line                      in  range ( int ( len ( flash ) / 32  ) ):
            slice                       =   flash [ ( line  ) * 32  : ( line  + 1 ) * 32  ]
            hex                         =   "".join ( " {:02x}".format ( byte ) for byte in slice )
            ascii                       =   "".join ( toPrintable ( byte  )     for byte in slice )
            print ( "0x{:04x}:{} | {}".format  ( line*32,  hex,  ascii ) )
      elif  command ==  "h" or  command ==  "help":
        printHelp ( )
      elif  command ==  "i" or  command ==  "import":
        fileName                        =   getFileName ( )
        with open ( fileName, "rb"  )   as  file:
          flash                         =   list  ( file.read ( ) )
      elif  command ==  "l" or  command ==  "list":
        result                          =   listConfig  ( configName, config  )
        if  result  is  not None:
          print ( result  )
      elif  command ==  "m" or  command ==  "more":
        length                          =   int ( input ( "# "  ) )
        flash                           =   readFlash ( socket, length  )
      elif  command ==  "q" or  command ==  "quit":
        socket.close  ( )
        break
      elif  command ==  "p" or  command ==  "print":
        result                          =   listConfig  ( configName, config  )
        if  result  is  not None:
          fileName                      =   getFileName ( )
          with open(fileName, "w+")     as file:
            file.write(result)
      elif  command ==  "r" or  command ==  "read":
        flash                           =   readFlash ( socket, 512 )
      elif  command ==  "s" or  command ==  "search":
        findOption  ( config  )
      elif  command ==  "w" or  command ==  "write":
        sendFlash ( socket, flash )
      elif  command ==  "x" or  command ==  "export":
        fileName                        =   getFileName ( )
        with open ( fileName, "wb+" )   as  file:
          file.write  ( bytes ( flash ) )
      else:
        print ( "unknown command ›{}‹, these are available:".format ( command ) )
        printHelp ( )
