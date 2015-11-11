from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerUpPickUp(ServerResponse):
    def execute(self, data):
        try:
            validate = data.getInt32()

            self.main.emit('ResponsePowerUpPickUp', {'validate': validate})

            self.log('Received [' + str(Constants.SMSG_POWER_PICKUP) + '] ResponsePowerUpPickUp')
        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_PICKUP) + '] ResponsePowerUpPickUp')
            print_exc()
