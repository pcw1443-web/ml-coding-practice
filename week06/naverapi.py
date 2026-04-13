# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

# [중요] 네이버 개발자 센터에서 발급받은 ID와 Secret을 입력해야 합니다.
client_id = 'Client ID'
client_secret = 'Client Secret'

def main():
    node = 'news'  # 크롤링할 대상 (news, blog, shop 등)
    srcText = input('검색어를 입력하세요: ')

    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    total = jsonResponse['total']

    # 검색 결과가 있을 때까지 반복 (최대 1000개까지 가능)
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        start = jsonResponse['start'] + jsonResponse['display']
        if start > 1000: break # 네이버 검색 API는 최대 1000개까지 조회 가능
        jsonResponse = getNaverSearch(node, srcText, start, 100)

    print('전체 검색 : %d 건' % total)

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding = 'utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)
        outfile.write(jsonFile)

    print("가져온 데이터 : %d 건" % (cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))
