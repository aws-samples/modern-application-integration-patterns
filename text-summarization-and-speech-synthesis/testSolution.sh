#!/bin/bash

STACK=$(sed -nr '/stack_name/{s/stack_name = "(.*)"/\1/;p;}' samconfig.toml)
WS_WAIT=60
MSG=$1

function get_cf_output () {
    ENDPOINT=$(aws cloudformation describe-stacks \
            --stack-name $STACK \
            --query "Stacks[].Outputs[?OutputKey=='$1'].OutputValue" \
            --output text) 
    echo $ENDPOINT
}

REST_ENDPOINT=$(get_cf_output "SolutionRestApiEndpoint")/workflows
echo $REST_ENDPOINT
echo "Connecting to REST API ($REST_ENDPOINT) to start Step Functions Execution..."
REST_MSG=$(jq -r -n --arg v "$MSG" '{"text": $v}')
SFN_EXE_ARN=$(curl -X POST -d "$REST_MSG" $REST_ENDPOINT --header "Content-Type:application/json" -s | jq -r .workflow.executionArn)

WS_ENDPOINT=$(get_cf_output "SolutionWebsocketEndpoint")
WS_MESSAGE=$(jq -n --arg v $SFN_EXE_ARN '{"action": "OpenConnection", "executionArn": $v}')
echo "Connecting to Websocket API for response (Execution ARN: $SFN_EXE_ARN) ..."
wscat -c $WS_ENDPOINT -w $WS_WAIT -x "$WS_MESSAGE"
