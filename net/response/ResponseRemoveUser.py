from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseRemoveUser(ServerResponse):
    def execute(self, data):
        try:
            username = data.getString()

            self.main.emit('ResponseRemoveUser', {'username': username})

            self.log('Received [' + str(Constants.SMSG_REMOVE_CHARACTER) + '] ResponseRemoveUser')
        except:
            self.log('Bad [' + str(Constants.SMSG_REMOVE_CHARACTER) + '] ResponseRemoveUser')
            print_exc()
