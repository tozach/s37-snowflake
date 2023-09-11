# import functions_framework
import json
import requests

# @functions_framework.http
def detokenize():
    url = "https://ebfc9bee4242.vault.skyflowapis.com/v1/vaults/tbafa641903740b3aaeda426b8ed5d8a/detokenize"
    #print("Going to call signedJWT ...")
    #signedJWT, creds = getSignedJWT()
    #print("Called signedJWT ...")
    detokenizationParameters = []
    
    #request_json = request.get_json(silent=True)
    request_json = {'requestId': 'fb033523-4d2d-4c61-a2cb-b52f13468d08', 'caller': '//bigquery.googleapis.com/projects/genial-shuttle-365622/jobs/bquxjob_9ac1abf_189b918a90a', 'sessionUser': 'toms.zacharia@gmail.com', 'calls': [['egoroqxfxztjagetbnaa@cqacfvcjtq.com', 'PLAIN_TEXT'], ['nuacujpxenqqnljizxzg@fqisimxfch.com', 'PLAIN_TEXT'], ['vdptkodgdlcvjlhmpxsc@xjfrlsnzfe.com', 'PLAIN_TEXT'], ['vmdyxweuiqwvjhxrqard@lbaligjzwr.com', 'PLAIN_TEXT'], ['ukobrddvrbrpqcmcyryv@cnlrhpbhea.com', 'PLAIN_TEXT'], ['speddluurtrtpvhroqqi@yecfeakrpa.com', 'PLAIN_TEXT'], ['mbfnwbilcxanbhbktlbo@oxubsecqia.com', 'PLAIN_TEXT'], ['fuonsxwtbsyvtyxhimji@xjoqlyxntq.com', 'PLAIN_TEXT'], ['fkpglolowiwlnixroebw@zasdhszyjv.com', 'PLAIN_TEXT'], ['nynjahhyvdvpjmrsexht@tkfwemrdby.com', 'PLAIN_TEXT'], ['rvtpldvhfisdhfouixht@nmtjrzvmod.com', 'PLAIN_TEXT'], ['bjzzpfwxhnzmdwjgtyfc@qpuoluugjs.com', 'PLAIN_TEXT'], ['easrzttwrnbkzvpxnfth@lmliqaujdo.com', 'PLAIN_TEXT'], ['yjycccjotybsmscpriwh@zigfmoqibs.com', 'PLAIN_TEXT'], ['fhpwktuguwkspfuovxcn@ifwdjkgyvf.com', 'PLAIN_TEXT'], ['xytvzjsgeephygpyaqfd@myszcmccge.com', 'PLAIN_TEXT'], ['zywrbrmdttrswpkvpyfq@uhllzysibb.com', 'PLAIN_TEXT'], ['jsgqqwwvxdqbipsemsca@usrzqnyyte.com', 'PLAIN_TEXT'], ['toixbrvmjizcsazabojq@vsdbbrajql.com', 'PLAIN_TEXT'], ['ecmukfcldotwejctshvi@wqkreknabl.com', 'PLAIN_TEXT'], ['uuuxfvkqxfewcsldppuv@kakymzieub.com', 'PLAIN_TEXT'], ['kogkzooptkvjwzvmudde@pdyrhxtchj.com', 'PLAIN_TEXT'], ['alxvzlhqashfebkhgjni@vzuwulgjzp.com', 'PLAIN_TEXT'], ['omnnprxozcmkpdaacmrd@fsgrtnnsqq.com', 'PLAIN_TEXT'], ['hrajqarxpwgicelaxoky@sriqibtvxp.com', 'PLAIN_TEXT']]}
    
    token_list = []
    for items in request_json['calls']:
        #print(items)
        token_obj = {'token': items[0], 'redaction': items[1]}
        token_list.append(token_obj)
    
    print(token_list)

    #token = request_json['calls'][0][0]

    payload = json.dumps({"detokenizationParameters": token_list})

    #print(payload)

    headers = {
    'Content-Type': 'application/json',
    'X-SKYFLOW-ACCOUNT-ID': 'cd552c6d6f3047c1bfbfbe3148300365',
    #'Authorization': "Bearer "+ json.loads(getBearerToken(signedJWT, creds))['accessToken']
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2MiOiJjZDU1MmM2ZDZmMzA0N2MxYmZiZmJlMzE0ODMwMDM2NSIsImF1ZCI6Imh0dHBzOi8vbWFuYWdlLnNreWZsb3dhcGlzLmNvbSIsImV4cCI6MTY5MzU3MzQ2NSwiaWF0IjoxNjkwOTgxNDY1LCJpc3MiOiJzYS1hdXRoQG1hbmFnZS5za3lmbG93YXBpcy5jb20iLCJqdGkiOiJtZjY2NTU4ZTU2ZmU0NDYwOWI0YTMzY2FmNjg4MTcxYyIsInN1YiI6Im9mNDg1OTE1M2ZkZDRjNjc5MzYxZTAxNTAzOTAyMzQ0In0.I7bZ-o2Axyl7IMKdOhv9cL2RNa9vQndzGANCXHgd07oFOjU3hiDx0JFoER6kYeKzbgUl7Rhe_UJaovJ11TF06rGxY6qQBHaVHzf3FThrnkDJrjY--fDKksGL0aQs28a-51nnEFcMMNlbxirvK_a90dOmC8WHYFiXl_14Ig6GhOIShWISJCO2SEni1gqO1-6p4p2wNNdkxw1hNc5QNb4bKYnkbApNf6JJX1bKi6lEL3tNFKyHSHHW8Hu3GlPb1YtpHjGMZWdygTru1-tK5l25r6yZWZTyEWa_cLAQcHBYYRKkwuEWhMDtAKPZhc2vzS5WVx1KNZ4i4QGsz9k7ZER59g"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    value = json.loads(response.text)
    detoken_list = []
    for detoken in value['records']:
        detoken_list.append(detoken['value'])
    reply = {'replies': detoken_list}
    print(json.dumps(reply))
    #print(json.dumps({"replies": value}))
    #return (json.dumps({"replies": [value]}))

detokenize()