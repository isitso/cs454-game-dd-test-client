from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestPowerUpPickUp(ServerRequest):
    def send(self, kwargs):
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_POWER_PICKUP)
            pkg.addInt32(kwargs['powerId'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_POWER_PICKUP) + '] RequestPowerUpPickUp')
        except:
            self.log('Bad [' + str(Constants.CMSG_POWER_PICKUP) + '] RequestPowerUpPickUp')
            print_exc()
