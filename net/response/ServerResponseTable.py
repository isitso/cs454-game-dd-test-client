from common.Constants import Constants

from net.response.ResponseLogout import ResponseLogout
from net.response.ResponseMove import ResponseMove
from net.response.ResponsePowerUpUse import ResponsePowerUpUse
from net.response.ResponsePowerUpPickUp import ResponsePowerUpPickUp
from net.response.ResponseChangeHealth import ResponseChangeHealth
from net.response.ResponseResults import ResponseResults
from net.response.ResponseRankings import ResponseRankings
from net.response.ResponsePrizes import ResponsePrizes
from net.response.ResponseCollision import ResponseCollision
from net.response.ResponseDead import ResponseDead
from net.response.ResponseRenderCharacter import ResponseRenderCharacter
from net.response.ResponseRemoveUser import ResponseRemoveUser

class ServerResponseTable:
    """
    The ServerResponseTable contains a mapping of all responses for use
    with the networking component.
    """
    responseTable = {}

    def __init__(self):
        """Initialize the response table."""
        #self.add(Constants.SMSG_AUTH, 'ResponseAuth')
        self.add(Constants.SMSG_DISCONNECT, 'ResponseLogout')
        #self.add(Constants.SMSG_REGISTER, 'ResponseRegistration')
        #self.add(Constants.SMSG_FORGOT_PASSWORD, 'ResponseAccountInformation')
        #self.add(Constants.SMSG_CREATE_CHARACTER, 'ResponseCharacterCreation')
        #self.add(Constants.SMSG_CHAT, 'ResponseChat')
        self.add(Constants.SMSG_MOVE, 'ResponseMove')
        self.add(Constants.SMSG_POWER_UP, 'ResponsePowerUpUse')
        self.add(Constants.SMSG_POWER_PICKUP, 'ResponsePowerUpPickUp')
        self.add(Constants.SMSG_HEALTH, 'ResponseChangeHealth')
        #self.add(Constants.SMSG_ENTER_LOBBY, 'ResponseEnterLobby')
        #self.add(Constants.SMSG_ENTER_GAME_LOBBY, 'ResponseEnterGameLobby')
        #self.add(Constants.SMSG_ENTER_GAME_NAME, 'ResponseEnterGameName')
        #self.add(Constants.SMSG_CREATE_LOBBY, 'ReponseCreateLobby')
        #self.add(Constants.SMSG_PRIVATE_CHAT, 'ReponsePrivateChat')
        #self.add(Constants.SMSG_INVITE, 'ResponseInvite')
        #self.add(Constants.SMSG_CAR_CHOICE, 'ResponseCarChoice')
        #self.add(Constants.SMSG_CAR_PAINT, 'ResponseCarPaint')
        #self.add(Constants.SMSG_CAR_TIRES, 'ResponseCarTires')
        #self.add(Constants.SMSG_GARAGE_PURCHASE, 'ResponseGaragePurchase')
        self.add(Constants.SMSG_RESULTS, 'ResponseResults')
        self.add(Constants.SMSG_RANKINGS, 'ResponseRankings')
        self.add(Constants.SMSG_PRIZES, 'ResponsePrizes')
        self.add(Constants.SMSG_COLLISION, 'ResponseCollision')
        self.add(Constants.SMSG_DEAD, 'ResponseDead')
        #self.add(Constants.SMSG_READY, '')
        self.add(Constants.SMSG_RENDER_CHARACTER, 'ResponseRenderCharacter')
        self.add(Constants.SMSG_REMOVE_CHARACTER, 'ResponseRemoveUser')

    def add(self, constant, name):
        """Map a numeric response code with the name of an existing response module."""
        if name in globals():
            self.responseTable[constant] = name
        else:
            print 'Add Response Error: No module named ' + str(name)

    def get(self, responseCode):
        """Retrieve an instance of the corresponding response."""
        serverResponse = None

        if responseCode in self.responseTable:
            serverResponse = globals()[self.responseTable[responseCode]]()
        else:
            print 'Bad Response Code: ' + str(responseCode)

        return serverResponse
