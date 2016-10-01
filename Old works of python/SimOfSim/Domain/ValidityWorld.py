

class ObjectException(Exception):

    def __init__(self,msg):

        self.__msg=msg

    def __str__(self):

        return self.__msg

class Validator:

    def validate(self,obj):

        msg=""

        if not obj.get_name().isalpha() : msg+="There is no name or incorect typing of the name!!!"
        if not obj.get_pType().isalpha() : msg+="There is no type or incorect typing of the type!!!"
        if not obj.get_q().isdigit() : msg+="There is no number or number typed incorectly!!!"

        if len(msg) > 0 :
            raise ObjectException(msg)