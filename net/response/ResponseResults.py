from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseResults(ServerResponse):
    def execute(self, data):
        try:
            place = data.getInt32()
            numberOfPlayers = data.getInt32()
            players = []
            for i in range(numberOfPlayers):
                username = data.getString()
                theirPlace = data.getInt32()
                players.append({'username': username, 'place': theirPlace})

            self.main.emit('ResponseResults', {'place': place, 'players': players})

            self.log('Received [' + str(Constants.SMSG_RESULTS) + '] ResponseResults')
        except:
            self.log('Bad [' + str(Constants.SMSG_RESULTS) + '] ResponseResults')
            print_exc()
