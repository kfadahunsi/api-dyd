import os
from dotenv import load_dotenv


load_dotenv()  # picks up .env.local automatically

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

#these will change each season
entry_ids = {
        "ASA" : 224216,
        "SSFC" : 228809,
        "MMUFC" : 257018,
        "SLS" : 227314,
        "DDGP" : 237637,
        "DTF" : 312224,
    }

#this changes per season
league_id = 43953

#these will change each season
team_ids = {
        "ASA" : 222315,
        "SSFC" : 226964,
        "MMUFC" : 255709,
        "SLS" : 225455,
        "DDGP" : 235896,
        "DTF" : 311434,
}

full_team_ids = {
    "Super Slimey Fütbol": 226964,
    "Amassing Silvaware": 222315,
    "Maatsen Margiela Utd": 255709,
    "Saint Laurent Slot": 225455,
    "Darwin’s Theory": 311434,
    "Duck Duck Guus Poyet": 235896,
}









ifc_team_id = 324714
ifc_league_id = 63351




#the below can be used for accessing the restricted endpoints, maybe useful in future updates 

cookies = {
    '_gcl_au': '1.1.1348086957.1773400481',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Mar+18+2026+15%3A40%3A00+GMT%2B0100+(West+Africa+Time)&version=202502.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=10d87b4a-7e0d-4581-b9fb-f2b5419b358c&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&intType=2&geolocation=NG%3BLA&AwaitingReconsent=false',
    'datadome': 'x6EirH05b4ctnF8fZ4NYu_m25bqD4BvM1owJodCFgq_UqKsf1x_sHDAbHi4~bu5tlMGMVULyHinIom09STbpmzB16YQP734e3VNs8ElXDEwnZv7FWkrzlyjBwDktuljr',
    'OptanonAlertBoxClosed': '2026-03-13T11:14:45.902Z',
    '_fbp': 'fb.1.1773400531569.897802345639227237',
    '_tt_enable_cookie': '1',
    '_ttp': '01KKKEH948DPVRTXR21WYYBNQN_.tt.1',
    'ttcsid_CQTPD5JC77U6D8VT2IE0': '1773842838255::m6Ea-Rb78vYezaLbwXFr.4.1773842853942.1',
    'ttcsid': '1773842838256::fGqwGvqk2IbOAOm2EZB2.4.1773842853941.0',
    'global_sso_id': '786b4074-a7d6-4ba8-ba09-ef1296649a25',
    'activeEntry': '224216',
    'optimizelyEndUserId': 'oeu1773673031113r0.6088700258556428',
    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImRlZmF1bHQifQ.eyJjbGllbnRfaWQiOiIxZjI0M2Q3MC1hMTQwLTQwMzUtOGM0MS0zNDFmNWFmNWFhMTIiLCJpc3MiOiJodHRwczovL2F1dGgucGluZ29uZS5ldS82ODM0MGRlMS1kZmI5LTQxMmUtOTM3Yy0yMDE3Mjk4NmQxMjkvYXMiLCJqdGkiOiI1OWU5ZWQxNC03ZDI3LTQxNzktYWJjOC1lZTk5ZThmNWM0MTciLCJpYXQiOjE3NzM2NzMwMzgsImV4cCI6MTc3MzcwMTgzOCwiYXVkIjpbImh0dHBzOi8vYXBpLnBpbmdvbmUuZXUiXSwic2NvcGUiOiJwMTpyZWFkOmRldmljZSBwMTp1cGRhdGU6dXNlciBvcGVuaWQgcHJvZmlsZSBvZmZsaW5lX2FjY2VzcyBwMTpyZXNldDp1c2VyUGFzc3dvcmQiLCJzdWIiOiI3ODZiNDA3NC1hN2Q2LTRiYTgtYmEwOS1lZjEyOTY2NDlhMjUiLCJzaWQiOiJhMjhiZjhmMy03NWNhLTQ2Y2MtYmFhOS0wNzEyMzY1ODkzODMiLCJhdXRoX3RpbWUiOjE3NzM2NzMwMzcsImFjciI6IjI2MmNlNGIwMWQxOWRkOWQzODVkMjZiZGRiNDI5N2I2IiwiYXV0aGVudGljYXRvciI6InB3ZCBtZmEiLCJodHRwOi8vbWVkaWFraW5kLmNvbS9tZi90aWQiOiJkZWZhdWx0IiwiZW52IjoiNjgzNDBkZTEtZGZiOS00MTJlLTkzN2MtMjAxNzI5ODZkMTI5Iiwib3JnIjoiM2E2ODUwMzItODMyNi00OTY5LWE3OGItY2MyOTc3NWIxM2Q2IiwicDEucmlkIjoiZDU5YmM4NjItMGIzMy00N2Q3LWE1OTQtMTMxYTQ1MmJlOGI4In0.OBJm-Pb-_0je3KkXf7dGNsq_OaSlO-VWvABIJ1Vr41WGMr3VDpk99st1BwuzPbeiSNP8iBWWpGzdiqP-B9hnDAawB6TDoqTE9zKquSm0eYBAgM2LMlL8CWjprct1gdzGRDcHdJmqCwer2vtWJdFK8U2JjVJcMTiQDYZZ8MTA7UXhucdgEsHfrWWEputKb4cRPM6BzpR0roRXRLkzZWrDGH2JJyqj7GRWW0Il_tH-0PD0aa1M-rZoKhJapVbdk7vmupELX8nPX4b3Trh0n-1HkFsajzZropH0_limoYy-iLHT_oT-NTwb2uuaZfyqOikrulCWEojC-m0WQpjvM975mQ',
    'refresh_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImRlZmF1bHQifQ.eyJzdWIiOiI3ODZiNDA3NC1hN2Q2LTRiYTgtYmEwOS1lZjEyOTY2NDlhMjUiLCJqdGkiOiI2NTM4ZDBmYi04YzA4LTQxZWItODRiMi1iYzkwY2YxODViY2IiLCJleHAiOjE3NzYyNjUwMzgsInNpZCI6ImEyOGJmOGYzLTc1Y2EtNDZjYy1iYWE5LTA3MTIzNjU4OTM4MyIsInNjb3BlIjoicDE6cmVhZDpkZXZpY2UgcDE6dXBkYXRlOnVzZXIgb3BlbmlkIHByb2ZpbGUgb2ZmbGluZV9hY2Nlc3MgcDE6cmVzZXQ6dXNlclBhc3N3b3JkIiwiYXV0aF90aW1lIjoxNzczNjczMDM3LCJhY3IiOiIyNjJjZTRiMDFkMTlkZDlkMzg1ZDI2YmRkYjQyOTdiNiIsImFtciI6WyJtZmEiLCJwd2QiXSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnBpbmdvbmUuZXUvNjgzNDBkZTEtZGZiOS00MTJlLTkzN2MtMjAxNzI5ODZkMTI5L2FzIiwiZGF2aW5jaV9hY2Nlc3NfdG9rZW5fYXR0cmlidXRlcyI6IntcImF1dGhlbnRpY2F0b3JcIjpcInB3ZCBtZmFcIixcImh0dHA6Ly9tZWRpYWtpbmQuY29tL21mL3RpZFwiOlwiZGVmYXVsdFwifSJ9.Bczr8QNM2WbtvkCoagkTWGdIQLuwdgbdt7aJx5u5vEvKsYudKDBlztJ8n5ODCDf0yX3hVp5Ah_btNFpdghnixa5WYsGdmocY080rhuIu4ZqBUvPyXCCdzMxMoCxvW8NpYlknQgjh-GQhkMwQdKdMrzVjpJ1zCh1XPv8hU1IrgEd2wQDVQIdInMN0GwVoWwTdBPmYnG2wNJb3X26tQ1kQvovexfcAr7jkAIOofXCb6e4y-UVQiqFNoi1eD6p_FclYORM7brB0_og8hiqaTK86JxUjRKqCxilmV1CCoVKbOQK1dOe0il5TpxFoWKqZl1J6g7RIlPMpsvZ-Xu8lrC7OUw',
    '_cb': 'CIjFQaBsnzPmBxJemT',
    '_chartbeat2': '.1773673077412.1773673102646.1.DjiWJAD01qOXBl2doLrmOdABfR_Y_.4',
    'optimizelySession': '1773673101312',
    '__gads': 'ID=08c063e59cf9c976:T=1773673673:RT=1773673673:S=ALNI_MY_hTDo6NRuap6lJ8zDmPFQ3mJaGA',
    '__gpi': 'UID=0000138178e52b07:T=1773673673:RT=1773673673:S=ALNI_MYNLwk1Hm6UIwdw9Nr4ehNwQ6vMnw',
    '__eoi': 'ID=a16f8e66ef5e75eb:T=1773673673:RT=1773673673:S=AA-AfjbtDJH8-KRXKbU3eJBR87Sv',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://draft.premierleague.com/team/my',
    'X-API-Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImRlZmF1bHQifQ.eyJjbGllbnRfaWQiOiJkZDRkZTAzYy0wZTAxLTRmN2MtOGQzNC03YTQzMjIzZDJmN2IiLCJpc3MiOiJodHRwczovL2FjY291bnQucHJlbWllcmxlYWd1ZS5jb20vYXMiLCJqdGkiOiIxNzQyYTM2Yi04NTRlLTQ5ZTYtOGYwYi05MzM5N2Q5ZDc3MjMiLCJpYXQiOjE3NzM4NDI4MTksImV4cCI6MTc3Mzg3MTYxOSwiYXVkIjpbImh0dHBzOi8vYXBpLnBpbmdvbmUuZXUiXSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInN1YiI6Ijc4NmI0MDc0LWE3ZDYtNGJhOC1iYTA5LWVmMTI5NjY0OWEyNSIsInNpZCI6ImE1OWU0ZmNhLWQyMjUtNDcxMS1hYjA4LTkyZTI3YWY4NWU5ZiIsImF1dGhfdGltZSI6MTc3Mzg0MjgxNywiYWNyIjoiMjYyY2U0YjAxZDE5ZGQ5ZDM4NWQyNmJkZGI0Mjk3YjYiLCJhdXRoZW50aWNhdG9yIjoicHdkIiwiaHR0cDovL21lZGlha2luZC5jb20vbWYvdGlkIjoiZGVmYXVsdCIsImVudiI6IjY4MzQwZGUxLWRmYjktNDEyZS05MzdjLTIwMTcyOTg2ZDEyOSIsIm9yZyI6IjNhNjg1MDMyLTgzMjYtNDk2OS1hNzhiLWNjMjk3NzViMTNkNiIsInAxLnJpZCI6IjEwZTdhMjE3LTAzOWQtNDk0My1iNTQwLWM4YjY3MTQzYTBjZCJ9.XRZNxrvz-669ovHu-jRELTiVW7U4lY8bojdhroPC0y74dgB8ubQrygNdLHlBnFV2XrDY0Enq7RMvys9GvZi3br2MeKqnXpJ4E-cIhWOoamz0vtckXoFPB6tExtqGBOY5xsCwhJdkPUYXiRdpZ4_2Ujm6Kwlew2x9c1-dAvlyhCK1kqYLlPgrZCV02ENLTc-Hf_Xs4sdPjQhq1PVpuWo0IMT7FjrhFkujBSuBn8S9d_5Oey7mRoYjBCMxng7PRZ-JLPHPiXNZAU-pSE_obOPW4-mAnKSsWXN-EQQvVCay4ZEwxv8ZgwLK84P8wPX8Ey-hy690vYIhPMzzCxYKeWa4iA',
    'Connection': 'keep-alive',
    # 'Cookie': '_gcl_au=1.1.1348086957.1773400481; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Mar+18+2026+15%3A40%3A00+GMT%2B0100+(West+Africa+Time)&version=202502.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=10d87b4a-7e0d-4581-b9fb-f2b5419b358c&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&intType=2&geolocation=NG%3BLA&AwaitingReconsent=false; datadome=x6EirH05b4ctnF8fZ4NYu_m25bqD4BvM1owJodCFgq_UqKsf1x_sHDAbHi4~bu5tlMGMVULyHinIom09STbpmzB16YQP734e3VNs8ElXDEwnZv7FWkrzlyjBwDktuljr; OptanonAlertBoxClosed=2026-03-13T11:14:45.902Z; _fbp=fb.1.1773400531569.897802345639227237; _tt_enable_cookie=1; _ttp=01KKKEH948DPVRTXR21WYYBNQN_.tt.1; ttcsid_CQTPD5JC77U6D8VT2IE0=1773842838255::m6Ea-Rb78vYezaLbwXFr.4.1773842853942.1; ttcsid=1773842838256::fGqwGvqk2IbOAOm2EZB2.4.1773842853941.0; global_sso_id=786b4074-a7d6-4ba8-ba09-ef1296649a25; activeEntry=224216; optimizelyEndUserId=oeu1773673031113r0.6088700258556428; access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImRlZmF1bHQifQ.eyJjbGllbnRfaWQiOiIxZjI0M2Q3MC1hMTQwLTQwMzUtOGM0MS0zNDFmNWFmNWFhMTIiLCJpc3MiOiJodHRwczovL2F1dGgucGluZ29uZS5ldS82ODM0MGRlMS1kZmI5LTQxMmUtOTM3Yy0yMDE3Mjk4NmQxMjkvYXMiLCJqdGkiOiI1OWU5ZWQxNC03ZDI3LTQxNzktYWJjOC1lZTk5ZThmNWM0MTciLCJpYXQiOjE3NzM2NzMwMzgsImV4cCI6MTc3MzcwMTgzOCwiYXVkIjpbImh0dHBzOi8vYXBpLnBpbmdvbmUuZXUiXSwic2NvcGUiOiJwMTpyZWFkOmRldmljZSBwMTp1cGRhdGU6dXNlciBvcGVuaWQgcHJvZmlsZSBvZmZsaW5lX2FjY2VzcyBwMTpyZXNldDp1c2VyUGFzc3dvcmQiLCJzdWIiOiI3ODZiNDA3NC1hN2Q2LTRiYTgtYmEwOS1lZjEyOTY2NDlhMjUiLCJzaWQiOiJhMjhiZjhmMy03NWNhLTQ2Y2MtYmFhOS0wNzEyMzY1ODkzODMiLCJhdXRoX3RpbWUiOjE3NzM2NzMwMzcsImFjciI6IjI2MmNlNGIwMWQxOWRkOWQzODVkMjZiZGRiNDI5N2I2IiwiYXV0aGVudGljYXRvciI6InB3ZCBtZmEiLCJodHRwOi8vbWVkaWFraW5kLmNvbS9tZi90aWQiOiJkZWZhdWx0IiwiZW52IjoiNjgzNDBkZTEtZGZiOS00MTJlLTkzN2MtMjAxNzI5ODZkMTI5Iiwib3JnIjoiM2E2ODUwMzItODMyNi00OTY5LWE3OGItY2MyOTc3NWIxM2Q2IiwicDEucmlkIjoiZDU5YmM4NjItMGIzMy00N2Q3LWE1OTQtMTMxYTQ1MmJlOGI4In0.OBJm-Pb-_0je3KkXf7dGNsq_OaSlO-VWvABIJ1Vr41WGMr3VDpk99st1BwuzPbeiSNP8iBWWpGzdiqP-B9hnDAawB6TDoqTE9zKquSm0eYBAgM2LMlL8CWjprct1gdzGRDcHdJmqCwer2vtWJdFK8U2JjVJcMTiQDYZZ8MTA7UXhucdgEsHfrWWEputKb4cRPM6BzpR0roRXRLkzZWrDGH2JJyqj7GRWW0Il_tH-0PD0aa1M-rZoKhJapVbdk7vmupELX8nPX4b3Trh0n-1HkFsajzZropH0_limoYy-iLHT_oT-NTwb2uuaZfyqOikrulCWEojC-m0WQpjvM975mQ; refresh_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImRlZmF1bHQifQ.eyJzdWIiOiI3ODZiNDA3NC1hN2Q2LTRiYTgtYmEwOS1lZjEyOTY2NDlhMjUiLCJqdGkiOiI2NTM4ZDBmYi04YzA4LTQxZWItODRiMi1iYzkwY2YxODViY2IiLCJleHAiOjE3NzYyNjUwMzgsInNpZCI6ImEyOGJmOGYzLTc1Y2EtNDZjYy1iYWE5LTA3MTIzNjU4OTM4MyIsInNjb3BlIjoicDE6cmVhZDpkZXZpY2UgcDE6dXBkYXRlOnVzZXIgb3BlbmlkIHByb2ZpbGUgb2ZmbGluZV9hY2Nlc3MgcDE6cmVzZXQ6dXNlclBhc3N3b3JkIiwiYXV0aF90aW1lIjoxNzczNjczMDM3LCJhY3IiOiIyNjJjZTRiMDFkMTlkZDlkMzg1ZDI2YmRkYjQyOTdiNiIsImFtciI6WyJtZmEiLCJwd2QiXSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnBpbmdvbmUuZXUvNjgzNDBkZTEtZGZiOS00MTJlLTkzN2MtMjAxNzI5ODZkMTI5L2FzIiwiZGF2aW5jaV9hY2Nlc3NfdG9rZW5fYXR0cmlidXRlcyI6IntcImF1dGhlbnRpY2F0b3JcIjpcInB3ZCBtZmFcIixcImh0dHA6Ly9tZWRpYWtpbmQuY29tL21mL3RpZFwiOlwiZGVmYXVsdFwifSJ9.Bczr8QNM2WbtvkCoagkTWGdIQLuwdgbdt7aJx5u5vEvKsYudKDBlztJ8n5ODCDf0yX3hVp5Ah_btNFpdghnixa5WYsGdmocY080rhuIu4ZqBUvPyXCCdzMxMoCxvW8NpYlknQgjh-GQhkMwQdKdMrzVjpJ1zCh1XPv8hU1IrgEd2wQDVQIdInMN0GwVoWwTdBPmYnG2wNJb3X26tQ1kQvovexfcAr7jkAIOofXCb6e4y-UVQiqFNoi1eD6p_FclYORM7brB0_og8hiqaTK86JxUjRKqCxilmV1CCoVKbOQK1dOe0il5TpxFoWKqZl1J6g7RIlPMpsvZ-Xu8lrC7OUw; _cb=CIjFQaBsnzPmBxJemT; _chartbeat2=.1773673077412.1773673102646.1.DjiWJAD01qOXBl2doLrmOdABfR_Y_.4; optimizelySession=1773673101312; __gads=ID=08c063e59cf9c976:T=1773673673:RT=1773673673:S=ALNI_MY_hTDo6NRuap6lJ8zDmPFQ3mJaGA; __gpi=UID=0000138178e52b07:T=1773673673:RT=1773673673:S=ALNI_MYNLwk1Hm6UIwdw9Nr4ehNwQ6vMnw; __eoi=ID=a16f8e66ef5e75eb:T=1773673673:RT=1773673673:S=AA-AfjbtDJH8-KRXKbU3eJBR87Sv',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=4',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


"""
Log in to the fpl website in browser
Open the inspection console 
Click on the network tab, you will see a similar table to the one below:
Navigate to any page on the fpl site eg “pick team” which should trigger the table to be populated
Right click on one of the rows which is an api call, eg the highlighted one in the picture above.
Click on copy value > copy as cURL (POSIX)
Paste the copied info to this site https://curlconverter.com/
This will generate the headers and cookies you need to put into any request that requires them
"""