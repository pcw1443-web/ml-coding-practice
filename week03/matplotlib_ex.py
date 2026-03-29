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

"""### **산점도 그래프 : 나이와 요금, 생존 여부 확인하기**"""

# 결측치 처리
titanic_scatter = titanic.dropna(subset=['Age', 'Fare', 'Survived'])

# 산점도 그래프 그리기
plt.figure(figsize=(12, 8))
scatter = plt.scatter(x='Age', y='Fare', data=titanic_scatter, c=titanic_scatter['Survived'], cmap='Set2', alpha=0.7)

plt.title('Age and Fare Relationship with Survival on the Titanic')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend(handles=scatter.legend_elements()[0], title='Survived',
           labels=['Not Survived', 'Survived'], loc='upper right')
plt.savefig('Figure04.png')
plt.close()

"""### **파이 차트 : 생존자, 사망자 비율 표현하기**"""

# 사망자와 생존자의 수 계산
survived_total_counts = titanic['Survived'].value_counts()

# 파이 차트 그리기
plt.figure(figsize=(8, 8))
plt.pie(survived_total_counts, labels=['Not Survived', 'Survived'], colors=['orange', 'gold'],
        autopct='%0.1f%%', startangle=90, shadow=True, explode=(0, 0.1))

plt.title('Survival Distribution on the Titanic')
plt.savefig('Figure05.png')
plt.close()

"""### **히스토그램 : 승객의 나이 분포 표시하기**"""

# 나이 결측치 제거
titanic_age = titanic.dropna(subset=['Age'])

# 히스토그램 그리기
plt.figure(figsize=(10, 6))
plt.hist(titanic_age['Age'], bins=20, color='seagreen', edgecolor='black')

plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages on the Titanic')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Figure06.png')
plt.close()

"""### **히트맵 : 두 변수의 상관 관계를 표시하기**"""

# 상관 행렬 계산 (수치형 데이터만)
correlation_matrix = titanic.drop('PassengerId', axis=1).corr(numeric_only=True)

# 히트맵 그리기
plt.matshow(correlation_matrix, cmap='PuRd_r')
plt.colorbar()

# x축과 y축의 눈금 설정
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

plt.title('Correlation Heatmap of Titanic', pad=20)
plt.savefig('Figure07.png')
plt.close()

"""### **영역 채우기 그래프 : 나이대별 생존자와 사망자 수 표현하기**"""

# 나이대별 범주화
age_groups = pd.cut(titanic_age['Age'], bins=range(0, 81, 5))
survived_by_age = titanic_age.groupby([age_groups, 'Survived'], observed=False).size().unstack().fillna(0)

# 영역 채우기 그래프 그리기
plt.figure(figsize=(10, 6))
plt.fill_between(survived_by_age.index.astype(str), survived_by_age[1],
                 color='purple', alpha=0.9, label='Survived')
plt.fill_between(survived_by_age.index.astype(str), survived_by_age[0],
                 color='hotpink', alpha=0.6, label='Not Survived')

plt.title('Survival by Age Group on Titanic')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.savefig('Figure08.png')
plt.close()

"""### **박스 플롯 : 승객 나이의 데이터 분포 살펴보기**"""

# 승객 등급에 따른 나이의 박스 플롯
plt.figure(figsize=(8, 6))
plt.boxplot([titanic_age[titanic_age['Pclass'] == 1]['Age'],
             titanic_age[titanic_age['Pclass'] == 2]['Age'],
             titanic_age[titanic_age['Pclass'] == 3]['Age']],
            labels=['1st Class', '2nd Class', '3rd Class'])

plt.title('Box Plot for Age by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Age')
plt.savefig('Figure09.png')
plt.close()

"""### **바이올린 플롯 : 승객 등급에 따른 나이 분포 표시하기**"""

plt.figure(figsize=(10, 6))
violin_plot = plt.violinplot([titanic_age[titanic_age['Pclass'] == 1]['Age'],
                              titanic_age[titanic_age['Pclass'] == 2]['Age'],
                              titanic_age[titanic_age['Pclass'] == 3]['Age']],
                             showmeans=False, showmedians=True)

plt.title('Violin Plot of Age by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Age')
plt.xticks([1, 2, 3], ['1st Class', '2nd Class', '3rd Class'])
plt.legend(violin_plot['bodies'], ['1st Class', '2nd Class', '3rd Class'], title='Pclass')
plt.savefig('Figure10.png')
plt.close()

"""### **에러 바 : 요금의 평균과 표준편차 표현하기**"""

fare_means = titanic.groupby('Parch')['Fare'].mean()
fare_std = titanic.groupby('Parch')['Fare'].std().fillna(0) # 혼자 탄 경우 등 NaN 방지

plt.figure(figsize=(10, 6))
plt.errorbar(fare_means.index, fare_means, yerr=fare_std, fmt='o',
             capsize=5, capthick=1, label='Fare')

plt.title('Error Bar Plot of Fare by Parch')
plt.xlabel('Parch')
plt.ylabel('Fare')
plt.xticks(fare_means.index)
plt.legend()
plt.savefig('Figure11.png')
plt.close()

"""### **서브플롯 활용 예시**"""

# 1. subplot 하나씩 추가하기 (Figure 13 연계)
parch_counts = titanic.groupby('Parch')['Survived'].value_counts().unstack().fillna(0)
x_parch = parch_counts.index.astype(str)
y_dead = parch_counts[0].values
y_survived = parch_counts[1].values

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(x_parch, y_dead, '-o', color='indigo', label='Not Survived')
plt.ylabel('Not Survived Count')
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(x_parch, y_survived, color='deeppink', alpha=0.7, label='Survived')
plt.ylabel('Survived Count')
plt.legend()

plt.suptitle('Survival Analysis by Parch (Subplot Method 1)')
plt.tight_layout()
plt.savefig('Figure13.png')
plt.close()

# 2. subplots()로 동시에 생성 및 축 공유 (Figure 16 연계)
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(x_parch, y_dead, '-s', color='indigo', linewidth=3, label='Not Survived')
ax1.set_xlabel('Parch')
ax1.set_ylabel('Not Survived Count', color='indigo')

ax2 = ax1.twinx() # x축 공유
ax2.bar(x_parch, y_survived, color='deeppink', alpha=0.3, label='Survived')
ax2.set_ylabel('Survived Count', color='deeppink')

plt.title('Survival Analysis by Parch (Dual Axis)')
plt.savefig('Figure16.png')
plt.close()