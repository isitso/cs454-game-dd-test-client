from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestPowerUpUse(ServerRequest):
    def send(self, kwargs):
        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_POWER_UP)
            pkg.addInt32(kwargs['powerId'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_POWER_UP) + '] RequestPowerUpUse')
        except:
            self.log('Bad [' + str(Constants.CMSG_POWER_UP) + '] RequestPowerUpUse')
            print_exc()
