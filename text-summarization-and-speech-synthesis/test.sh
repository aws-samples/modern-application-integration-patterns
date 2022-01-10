#!/bin/zsh

STACK=$(sed -nr '/stack_name/{s/stack_name = "(.*)"/\1/;p;}' samconfig.toml)
WS_WAIT=50
MSG=$1

function get_cf_output () {
    ENDPOINT=$(aws cloudformation describe-stacks \
            --stack-name $STACK \
            --query "Stacks[].Outputs[?OutputKey=='$1'].OutputValue" \
            --output text) 
    echo $ENDPOINT
}

REST_ENDPOINT=$(get_cf_output "SolutionRestApiEndpoint")
echo "Connecting to REST API ($REST_ENDPOINT) to start Step Functions Execution..."
#SFN_EXE_ARN=$(http POST $REST_ENDPOINT text=$MSG | jq .workflow.executionArn)
SFN_EXE_ARN=$(curl -X POST -d "{"text": \"$MSG\"}" $REST_ENDPOINT --header "Content-Type:application/json" -s | jq .workflow.executionArn)

WS_ENDPOINT=$(get_cf_output "SolutionWebsocketEndpoint")
WS_MESSAGE='{"action": "OpenConnection", "executionArn":'$SFN_EXE_ARN'}'
echo "Connecting to Websocket API for response (Execution ARN: $SFN_EXE_ARN) ..."
wscat -c $WS_ENDPOINT -w $WS_WAIT -x $WS_MESSAGE
