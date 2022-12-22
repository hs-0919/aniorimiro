# -*- coding: utf-8 -*-

import pandas as pd

import warnings
warnings.filterwarnings(action='ignore')# 경고출력안하기
import scipy.stats as stats
# from sklearn.preprocessing import LabelEncoder   
import statsmodels.formula.api as smf
  
# # Colab 한글 깨짐 현상 방지
# !sudo apt-get install -y fonts-nanum 
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

pd.options.display.float_format = '{:.5f}'.format
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

from django.shortcuts import render
from django.http import JsonResponse

#데이터 탐색용
df=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiro_data/master/yongsan_192021.csv", encoding='utf-8')

def map(request):

  return render(request, 'analysis/map.html')



def calldbFunc(request):
    
    if request.method=="POST":
        print('view옴')
        tradingArea=request.POST.get('tradingArea')
        BigTradingArea=request.POST.get('BigTradingArea')
        businessType=request.POST.get('businessType')
        smallBusiType=request.POST.get('smallBusiType')

        
        print(BigTradingArea)
        print(tradingArea)
        print(smallBusiType)
        
        
        # 요청을 받으면 해당 상권에 맞는 코드 실행하기
        # 발달상권 예측모델 실행
        if BigTradingArea == '발달상권':
            
            #발달상권
            bal=pd.read_csv("https://raw.githubusercontent.com/JustinChoiHokyeong/aniorimiro/master/aniorimiro/static/data/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EB%B0%9C%EB%8B%AC%EC%83%81%EA%B6%8C_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
            print('발달상권 매출 예상')
            sang_bal = bal[bal['상권_코드_명']==tradingArea]
            # 존재하지 않는 업종이 선택되어 데이터가 없다면 '데이터가 없습니다' 로 도출
            service_bal = sang_bal[sang_bal['서비스_업종_코드_명']==smallBusiType] 
    
            # 업종의 분기별 평균을 토대로 예상매출액을 계산
            bal_1 = service_bal[service_bal['기준_분기_코드']==1]
            bal_1_a = bal_1['월요일_매출_금액'].mean()
            bal_1_b = bal_1['토요일_매출_금액'].mean()
            bal_1_c = bal_1['일요일_매출_금액'].mean()
            bal_1_mon = bal_1['월요일_매출_건수'].mean()
            bal_1_sat = bal_1['토요일_매출_건수'].mean()
            bal_1_sn = bal_1['일요일_매출_건수'].mean()
    
            bal_2 = service_bal[service_bal['기준_분기_코드']==2]
            bal_2_a = bal_2['월요일_매출_금액'].mean()
            bal_2_b = bal_2['토요일_매출_금액'].mean()
            bal_2_c = bal_2['일요일_매출_금액'].mean()
            bal_2_mon = bal_2['월요일_매출_건수'].mean()
            bal_2_sat = bal_2['토요일_매출_건수'].mean()
            bal_2_sn = bal_2['일요일_매출_건수'].mean()
    
            bal_3 = service_bal[service_bal['기준_분기_코드']==3]
            bal_3_a = bal_3['월요일_매출_금액'].mean()
            bal_3_b = bal_3['토요일_매출_금액'].mean()
            bal_3_c = bal_3['일요일_매출_금액'].mean()
            bal_3_mon = bal_3['월요일_매출_건수'].mean()
            bal_3_sat = bal_3['토요일_매출_건수'].mean()
            bal_3_sn = bal_3['일요일_매출_건수'].mean()
    
            bal_4 = service_bal[service_bal['기준_분기_코드']==4]
            bal_4_a = bal_4['월요일_매출_금액'].mean()
            bal_4_b = bal_4['토요일_매출_금액'].mean()
            bal_4_c = bal_4['일요일_매출_금액'].mean()
            bal_4_mon = bal_4['월요일_매출_건수'].mean()
            bal_4_sat = bal_4['토요일_매출_건수'].mean()
            bal_4_sn = bal_4['일요일_매출_건수'].mean()
    
            # 1분기 모델
            model_bal_1 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_bal).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[bal_1_a],'토요일_매출_금액':[bal_1_b],'일요일_매출_금액':[bal_1_c],
                                '월요일_매출_건수':[bal_1_mon],'토요일_매출_건수':[bal_1_sat],'일요일_매출_건수':[bal_1_sn]})
            pred1 = model_bal_1.predict(x_new2)
            
            print('실제값 1:',bal_1['분기당_매출_금액'].mean() / bal_1['점포수'].mean())
            print('예측값 1:',pred1 / bal_1['점포수'].mean())
    
    
            # 2분기 모델
            model_bal_2 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_bal).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[bal_2_a],'토요일_매출_금액':[bal_2_b],'일요일_매출_금액':[bal_2_c],
                                '월요일_매출_건수':[bal_2_mon],'토요일_매출_건수':[bal_2_sat],'일요일_매출_건수':[bal_2_sn]})
            pred2 = model_bal_2.predict(x_new2)
            
            print('실제값 2:',(bal_2['분기당_매출_금액'].mean()) / bal_2['점포수'].mean())
            print('예측값 2:',pred2 / bal_2['점포수'].mean())
    
    
            # 3분기 모델
            model_bal_3 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_bal).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[bal_3_a],'토요일_매출_금액':[bal_3_b],'일요일_매출_금액':[bal_3_c],
                                '월요일_매출_건수':[bal_3_mon],'토요일_매출_건수':[bal_3_sat],'일요일_매출_건수':[bal_3_sn]})
            pred3 = model_bal_3.predict(x_new2)
            
            print('실제값 3:',(bal_3['분기당_매출_금액'].mean()) / bal_3['점포수'].mean())
            print('예측값 3:',pred3 / bal_3['점포수'].mean())
    
    
            # 4분기 모델
            model_bal_4 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_bal).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[bal_4_a],'토요일_매출_금액':[bal_4_b],'일요일_매출_금액':[bal_4_c],
                                '월요일_매출_건수':[bal_4_mon],'토요일_매출_건수':[bal_4_sat],'일요일_매출_건수':[bal_4_sn]})
            pred4 = model_bal_4.predict(x_new2)
            
            print('실제값 4:',(bal_4['분기당_매출_금액'].mean()) / bal_4['점포수'].mean())
            print('예측값 4:',pred4 / bal_4['점포수'].mean())
            
            print(model_bal_1.summary())
    
        # 관광특구 예측모델 실행
        elif BigTradingArea == '관광특구':
            
            #관광특구
            cul=pd.read_csv("https://raw.githubusercontent.com/JustinChoiHokyeong/aniorimiro/master/aniorimiro/static/data/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EA%B4%80%EA%B4%91%ED%8A%B9%EA%B5%AC_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
            print('관광특구 매출 예상')
            sang_cul = cul[cul['상권_코드_명']==tradingArea]
            # 존재하지 않는 업종이 선택되어 데이터가 없다면 '데이터가 없습니다' 로 도출
            service_cul = sang_cul[sang_cul['서비스_업종_코드_명']==smallBusiType] 
        
            # 업종의 분기별 평균을 토대로 예상매출액을 계산
            cul_1 = service_cul[service_cul['기준_분기_코드']==1]
            cul_1_a = cul_1['월요일_매출_금액'].mean()
            cul_1_b = cul_1['토요일_매출_금액'].mean()
            cul_1_c = cul_1['일요일_매출_금액'].mean()
            cul_1_mon = cul_1['월요일_매출_건수'].mean()
            cul_1_sat = cul_1['토요일_매출_건수'].mean()
            cul_1_sn = cul_1['일요일_매출_건수'].mean()
        
            cul_2 = service_cul[service_cul['기준_분기_코드']==2]
            cul_2_a = cul_2['월요일_매출_금액'].mean()
            cul_2_b = cul_2['토요일_매출_금액'].mean()
            cul_2_c = cul_2['일요일_매출_금액'].mean()
            cul_2_mon = cul_2['월요일_매출_건수'].mean()
            cul_2_sat = cul_2['토요일_매출_건수'].mean()
            cul_2_sn = cul_2['일요일_매출_건수'].mean()
        
            cul_3 = service_cul[service_cul['기준_분기_코드']==3]
            cul_3_a = cul_3['월요일_매출_금액'].mean()
            cul_3_b = cul_3['토요일_매출_금액'].mean()
            cul_3_c = cul_3['일요일_매출_금액'].mean()
            cul_3_mon = cul_3['월요일_매출_건수'].mean()
            cul_3_sat = cul_3['토요일_매출_건수'].mean()
            cul_3_sn = cul_3['일요일_매출_건수'].mean()
        
            cul_4 = service_cul[service_cul['기준_분기_코드']==4]
            cul_4_a = cul_4['월요일_매출_금액'].mean()
            cul_4_b = cul_4['토요일_매출_금액'].mean()
            cul_4_c = cul_4['일요일_매출_금액'].mean()
            cul_4_mon = cul_4['월요일_매출_건수'].mean()
            cul_4_sat = cul_4['토요일_매출_건수'].mean()
            cul_4_sn = cul_4['일요일_매출_건수'].mean()
        
            # 1분기 모델
            model_cul_1 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_cul).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[cul_1_a],'토요일_매출_금액':[cul_1_b],'일요일_매출_금액':[cul_1_c],
                                '월요일_매출_건수':[cul_1_mon],'토요일_매출_건수':[cul_1_sat],'일요일_매출_건수':[cul_1_sn]})
            pred1 = model_cul_1.predict(x_new2)
        
            print('실제값 1:',(cul_1['분기당_매출_금액'].mean()) / cul_1['점포수'].mean())
            print('예측값 1:',pred1 / cul_1['점포수'].mean())
        
        
            # 2분기 모델
            model_cul_2 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_cul).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[cul_2_a],'토요일_매출_금액':[cul_2_b],'일요일_매출_금액':[cul_2_c],
                                '월요일_매출_건수':[cul_2_mon],'토요일_매출_건수':[cul_2_sat],'일요일_매출_건수':[cul_2_sn]})
            pred2 = model_cul_2.predict(x_new2)
        
            print('실제값 2:',(cul_2['분기당_매출_금액'].mean()) / cul_2['점포수'].mean())
            print('예측값 2:',pred2 / cul_2['점포수'].mean())
        
        
            # 3분기 모델
            model_cul_3 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_cul).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[cul_3_a],'토요일_매출_금액':[cul_3_b],'일요일_매출_금액':[cul_3_c],
                                '월요일_매출_건수':[cul_3_mon],'토요일_매출_건수':[cul_3_sat],'일요일_매출_건수':[cul_3_sn]})
            pred3 = model_cul_3.predict(x_new2)
        
            print('실제값 3:',(cul_3['분기당_매출_금액'].mean()) / cul_3['점포수'].mean())
            print('예측값 3:',pred3 / cul_3['점포수'].mean())
        
        
            # 4분기 모델
            model_cul_4 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_cul).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[cul_4_a],'토요일_매출_금액':[cul_4_b],'일요일_매출_금액':[cul_4_c],
                                '월요일_매출_건수':[cul_4_mon],'토요일_매출_건수':[cul_4_sat],'일요일_매출_건수':[cul_4_sn]})
            pred4 = model_cul_4.predict(x_new2)
        
            print('실제값 4:',(cul_4['분기당_매출_금액'].mean()) / cul_4['점포수'].mean())
            print('예측값 4:',pred4 / cul_4['점포수'].mean())
        
            print(model_cul_1.summary())
        
        # 골목상권 예측모델 실행 
        elif BigTradingArea == '골목상권':
            
            #골목상권
            gol=pd.read_csv("https://raw.githubusercontent.com/JustinChoiHokyeong/aniorimiro/master/aniorimiro/static/data/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EA%B3%A8%EB%AA%A9%EC%83%81%EA%B6%8C_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
            print('골목상권 매출 예상')
            sang_gol = gol[gol['상권_코드_명']==tradingArea]
            # 존재하지 않는 업종이 선택되어 데이터가 없다면 '데이터가 없습니다' 로 도출
            service_gol = sang_gol[sang_gol['서비스_업종_코드_명']==smallBusiType] 
        
            # 업종의 분기별 평균을 토대로 예상매출액을 계산
            gol_1 = service_gol[service_gol['기준_분기_코드']==1]
            gol_1_a = gol_1['월요일_매출_금액'].mean()
            gol_1_b = gol_1['토요일_매출_금액'].mean()
            gol_1_c = gol_1['일요일_매출_금액'].mean()
            gol_1_mon = gol_1['월요일_매출_건수'].mean()
            gol_1_sat = gol_1['토요일_매출_건수'].mean()
            gol_1_sn = gol_1['일요일_매출_건수'].mean()
        
            gol_2 = service_gol[service_gol['기준_분기_코드']==2]
            gol_2_a = gol_2['월요일_매출_금액'].mean()
            gol_2_b = gol_2['토요일_매출_금액'].mean()
            gol_2_c = gol_2['일요일_매출_금액'].mean()
            gol_2_mon = gol_2['월요일_매출_건수'].mean()
            gol_2_sat = gol_2['토요일_매출_건수'].mean()
            gol_2_sn = gol_2['일요일_매출_건수'].mean()
        
            gol_3 = service_gol[service_gol['기준_분기_코드']==3]
            gol_3_a = gol_3['월요일_매출_금액'].mean()
            gol_3_b = gol_3['토요일_매출_금액'].mean()
            gol_3_c = gol_3['일요일_매출_금액'].mean()
            gol_3_mon = gol_3['월요일_매출_건수'].mean()
            gol_3_sat = gol_3['토요일_매출_건수'].mean()
            gol_3_sn = gol_3['일요일_매출_건수'].mean()
        
            gol_4 = service_gol[service_gol['기준_분기_코드']==4]
            gol_4_a = gol_4['월요일_매출_금액'].mean()
            gol_4_b = gol_4['토요일_매출_금액'].mean()
            gol_4_c = gol_4['일요일_매출_금액'].mean()
            gol_4_mon = gol_4['월요일_매출_건수'].mean()
            gol_4_sat = gol_4['토요일_매출_건수'].mean()
            gol_4_sn = gol_4['일요일_매출_건수'].mean()
        
            # 1분기 모델
            model_gol_1 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_gol).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[gol_1_a],'토요일_매출_금액':[gol_1_b],'일요일_매출_금액':[gol_1_c],
                                '월요일_매출_건수':[gol_1_mon],'토요일_매출_건수':[gol_1_sat],'일요일_매출_건수':[gol_1_sn]})
            pred1 = model_gol_1.predict(x_new2)
        
            print('실제값 1:',(gol_1['분기당_매출_금액'].mean()) / gol_1['점포수'].mean())
            print('예측값 1:',pred1 / gol_1['점포수'].mean())
        
        
            # 2분기 모델
            model_gol_2 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_gol).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[gol_2_a],'토요일_매출_금액':[gol_2_b],'일요일_매출_금액':[gol_2_c],
                                '월요일_매출_건수':[gol_2_mon],'토요일_매출_건수':[gol_2_sat],'일요일_매출_건수':[gol_2_sn]})
            pred2 = model_gol_2.predict(x_new2)
        
            print('실제값 2:',(gol_2['분기당_매출_금액'].mean()) / gol_2['점포수'].mean())
            print('예측값 2:',pred2 / gol_2['점포수'].mean())
        
        
            # 3분기 모델
            model_gol_3 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_gol).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[gol_3_a],'토요일_매출_금액':[gol_3_b],'일요일_매출_금액':[gol_3_c],
                                '월요일_매출_건수':[gol_3_mon],'토요일_매출_건수':[gol_3_sat],'일요일_매출_건수':[gol_3_sn]})
            pred3 = model_gol_3.predict(x_new2)
        
            print('실제값 3:',(gol_3['분기당_매출_금액'].mean()) / gol_3['점포수'].mean())
            print('예측값 3:',pred3 / gol_3['점포수'].mean())
        
        
            # 4분기 모델
            model_gol_4 = smf.ols(formula = '분기당_매출_금액 ~ 서비스_업종_코드 + 월요일_매출_금액 + 토요일_매출_금액 + 일요일_매출_금액 + 월요일_매출_건수 + 토요일_매출_건수 + 일요일_매출_건수',data = service_gol).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[gol_4_a],'토요일_매출_금액':[gol_4_b],'일요일_매출_금액':[gol_4_c],
                                '월요일_매출_건수':[gol_4_mon],'토요일_매출_건수':[gol_4_sat],'일요일_매출_건수':[gol_4_sn]})
            pred4 = model_gol_4.predict(x_new2)
            print('실제값 4:',(gol_4['분기당_매출_금액'].mean()) / gol_4['점포수'].mean())
            print('예측값 4:',pred4 / gol_4['점포수'].mean())
        
            print(model_gol_1.summary())
        
        # 전통시장 예측모델 실행
        elif BigTradingArea == '전통시장':
            
            #전통시장
            jeon=pd.read_csv("https://raw.githubusercontent.com/JustinChoiHokyeong/aniorimiro/master/aniorimiro/static/data/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EC%A0%84%ED%86%B5%EC%8B%9C%EC%9E%A5_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
            print('전통시장 매출 예상')
            sang_jeon = jeon[jeon['상권_코드_명']==tradingArea]
            # 존재하지 않는 업종이 선택되어 데이터가 없다면 '데이터가 없습니다' 로 도출
            service_jeon = sang_jeon[sang_jeon['서비스_업종_코드_명']==smallBusiType] 
        
            # 업종의 분기별 평균을 토대로 예상매출액을 계산
            jeon_1 = service_jeon[service_jeon['기준_분기_코드']==1]
            jeon_1_a = jeon_1['월요일_매출_금액'].mean()
            jeon_1_b = jeon_1['수요일_매출_금액'].mean()
            jeon_1_c = jeon_1['목요일_매출_금액'].mean()
            jeon_1_bun = jeon_1['분기당_매출_건수'].mean()
        
            jeon_2 = service_jeon[service_jeon['기준_분기_코드']==2]
            jeon_2_a = jeon_2['월요일_매출_금액'].mean()
            jeon_2_b = jeon_2['수요일_매출_금액'].mean()
            jeon_2_c = jeon_2['목요일_매출_금액'].mean()
            jeon_2_bun = jeon_2['분기당_매출_건수'].mean()
        
            jeon_3 = service_jeon[service_jeon['기준_분기_코드']==3]
            jeon_3_a = jeon_3['월요일_매출_금액'].mean()
            jeon_3_b = jeon_3['수요일_매출_금액'].mean()
            jeon_3_c = jeon_3['목요일_매출_금액'].mean()
            jeon_3_bun = jeon_3['분기당_매출_건수'].mean()
        
            jeon_4 = service_jeon[service_jeon['기준_분기_코드']==4]
            jeon_4_a = jeon_4['월요일_매출_금액'].mean()
            jeon_4_b = jeon_4['수요일_매출_금액'].mean()
            jeon_4_c = jeon_4['목요일_매출_금액'].mean()
            jeon_4_bun = jeon_4['분기당_매출_건수'].mean()
        
            # 1분기 모델
            model_jeon_1 = smf.ols(formula = '분기당_매출_금액 ~ 월요일_매출_금액 + 수요일_매출_금액 + 목요일_매출_금액 + 분기당_매출_건수',data = service_jeon).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[jeon_1_a],'수요일_매출_금액':[jeon_1_b],'목요일_매출_금액':[jeon_1_c],
                                '분기당_매출_건수':[jeon_1_bun]})
            pred1 = model_jeon_1.predict(x_new2)
        
            print('실제값 1:',(jeon_1['분기당_매출_금액'].mean()) / jeon_1['점포수'].mean())
            print('예측값 1:',pred1 / jeon_1['점포수'].mean())
            result1 = (pred1 / jeon_1['점포수'].mean()).values[0]
        
        
            # 2분기 모델
            model_jeon_2 = smf.ols(formula = '분기당_매출_금액 ~ 월요일_매출_금액 + 수요일_매출_금액 + 목요일_매출_금액 + 분기당_매출_건수',data = service_jeon).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[jeon_2_a],'수요일_매출_금액':[jeon_2_b],'목요일_매출_금액':[jeon_2_c],
                                '분기당_매출_건수':[jeon_2_bun]})
            pred2 = model_jeon_2.predict(x_new2)
        
            print('실제값 2:',(jeon_2['분기당_매출_금액'].mean()) / jeon_2['점포수'].mean())
            print('예측값 2:',pred2 / jeon_2['점포수'].mean())
            result2 = (pred2 / jeon_2['점포수'].mean()).values[0]
        
        
            # 3분기 모델
            model_jeon_3 = smf.ols(formula = '분기당_매출_금액 ~ 월요일_매출_금액 + 수요일_매출_금액 + 목요일_매출_금액 + 분기당_매출_건수',data = service_jeon).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[jeon_3_a],'수요일_매출_금액':[jeon_3_b],'목요일_매출_금액':[jeon_3_c],
                                '분기당_매출_건수':[jeon_3_bun]})
            pred3 = model_jeon_3.predict(x_new2)
        
            print('실제값 3:',(jeon_3['분기당_매출_금액'].mean()) / jeon_3['점포수'].mean())
            print('예측값 3:',pred3 / jeon_3['점포수'].mean())
            result3 = (pred3 / jeon_3['점포수'].mean()).values[0]
        
            # 4분기 모델
            model_jeon_4 = smf.ols(formula = '분기당_매출_금액 ~ 월요일_매출_금액 + 수요일_매출_금액 + 목요일_매출_금액 + 분기당_매출_건수',data = service_jeon).fit()
            x_new2 = pd.DataFrame({'서비스_업종_코드':[5],
                                '월요일_매출_금액':[jeon_4_a],'수요일_매출_금액':[jeon_4_b],'목요일_매출_금액':[jeon_4_c],
                                '분기당_매출_건수':[jeon_4_bun]})
            pred4 = model_jeon_4.predict(x_new2)
        
            print('실제값 4:',(jeon_4['분기당_매출_금액'].mean()) / jeon_4['점포수'].mean())
            print('예측값 4:',pred4 / jeon_4['점포수'].mean())
            result4 = (pred4 / jeon_4['점포수'].mean()).values[0]  
            
            print(model_jeon_1.summary())

          

        context = {
          'businessType':businessType,
          'tradingArea':tradingArea,
          'BigTradingArea':BigTradingArea,
          'smallBusiType':smallBusiType,
          'result1':result1,
          'result2':result2,
          'result3':result3,
          'result4':result4
        }
        
    return JsonResponse(context)






  
