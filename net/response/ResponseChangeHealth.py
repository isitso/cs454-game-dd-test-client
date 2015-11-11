from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeHealth(ServerResponse):
    def execute(self, data):
        try:
            carId = data.getString()
            healthChange = data.getInt32()

            self.main.emit('ResponseChangeHealth', {'carId': carId, 'healthChange': healthChange})

            self.log('Received [' + str(Constants.SMSG_HEALTH) + '] ResponseChangeHealth')
        except:
            self.log('Bad [' + str(Constants.SMSG_HEALTH) + '] ResponseChangeHealth')
            print_exc()
