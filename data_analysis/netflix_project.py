# -*- coding: utf-8 -*-
# 넷플릭스 데이터 분석 프로젝트

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 세션 저장소에 업로드한 csv 파일을 읽어 변수에 할당
netflix = pd.read_csv('netflix_titles.csv')
netflix.head()

# .columns : 열 이름 확인
list(netflix.columns)
