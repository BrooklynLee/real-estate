# TODO 

# CH1.  부동산 데이터 분석

## 1.1 부동산 데이터
## 1.2 데이터 분석

# CH2. 파이썬 데이터 분석 환경 구성 (개발 환경 구성)

## 아나콘다 & 주피터노트북 환경 구성

* anaconda 설명 & 설치하는 방법
* jupyter-notebook 설명 & 설치하는 방법

## 파이썬 기본 문법 (+ 데이터 분석을 위한 패키지 설명)

* python 문법 설명
  * list/dict/loop/data-type
* pandas 설명
  * 엑셀을 대체 할 수 있다.
  * select/join/concat/merge
  * data I/O
* matplotlib 설명
  * 복잡한 데이터를 한눈에 파악하는 시각화
  * plotting/histogram/chart

# CH3 의미있는 데이터 가져오기 및 관리

3.1 데이터 가져오기

3.1.1.부동산 실거래 매매 데이터 가져오기

* 공공데이터 포털에서 실거래 (매매/전세) 데이터 가져오기 
  * 소스코드 제공
* 신규아파트 분양가격 동향 
  * 소스코드 제공
3.1.2 데이터 스크랩하기 (필요한 데이터 직접 가져오기)

* BeautifulSoup, Selenium 설명
* 네이버 부동산 매물 데이터 가져오기  

3.2 데이터 관리하기

* Elasticsearch 설명
  * Index
  * put/get/update
  * Kibana

# CH4 부동산 데이터 분석하기

* 부동산 데이터 분석 맛보기
  * pandas
    * select/join/concat/merge
  * matplotlib
    * plotting/histogram/chart
* 데이터 분석 단계 [view more](https://www.northeastern.edu/graduate/blog/data-analysis-project-lifecycle/)
  * 비즈니스에 대한 이해
  * 수집
  * 전처리 (클렌징/포맷팅/샘플)
  * 분석 (중요한 요소 찾기/모델링)
  * 검증
  * 시각화

* 평당 가격이 가장 비싼 동네는 바로 ㅇㅇ다.
* KB 부동산 데이터 따라하기 [kb liveon](https://onland.kbstar.com/quics?page=C059743)
  * (주/월)간 아파트 (전세/매매) 가격 동향 
  * pandas, matplot을 이용해서 동일하게 나타내기
* 주택 가격 증감률 (매매증감, 전세 증감)

# CH5 재미로 보는 부동산 분석 

* 단지를 나타내는 키워드들 시각화
  * Wordcloud [view more](https://lovit.github.io/nlp/2018/04/17/word_cloud/)
* 금리와 부동산의 관계
  * 금리 데이터 [view more](https://ecos.bok.or.kr/)
  * correlation matrix [view more](https://stackoverflow.com/questions/29432629/plot-correlation-matrix-using-pandas)
* 수요/공급과 부동산 가격
  * 9.13 부동산 정책이준 부동산의 영향은?
* 부동산 가격에서 가장 영향을 미치는 요소는 무엇일까?
  * feature selection [view more](https://towardsdatascience.com/a-feature-selection-tool-for-machine-learning-in-python-b64dd23710f0)
