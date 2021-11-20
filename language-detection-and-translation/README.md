curl -i --location --request POST 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows' --header 'Content-Type: application/json' --data-raw '{"SourceText": "Das ist ein Test."}'


curl -i --location --request GET 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows/arn:aws:states:eu-central-1:689573718314:execution:LanguageDetectionAndTranslationStateMachine-BOQTYVwnDlXz:72267fcd-34db-46f5-b2bc-784221b14e92'
curl --request GET 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows/arn:aws:states:eu-central-1:689573718314:execution:LanguageDetectionAndTranslationStateMachine-BOQTYVwnDlXz:72267fcd-34db-46f5-b2bc-784221b14e92' | jq '.'
curl --request DELETE 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows/arn:aws:states:eu-central-1:689573718314:execution:LanguageDetectionAndTranslationStateMachine-BOQTYVwnDlXz:72267fcd-34db-46f5-b2bc-784221b14e92' | jq '.'

curl --request GET 'https://y4cia8vny6.execute-api.eu-central-1.amazonaws.com/live/workflows' | jq '.'

https://stedolan.github.io/jq/tutorial/
curl -XGET https://r3385gr5je.execute-api.eu-central-1.amazonaws.com/live/respond/reject/AAAAKgAAAAIAAAAAAAAAAaGAtQnYt6Qia9Yx/zIvX/HF0ZO/YDP3naQ2pxe+ZxjOvMc+v3SkDxp4erqT6f3NsqFcVHb1n55ECsyPPbMkbh9zPtr3mPD3KHYPrcleDDhKCyT3bRcmdbftQyVy/W+TRkpNl3u0DDbcxAs9HlNDiLE9uHj4r6YJOE5Y7J4lq4/XRvxSmlPVI/fTmplotS1/spnhR0KfjwVnqJbbdKLnJZ5iw3m3lFMHxvw87JXzUZ2kIBrf0XsKyBBZC3lmkcYPbKAolO0RcZKXPdBDulktbWhW55FfvF+coT9s4dnp588xTylg4ZKL4aKfDkINDLZRkcElFneUcPPMtXTSHrEmwDQC0xo1Oel7XHCDUP7P3hIpxIhg8nnGANQixNARnraH7+NyEj3UyjKRoLXabT3Cq8EuzaSLwvPJtQ571vKu14idVw1Pq3AjjrL1eaFvT0v5GOlh9Tqjs7kIt3IbTsbB3wlp+yZLFMI0ZmqK5D+Ao9Bnod9K1DU3gc8b4tuosgXwwD3Di7QSDprwN9KleyQawQ0j7vDwZmnC0v3+eQ+mHSQaktImk0BXEOBpRhz9UFFe9cCcaddxYDc84ozdh2X3pmuim7Mce1ZUauyHjDzGnFstxfrtW45cHvJPzdfub5fhTOpHQSiN2ADZMQpvwz/TQmi5aHFXsM1Lpcsy9AFbSReqJQM3dPpAfR262CQg7kZqDg== | jq

curl -XGET https://r3385gr5je.execute-api.eu-central-1.amazonaws.com/live/respond/reject/A | jq

curl -i -XGET https://r3385gr5je.execute-api.eu-central-1.amazonaws.com/live/respond/confirm/AAAAKgAAAAIAAAAAAAAAAZI8IC+8h8L/EFHvLVHDb9JkXb4kO7zJyWpjQbkDdqe6SsdsrXclmMOAbmKZi/MOGsI3s6XHVAoTkoDbP6lWTSfcyBFtPC22xgU81mc5sY21nQT2npH6UevUG1DKvFElnJ+08OFzbO3xcBULy+GVOkoVuMJASNzXdmREXWNuepeJb9j7fELG+s93DhWQGT6OP7chutdMGi0yDXVO2gMk618C8PynFsIZyphqQOT4IxReP/dqnqE0irYKUnv84aqAkqLWaMz5URNBhrApJPlaLNOx2Yk7F7TU00wSy/eqOpSRr3SNxxEwIGFtgEkHdDG6aAgC+flgzNUcu+SLjNB+Fppzp1mjcvRo9IRkdqk3v7FTGckrj7Fc06LEWzZjSD6vkhM9YChxPEQfWRYxeb4nad0WLboIJ9YeirYhWTg/G5oRLT1feTclRoitmL2GLirVw0nQ5iAj2rWVNj0VSReW7jSR7Rn9GDhi6qOHo5AFNTmW7pODTbmvbKJ5IiBFUGi2IpAdIbDsZWPxM31l+nsud7DnjVJXUAEXFilf3NFgbygV1rmWjQ2rO+nZ2B/OPyRQ8G2CwibCVShyv6+kNjrdYSQ1XCjyf8mOLLkA0gVeep3o7IKzdRcRkeliDVXx63simhYfRHlJZwyAEdM2dikCHr+OHH/TvhNHJazQleAhVxwi9hFozd+iTuyebdkHMoVNpQ==
