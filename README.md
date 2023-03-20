# llmapi-server
llmapi-server 是一个封装了多种大语言模型(LLM，如ChatGPT,GPT-3,GPT-4等)的抽象后端，并通过OpenAPI提供简单的访问服务

## 安装和运行(Install & Run)

1. 本地安装运行
```
# python >= 3.8
python3 -m pip install requirements.txt

python3 run_server.py
```

2. 使用docker运行

```
./build_docker.sh
./start_docker.sh
```

## 访问llmapi-server

1. 使用curl命令访问:

``` shell
# 1. 开始一个session
curl -X POST -H "Content-Type: application/json" -d '{"apikey":"xxx","bot_type":"mock","bot_key":"your key"}' http://127.0.0.1:8800/v1/chat/start
# response: {"code":0,"msg":"Success","session":"123456"}

# 2. 和后端进行对话交互
curl -X POST -H "Content-Type: application/json" -d '{"apikey":"xxx","session":"123456","content":"hello"}' http://127.0.0.1:8800/v1/chat/ask
# response: {"code":0,"msg":"Success","reply":"Text mock reply for your prompt:hello","timestamp":1678865301.0842562}

# 3. 关闭session，结束对话
curl -X POST -H "Content-Type: application/json" -d '{"apikey":"xxx"}' http://127.0.0.1:8800/v1/chat/end
# response: {"code":0,"msg":"Success"}
```

2. 使用[llmapi_cli](https://github.com/llmapi-io/llmapi-cli)命令工具访问

``` shell
llmapi_cli --host="http://127.0.0.1:8800" --bot=mock --apikey=123 --bot_key="your key"
```

3. 在你的python代码中使用llmapi_cli库访问
``` python
from llmapi_cli import LLMClient

client = LLMClient(host = "http://127.0.0.1:8800", apikey = "123", bot = "mock", bot_key = "your key")

rep = client.ask("hello")

print(rep)
```

## 接入你的LLM后端

1. 需要在backend目录内新建一个新的后端名称（假设为`newllm`）,可以直接`cp -r mock newllm`
2. 参照`mock`的实现，更改后端名称为`newllm`
3. 在`newllm`目录下，添加必要的依赖，所有相关的开发约束于该目录内
4. 在`backend.py`中添加对`newllm`的支持
