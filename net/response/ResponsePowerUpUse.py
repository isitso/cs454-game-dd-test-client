from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponsePowerUpUse(ServerResponse):
    def execute(self, data):
        try:
            username = data.getString()
            powerId = data.getInt32()

            self.main.emit('ResponsePowerUpUse', {'username': username, 'powerId': powerId})

            self.log('Received [' + str(Constants.SMSG_POWER_UP) + '] ResponsePowerUpUse')
        except:
            self.log('Bad [' + str(Constants.SMSG_POWER_UP) + '] ResponsePowerUpUse')
            print_exc()
