import socket

class testSocket:
  def __enter__ ( self  ):
    return self

  def __exit__  ( self, type, value,  traceback ):
    pass

  def __init__  ( self  ):
    self.command                          =   0x00
    self.length                           =   0
    self.data                             =   [   ]
    self.flash                            =   [ 0 ] * 65536
    self.buffer                           =   [   ]

  def read      ( self, length  = 1 ):
    result                                =   self.buffer [         : length  ]
    self.buffer                           =   self.buffer [ length  :         ]
    # print ( "device→: {}".format  ( result  ) )
    return  result

  def write     ( self, data  ):
    # print ( "device←: {}".format  ( data    ) )
    self.command                          =   data  [ 0       ]
    self.length                           =   data  [ 1       ]
    self.data                             =   data  [ 2 : -1  ]
    self.check                            =   data  [ -1      ]
    if len  ( self.data ) !=  self.length:
      print ( "test: write failed, because length of data ({}) and length-field ({}) does not match".format ( len  ( self.data ), self.length                                           ) )
    elif self.check != socket.calculateCheckSum(self.command, self.data):
      print ( "test: write failed, because checksum is wrong: you gave {}, but {} is right".format          ( self.data,          socket.calculateCheckSum  ( self.command, self.data ) ) )
    else:
      if    self.command  ==  socket.CMD_FLASH_READ:
        start                               =   ( self.data [ 2 ] <<  8 ) + self.data [ 0 ]
        stop                                =   start + self.data [ 1 ]
        result                              =   self.flash  [ start : stop  ]
      elif  self.command  ==  socket.CMD_FLASH_WRITE:
        start                               =   ( self.data [ 2 ] <<  8 ) + self.data [ 0 ]
        stop                                =   start + self.data [ 1 ]
        # print ( "{}:{} ({})".format ( start,  stop, self.data [ 1 ] ) )
        count                               =   3
        for byte                            in  range ( start,  stop  ):
          self.flash  [ byte  ]             =   self.data [ count ]
          count                             +=  1
        result                              =   [ ]
      else:
        result                              =   [ ]
      result                                =   [ self.command, len ( result  ) ] + result  + [ socket.calculateCheckSum  ( self.command, result  ) ]
      # print ( "result: {}".format   ( result                        ) )
      self.buffer                           +=  result

  def close     ( self  ):
    pass
