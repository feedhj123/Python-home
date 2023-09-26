# 0926 project
def myfunction(msg):
    """_summary_

    Args:
        msg (_type_): _description_

    Returns:
        _type_: _description_
    """
    #a = 0
    #b = 10
    msg_local = msg
    def myfunction_inner():
        return msg_local
    return myfunction_inner
MSG = "Hello World"
aaa = myfunction(MSG)
print(aaa())
