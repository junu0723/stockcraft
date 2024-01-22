# cbd : Corporation Base Data
#
# base data로 활용하기 위한 기업 기본 정보입니다.
# 기업 공시 기본 내용이 변경되는 경우에 해당하는 trigger를 알 수 있다면, 그 것만 가져오면 되지만, 불가능하다면 매일 최신 정보를 긁어오는게 최선이지 않을까 싶습니다.
# 대한민국 기업 공시 채널 (krx)에서 기업 기본 정보(Corporation Base Data를 crawling해서 local에 저장 
# 
# /data 가 writable 해야함
#
# ==============================================

import pandas as pd
import time
from util import pysys

DATA_PATH = '/data'
TARGET_DATE = time.strftime('%Y%m%d')
CBD_PATH = f'{DATA_PATH}/base/cbd/{TARGET_DATE}'

stock_type = {
    'kospi': 'stockMkt',
    'kosdaq': 'kosdaqMkt'
}

# def get_target_date():
#     global TARGET_DATE
#     if len(sys.argv) > 1:
#         TARGET_DATE=sys.argv[1]
#         print(f'target date is {TARGET_DATE}')
#     else:
#         print(f'no specified target date. default target date is {TARGET_DATE}')

def get_cbd(market_type=None):
    print(f'processing market_type: {market_type}')
    download_link = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&marketType='
    download_link = download_link + stock_type[market_type]

    df = pd.read_html(download_link, header=0)[0]
    if market_type == 'kospi':
        df.종목코드 = df.종목코드.map('{:06d}.KS'.format)
    elif market_type == 'kosdaq':
        df.종목코드 = df.종목코드.map('{:06d}.KQ'.format)
    else:
        print('wrong market type')
    return df.copy()


def main():
    print(f"cbd.py starts : {time.strftime('%Y%m%d%H%M%S')}")
    # get_target_date()
    pysys.clean(CBD_PATH)
    pysys.mkdir(CBD_PATH)
    kospi_df = get_cbd('kospi')
    kosdaq_df = get_cbd('kosdaq')
    kospi_df.to_parquet(f'{CBD_PATH}/kospi.pq.gz', compression='gzip')
    kosdaq_df.to_parquet(f'{CBD_PATH}/kosdaq.pq.gz', compression='gzip')

    mdm_df = pd.concat([kospi_df, kosdaq_df])
    mdm_df.to_parquet(f'{CBD_PATH}/kr-full.pq.gz', compression='gzip')

    code_df = mdm_df[['회사명', '종목코드']]
    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    code_df.to_parquet(
        f'{CBD_PATH}/stock-code.pq.gz', compression='gzip')
    print(f"cbd.py ends : {time.strftime('%Y%m%d%H%M%S')}")

if __name__ == '__main__':
    main()
