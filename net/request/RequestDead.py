from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestDead(ServerRequest):
    def send(self, kwargs):
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_DEAD)
            pkg.addInt32(kwargs['gameId'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_DEAD) + '] RequestDead')
        except:
            self.log('Bad [' + str(Constants.CMSG_DEAD) + '] RequestDead')
            print_exc()
