from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestMove(ServerRequest):
    def send(self, kwargs):
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_MOVE)
            pkg.addFloat64(kwargs['x'])
            pkg.addFloat64(kwargs['y'])
            pkg.addFloat64(kwargs['z'])
            pkg.addFloat64(kwargs['h'])
            pkg.addString(kwargs['keys'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_MOVE) + '] RequestMove')
        except:
            self.log('Bad [' + str(Constants.CMSG_MOVE) + '] RequestMove')
            print_exc()
