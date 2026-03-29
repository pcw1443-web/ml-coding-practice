# -*- coding: utf-8 -*-
# 타이타닉 데이터셋 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# 타이타닉 CSV 파일 불러오기
# (참고: 실행 환경에 '3.1.1.titanic.csv' 파일이 있어야 합니다.)
titanic = pd.read_csv('3.1.1.titanic.csv')

# 데이터 처음 5개의 행 출력
print(titanic.head())

# 열에 대한 요약 정보 확인
print(titanic.info())

"""### **선 그래프 : 객실 등급에 따른 생존율 표시하기**"""

# 객실 등급에 따른 생존자와 사망자의 평균 계산 
pclass_survived_mean = titanic.groupby('Pclass')['Survived'].mean().reset_index()

# 선 그래프 그리기 
plt.plot(pclass_survived_mean['Pclass'], pclass_survived_mean['Survived'],
         marker='o', linestyle='-', color='violet')
plt.title('Survival Rate Variation Across Passenger Classes')
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')
plt.xticks([1, 2, 3])
plt.grid(True)
plt.savefig('Figure01.png')         # 결과를 그림파일로 저장
plt.close()                         # 다음 Plot을 새로 그리기 위해 plt 닫기


