ver=`cat VERSION`

# 1. check dbs and logs
mkdir -p logs

# 2. run api server
sudo docker run  --network=host --name='llmapi_api_server' -d -v `pwd`/configs:/app/configs -v `pwd`/logs:/app/logs llmapi_api_server:$ver
