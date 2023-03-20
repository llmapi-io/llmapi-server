from prepost.filter.filter import Filter

filter = Filter()

class Direct():
    def __init__(self, bottype = 'mock'):
        self.bottype = bottype

    @filter.before
    def _preprocess(self, prompt, **kwargs):
        # TODO app relatived process for prompt
        return prompt

    @filter.after
    def _postprocess(self, answer, **kwargs):
        # TODO app relatived process for answer
        return answer

    def pre(self, func):
        def wrap(prompt, **kwargs):
            text = self._preprocess(prompt,**kwargs)
            if type(text) is not str:
                return text
            res = func(text, **kwargs)
            return res
        return wrap

    def post(self, func):
        def wrap(**kwargs):
            res = func(**kwargs)
            res = self._postprocess(res,**kwargs)
            return res
        return wrap
