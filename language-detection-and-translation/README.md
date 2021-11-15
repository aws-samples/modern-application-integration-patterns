curl -i --location --request POST 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows' --header 'Content-Type: application/json' --data-raw '{"SourceText": "Das ist ein Test."}'


curl -i --location --request GET 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows/arn:aws:states:eu-central-1:689573718314:execution:LanguageDetectionAndTranslationStateMachine-BOQTYVwnDlXz:72267fcd-34db-46f5-b2bc-784221b14e92'
curl --request GET 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows/arn:aws:states:eu-central-1:689573718314:execution:LanguageDetectionAndTranslationStateMachine-BOQTYVwnDlXz:72267fcd-34db-46f5-b2bc-784221b14e92' | jq '.'
curl --request DELETE 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows/arn:aws:states:eu-central-1:689573718314:execution:LanguageDetectionAndTranslationStateMachine-BOQTYVwnDlXz:72267fcd-34db-46f5-b2bc-784221b14e92' | jq '.'

curl --request GET 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows' | jq '.'

https://stedolan.github.io/jq/tutorial/
