import hashlib
import time
import secrets
import logging
import random

def get_hash(content:str)->str:
    h = hashlib.sha256()
    h.update(content.encode('utf-8'))
    return str(h.hexdigest())

def get_short_hash(content:str)->str:
    return get_hash(content)[:8]

def get_rand_hex()->str:
    return secrets.token_hex(16)

def get_rand_code(num_digits:int = 6)->str:
    code = ''
    for i in range(num_digits):
        code += str(random.randint(0, 9))
    return code

def get_logger(name,filename,level = logging.WARNING):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    # 定义日志格式
    logging.Formatter.converter = time.localtime
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

def _test():
    # get_hash
    s = time.perf_counter()
    for i in range(1000):
        res = get_hash("abc123asdafs")
    print(f"run get_hash 1000 times,cost:{time.perf_counter()-s} s")


    import os
    log = get_logger("test","test.log",logging.INFO)
    log.info("info test")
    log.warning("warn test")
    log.error("error test")
    os.remove('test.log')

if __name__ == "__main__":
    try:
        _test()
    except AssertionError:
        print(' \033[1;32;41m !! test failed !! \033[0m')
    else:
        print(' \033[1;32;44m test PASS :) \033[0m')
