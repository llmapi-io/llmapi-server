LOG_FILE_ROOT='logs'

SupportBotTyps = ['mock','gpt3','chatgpt','welm', "newbing", "gpt-embedding"]

# read from config json
GPT3_KEYS = ['']
CHATGPT_KEYS = ['']
WELM_KEYS = ['']
NEWBING_KEYS = ['']
GPT_EMBEDDING_KEYS = ['']

def config_init():
    import json
    global GPT3_KEYS
    global CHATGPT_KEYS
    global WELM_KEYS
    global NEWBING_KEYS
    global GPT_EMBEDDING_KEYS

    with open('configs/keys.json') as f:
        js = json.load(f)
        GPT3_KEYS = js['gpt3']
        CHATGPT_KEYS = js['chatgpt']
        WELM_KEYS = js['welm']
        NEWBING_KEYS = js['newbing']
        GPT_EMBEDDING_KEYS = js['gpt-embedding']
