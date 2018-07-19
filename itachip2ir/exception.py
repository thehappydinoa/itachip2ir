"""exception.py"""


class iTachException(Exception):
    """iTachException Exception"""

    def __init__(self, msg):
        """init method"""
        message = self.error_handler(msg)
        super(iTachException, self).__init__(message)
        self.message = message

    def error_handler(self, msg):
        """error handler"""
        if msg.startswith("ERR_01"):
            msg = self.invalid_error("command. Command not found.")
        elif msg.startswith("ERR_02"):
            msg = self.invalid_error("module address (does not exist).")
        elif msg.startswith("ERR_03"):
            msg = self.invalid_error(
                "connector address (does not exist).")
        elif msg.startswith("ERR_04"):
            msg = self.invalid_error("ID value.")
        elif msg.startswith("ERR_05"):
            msg = self.invalid_error("frequency value")
        elif msg.startswith("ERR_06"):
            msg = self.invalid_error("repeat value.")
        elif msg.startswith("ERR_07"):
            msg = self.invalid_error("offset value.")
        elif msg.startswith("ERR_08"):
            msg = self.invalid_error("pulse count.")
        elif msg.startswith("ERR_09"):
            msg = self.invalid_error("pulse data.")
        elif msg.startswith("ERR_10"):
            msg = "Uneven amount of <on|off> statements."
        elif msg.startswith("ERR_11"):
            msg = "No carriage return found."
        elif msg.startswith("ERR_12"):
            msg = "Repeat count exceeded."
        elif msg.startswith("ERR_13"):
            msg = "IR command sent to input connector."
        elif msg.startswith("ERR_14"):
            msg = "Blaster command sent to non-blaster connector."
        elif msg.startswith("ERR_15"):
            msg = "No carriage return before buffer full."
        elif msg.startswith("ERR_16"):
            msg = "No carriage return."
        elif msg.startswith("ERR_17"):
            msg = "Bad command syntax."
        elif msg.startswith("ERR_18"):
            msg = "Sensor command sent to non-input connector."
        elif msg.startswith("ERR_19"):
            msg = "Repeated IR transmission failure."
        elif msg.startswith("ERR_20"):
            msg = "Above designated IR <on|off> pair limit."
        elif msg.startswith("ERR_21"):
            msg = "Symbol odd boundary."
        elif msg.startswith("ERR_22"):
            msg = "Undefined symbol."
        elif msg.startswith("ERR_23"):
            msg = "Unknown option."
        elif msg.startswith("ERR_24"):
            msg = self.invalid_error("baud rate setting.")
        elif msg.startswith("ERR_25"):
            msg = self.invalid_error("flow control setting.")
        elif msg.startswith("ERR_26"):
            msg = self.invalid_error("parity setting.")
        elif msg.startswith("ERR_27"):
            msg = "Settings are locked."
        return msg

    def invalid_error(self, msg):
        """invalid error"""
        return "Invalid " + msg
