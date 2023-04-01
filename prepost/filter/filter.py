import json
class Filter():

    def __init__(self):
        with open('configs/sensitive.json') as f:
            jstr = f.read()
            js = json.loads(jstr)
       
        self.sesi_dict = []
        for key in js:
            self.sesi_dict += js[key]

    def _filter_before(self, text, **kwargs):
        for sesi in self.sesi_dict:
            if sesi in text:
                return {"sensitive":"输入中包含敏感内容"}
        return text

    def _filter_after(self, text, **kwargs):
        # TODO sensitive filter for answer
        return text

    def before(self, func):
        def wrap(obj, text, **kwargs):
            text = self._filter_before(text,**kwargs)
            if type(text) is not str:
                return text
            res = func(obj, text, **kwargs)
            return res
        return wrap

    def after(self, func):
        def wrap(obj, text, **kwargs):
            res = func(obj, text, **kwargs)
            res = self._filter_after(res,**kwargs)
            return res
        return wrap

