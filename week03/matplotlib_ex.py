# -*- coding: utf-8 -*-
# 타이타닉 데이터셋 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# 타이타닉 CSV 파일 불러오기
# (참고: 실행 환경에 '3.1.1.titanic.csv' 파일이 있어야 합니다.)
titanic = pd.read_csv('3.1.1.titanic.csv')