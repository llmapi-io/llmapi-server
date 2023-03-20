import asyncio
import time
import sys
import threading

from utils.utils import get_rand_hex
from utils.kv import KV

import concurrent.futures
import threading

thpool = concurrent.futures.ThreadPoolExecutor(max_workers = 10)
class Bot:
    def __init__(self, **kwargs):
        self.status = "open"
        self.kv = KV()
        
    def open(self, **kwargs):
        if self.status != "close":
            return
        __init__(**kwargs)

    def stub_in(self, val,st = None):
        if self.kv.size() > 10:
            return None

        stub = st
        if st is None:
            stub = get_rand_hex()
        self.kv.set(stub, val)
        return stub

    def stub_out(self, stub):
        if not self.kv.has(stub):
            return None
        return self.kv.get(stub)

    def stub_del(self, stub):
        if self.kv.has(stub):
            self.kv.remove(stub)

    def input(self, prompt, **kwargs):
        stub = self.stub_in(None)
        if stub is None:
            return None
        self._run(stub=stub,prompt=prompt, **kwargs)
        return stub

    def output(self, stub, **kwargs):
        res = self.stub_out(stub)
        if res is not None:
            self.stub_del(stub)
        return res

    def reset(self, **kwargs):
        return None

    def reset(self, **kwargs):
        pass

    def close(self, **kwargs):
        self.status = "close"
        pass

    def task_impl(self, prompt:str, history:dict = None, **kwargs) -> str:
        '''
        interaction implementation for llms
        '''
        pass

    def _worker(self, **kwargs):
        if 'prompt' in kwargs:
            prompt = kwargs['prompt']
        if 'stub' in kwargs:
            stub = kwargs['stub']
        if 'history' in kwargs:
            res = self.task_impl(prompt = prompt, history = kwargs['history'])
        else:
            res = self.task_impl(prompt = prompt, history = None)

        self.stub_in(res,stub)

    def _run(self,**kwargs):
        # t = threading.Thread(target=self._worker, kwargs = kwargs)
        # t.start()
        thpool.submit(self._worker, **kwargs)
