# They are for data manipulation/ 기본 데이터 정리 및 처리
import pandas as pd
import numpy as np

# For Visualization / 시각화
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
plt.style.use('seaborn-whitegrid')
import missingno

# For preprocessing and ML algorithms / 전처리 및 머신 러닝 알고리즘
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import VotingClassifier

# Tunning and Evaluation / 모델 튜닝 및 평가
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_predict
from sklearn import model_selection

# Ignore warnings / 경고 제거 (Pandas often makes warnings)
import sys

import warnings
warnings.filterwarnings('ignore')

# This may be harder than expected for a firsttimer, but if the data was not delivered correctly from the copy, press "+ Add Data", load "Titanic Data" from "Competition Data", and click each file to check the path address.
# 이 것이 처음하는 사람에게 예상보다 어려울 수 있는데 복사한 것에서 데이터가 전달이 잘 안 되었다면 "+Add Data" 누르시고 'Competition Data'에서 "Titanic Data" 불러온 후 파일을 찍어서 경로 주소 확인해야 함
test = pd.read_csv("C:/Users/dkbla/PycharmProjects/projects_pc/test.csv")
train = pd.read_csv("C:/Users/dkbla/PycharmProjects/projects_pc/train.csv")

# Now csv files, test and train, have become data frames.



# 병합 준비
ntrain = train.shape[0]
ntest = test.shape[0]

# 아래는 따로 잘 모셔 둡니다.
y_train = train['Survived'].values
passId = test['PassengerId']

# 병함 파일 만들기
data = pd.concat((train, test))

# 데이터 행과 열의 크기는
print("data size is: {}".format(data.shape))

