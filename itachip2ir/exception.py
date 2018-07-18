class iTachException(Exception):
    def __init__(self, response):
        if response.startswith("ERR_01"):
            message = "Invalid command. Command not found."
        elif response.startswith("ERR_02"):
            message = "Invalid module address (does not exist)."
        elif response.startswith("ERR_03"):
            message = "Invalid connector address (does not exist)."
        elif response.startswith("ERR_04"):
            message = "Invalid ID value."
        elif response.startswith("ERR_05"):
            message = "Invalid frequency value"
        elif response.startswith("ERR_06"):
            message = "Invalid repeat value."
        elif response.startswith("ERR_07"):
            message = "Invalid offset value."
        elif response.startswith("ERR_08"):
            message = "Invalid pulse count."
        elif response.startswith("ERR_09"):
            message = "Invalid pulse data."
        elif response.startswith("ERR_10"):
            message = "Uneven amount of <on|off> statements."
        elif response.startswith("ERR_11"):
            message = "No carriage return found."
        elif response.startswith("ERR_12"):
            message = "Repeat count exceeded."
        elif response.startswith("ERR_13"):
            message = "IR command sent to input connector."
        elif response.startswith("ERR_14"):
            message = "Blaster command sent to non-blaster connector."
        elif response.startswith("ERR_15"):
            message = "No carriage return before buffer full."
        elif response.startswith("ERR_16"):
            message = "No carriage return."
        elif response.startswith("ERR_17"):
            message = "Bad command syntax."
        elif response.startswith("ERR_18"):
            message = "Sensor command sent to non-input connector."
        elif response.startswith("ERR_19"):
            message = "Repeated IR transmission failure."
        elif response.startswith("ERR_20"):
            message = "Above designated IR <on|off> pair limit."
        elif response.startswith("ERR_21"):
            message = "Symbol odd boundary."
        elif response.startswith("ERR_22"):
            message = "Undefined symbol."
        elif response.startswith("ERR_23"):
            message = "Unknown option."
        elif response.startswith("ERR_24"):
            message = "Invalid baud rate setting."
        elif response.startswith("ERR_25"):
            message = "Invalid flow control setting."
        elif response.startswith("ERR_26"):
            message = "Invalid parity setting."
        elif response.startswith("ERR_27"):
            message = "Settings are locked."
        message = response
