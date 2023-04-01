ver=`cat VERSION`
sudo docker build -t llmapi_api_server:$ver -f ./Dockerfile .
