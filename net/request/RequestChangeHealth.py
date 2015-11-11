from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChangeHealth(ServerRequest):
    def send(self, kwargs):
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_HEALTH)
            pkg.addString(kwargs['username'])
            pkg.addInt32(kwargs['healthChange'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_HEALTH) + '] RequestChangeHealth')
        except:
            self.log('Bad [' + str(Constants.CMSG_HEALTH) + '] RequestChangeHealth')
            print_exc()
