from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestCollision(ServerRequest):
    def send(self, kwargs):
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_COLLISION)
            pkg.addInt32(kwargs['playerId'])
            pkg.addInt32(kwargs['damage'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_COLLISION) + '] RequestCollision')
        except:
            self.log('Bad [' + str(Constants.CMSG_COLLISION) + '] RequestCollision')
            print_exc()
