


class TaskException(Exception):


    def __init__(self,msg):

        self.__msg=msg

    def __str__(self):

        return self.__msg


class Validator:

    @staticmethod
    def validate(option):

        errors=""

        valid=["exit","prev","next","filter","undo","redo","add","status","text","delete","report"]

        validFilter=["active","done","archived"]

        optimalString=option.split("<")

        if not optimalString[0] in valid :
            errors+="Not valid command!!!"
        else:
            if optimalString[0].strip() == "filter" or optimalString[0] == "status":
                optimalString=optimalString[1].strip("> ")
                if not optimalString in validFilter:
                    errors+="Not valid filter status"

        if len(errors) > 0 :
            raise TaskException(errors)





