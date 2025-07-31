import pandas as pd
# 스타벅스 csv파일 수정 -
#df = pd.read_csv('starbucks.csv', encoding='cp949')
# 0번째 열에 스타벅스 이름 추가
#df.iloc[:, 0] = '스타벅스 ' + df.iloc[:, 0].astype(str)
# navicode 일괄 부여
#prefix = '3232A'
#df.iloc[:, 1] = [f"{prefix}{i+1}" for i in range(len(df))]

#df.to_csv('starbucks.csv', index=False, encoding='cp949')

#df = pd.read_csv('starbucks.csv', encoding='cp949')

#print(df.iloc[:, 1].head()) //



#df = pd.read_csv('starbucks.csv', encoding='cp949')

#df['type'] = '1' # dynamic = 1

#df.to_csv('starbucks.csv', index=False, encoding='cp949')
def add(name:str, navicode:str, lati:float, long:float, type:int = 2):
    df = pd.read_csv('starbucks.csv', encoding='cp949')

    new_row = {
        'name': name,
        'navicode': navicode,
        'latitude': lati,
        'longitude': long,
        'type': type
    }
    new_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_df], ignore_index=True)

    df.to_csv('starbucks.csv', index=False, encoding='cp949')

add('찌개로돈가스길',1111, 35.822565, 128.7551445, 2)