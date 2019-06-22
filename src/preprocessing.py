# -*- encoding: utf8 -*-

import pandas as pd 

def join_meta(df, r_df): 
    df['지역코드'] = df['지역코드'].astype(str)
    df[['시', '구', '도로명']] = df['지역코드'].apply(lambda x: r_df.loc[x])
    df['시군구'] = df['시'] + ' ' + df['구']
    return df

def preprocessing(df):
    df['평수'] = df['전용면적'].apply(lambda x: x / float(3.30578))
    # 60m2이하, 60~85m2, 85m2초과 
    labels = ["60m이하", "60-85m2이하", "85m2초과"]
    df['규모'] = pd.cut(df['전용면적'], [0, 65, 85, 99999999],labels = labels)
    df['건축년도'] = df['건축년도'].astype(str)
    df['년'] = df['년'].astype(str)
    df['월'] = df['월'].astype(str)
    df['date'] = df['date'].astype(str)
    df['date'] = pd.to_datetime(df['date'], format="%Y%m")
    return df

def preprocessing_rent(df): 
    df['보증금액'] = df['보증금액'].apply(lambda x: int(x.replace(',', '')))  
    df['월세금액'] = df['월세금액'].astype(str).apply(lambda x: int(x.replace(',', '')))
    df['거래금액'] = df['보증금액'] + 24 * df['월세금액']
    df['평당거래액'] = df['거래금액'] / df['전용면적'] 
    df = preprocessing(df) 
    return df

def preprocessing_trade(df):
    df['거래금액'] = df['거래금액'].apply(lambda x: int(x.replace(',', ''))) 
    df['평당거래액'] = df['거래금액'] / df['전용면적']
    df = preprocessing(df)
    return df