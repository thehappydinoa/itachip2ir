"""exception.py"""


class iTachException(Exception):
    """iTachException Exception"""

    def __init__(self, response):
        """init method"""
        message = self.error_handler(response)
        super(iTachException, self).__init__(message)
        self.message = message

    def error_handler(self, response):
        """error handler"""
        if response.startswith("ERR_01"):
            response = self.invalid_error("command. Command not found.")
        elif response.startswith("ERR_02"):
            response = self.invalid_error("module address (does not exist).")
        elif response.startswith("ERR_03"):
            response = self.invalid_error("connector address (does not exist).")
        elif response.startswith("ERR_04"):
            response = self.invalid_error("ID value.")
        elif response.startswith("ERR_05"):
            response = self.invalid_error("frequency value")
        elif response.startswith("ERR_06"):
            response = self.invalid_error("repeat value.")
        elif response.startswith("ERR_07"):
            response = self.invalid_error("offset value.")
        elif response.startswith("ERR_08"):
            response = self.invalid_error("pulse count.")
        elif response.startswith("ERR_09"):
            response = self.invalid_error("pulse data.")
        elif response.startswith("ERR_10"):
            response = "Uneven amount of <on|off> statements."
        elif response.startswith("ERR_11"):
            response = "No carriage return found."
        elif response.startswith("ERR_12"):
            response = "Repeat count exceeded."
        elif response.startswith("ERR_13"):
            response = "IR command sent to input connector."
        elif response.startswith("ERR_14"):
            response = "Blaster command sent to non-blaster connector."
        elif response.startswith("ERR_15"):
            response = "No carriage return before buffer full."
        elif response.startswith("ERR_16"):
            response = "No carriage return."
        elif response.startswith("ERR_17"):
            response = "Bad command syntax."
        elif response.startswith("ERR_18"):
            response = "Sensor command sent to non-input connector."
        elif response.startswith("ERR_19"):
            response = "Repeated IR transmission failure."
        elif response.startswith("ERR_20"):
            response = "Above designated IR <on|off> pair limit."
        elif response.startswith("ERR_21"):
            response = "Symbol odd boundary."
        elif response.startswith("ERR_22"):
            response = "Undefined symbol."
        elif response.startswith("ERR_23"):
            response = "Unknown option."
        elif response.startswith("ERR_24"):
            response = self.invalid_error("baud rate setting.")
        elif response.startswith("ERR_25"):
            response = self.invalid_error("flow control setting.")
        elif response.startswith("ERR_26"):
            response = self.invalid_error("parity setting.")
        elif response.startswith("ERR_27"):
            response = "Settings are locked."
        return response

    def invalid_error(self, message):
        """invalid error"""
        return "Invalid " + message
