# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

# [중요] 여기에 공공데이터포털에서 발급받은 서비스키를 넣어야 합니다.
ServiceKey = "자신의 Service Key"

def main():
    jsonResult = []
    result = []

    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    nat_cd = input('국가 코드를 입력하세요(중국: 112 / 일본: 130 / 미국: 275) :')
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? : '))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))
    ed_cd = "E"  # E : 방한외래관광객, D : 해외 출국

    jsonResult, result, natName, dataEND = getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)

    # 파일 저장 : csv 파일
    columns = ["입국자국가", "국가코드", "입국연월", "입국자 수"]
    result_df = pd.DataFrame(result, columns = columns)
    # 한글 깨짐 방지를 위해 cp949 인코딩 사용
    result_df.to_csv('./%s_%s_%d_%s.csv' % (natName, ed_cd, nStartYear, dataEND), index = False, encoding = 'cp949')
