from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCollision(ServerResponse):
    def execute(self, data):
        try:
            damage = data.getInt32()

            self.main.emit('ResponseCollision', {'damage': damage})

            self.log('Received [' + str(Constants.SMSG_COLLISION) + '] ResponseCollision')
        except:
            self.log('Bad [' + str(Constants.SMSG_COLLISION) + '] ResponseCollision')
            print_exc()
