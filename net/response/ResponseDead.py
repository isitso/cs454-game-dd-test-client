from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseDead(ServerResponse):
    def execute(self, data):
        try:
            playerId = data.getInt32()

            self.main.emit('ResponseDead', {'playerId': playerId})

            self.log('Received [' + str(Constants.SMSG_DEAD) + '] ResponseDead')
        except:
            self.log('Bad [' + str(Constants.SMSG_DEAD) + '] ResponseDead')
            print_exc()
