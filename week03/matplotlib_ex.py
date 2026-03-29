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

"""### **수직 막대 그래프 : 각 승선 항구에 따른 생존자 수 확인하기**"""

# 승선 항구에 따른 생존자의 수 계산
survived_counts = titanic[titanic['Survived'] == 1]['Embarked'].value_counts()

# 막대 그래프 그리기
plt.bar(survived_counts.index, survived_counts,
        color = ['mediumorchid', 'darkviolet', 'indigo'])
plt.title('Survived Counts by Embarked Port on Titanic')
plt.xlabel('Embarked Port')
plt.ylabel('Count')
plt.xticks(survived_counts.index, ['Southampton', 'Cherbourg', 'Queenstown'])
plt.legend(['Survived'], loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 생존자 수 표시
for i, value in enumerate(survived_counts):
    plt.text(i, value + 1, str(value), ha='center', va='bottom')

plt.savefig('Figure02.png')
plt.close()

"""### **수평 막대 그래프 : 성별에 따른 생존자 수 확인하기**"""

# 성별에 따른 생존자의 수 계산
survived_counts = titanic[titanic['Survived'] == 1]['Sex'].value_counts()

# 수평 막대 그래프 그리기
bars = plt.barh(survived_counts.index, survived_counts, color=['darkturquoise', 'salmon'])
plt.title('Survived Counts by Gender on Titanic')
plt.xlabel('Count')
plt.ylabel('Gender')
plt.legend(bars, ['Survived - Female', 'Survived - Male'], loc='upper right')

# 차이 강조를 위해 수평선 추가
plt.axvline(x=survived_counts['male'], color='gray', linestyle='--', linewidth=1)

# 생존자 수 표시
for i, value in enumerate(survived_counts):
    plt.text(value + 1, i, str(value), ha='left', va='center')

plt.savefig('Figure03.png')
plt.close()
