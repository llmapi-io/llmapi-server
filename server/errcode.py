from enum import Enum

class StatusCode(Enum):
    OK = (0, 'Success')
    ERROR = (-1, 'Internal error')
    FAILED = (-2, 'Failed')
    PARAM_ERR = (-3, 'Request params not valid')
    SESSION_INVALID = (-4, 'Session invalid')
    BOT_TYPE_INVALID = (-5, 'Bot type invalid')
    REPLY_TIMEOUT = (-6, 'Reply timeout')

    @property
    def code(self):
        return self.value[0]
    @property
    def msg(self):
        return self.value[1]


def _test():
    repeat = False
    for v in StatusCode:
        for vv in StatusCode:
            if v != vv and (v.code == vv.code or v.msg == vv.msg):
                print('Value duplication:',v,v.value,' and ',vv,vv.value)
                repeat = True
                assert(repeat == False)

if __name__ == '__main__':
    try:
        _test()
    except AssertionError:
        print(' \033[1;32;41m !! test failed !! \033[0m')
    else:
        print(' \033[1;32;44m test PASS :) \033[0m')
