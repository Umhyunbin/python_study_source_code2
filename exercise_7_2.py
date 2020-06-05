happiness = {
    '호주': 7.95,
    '노르웨이': 7.9,
    '미국': 7.85,
    '일본': 6.2,
    '한국': 5.75,
}

for nation,number in happiness.items():
    print(nation,"사람들은",number,'만큼 행복합니다.')

천간 = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
지지 = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']

for m_10 in 천간:
    for n_10 in 지지:
        print(m_10+n_10,end=" ")
    print()

list1=[1,2,3]
list2=[4,5,6]

def plus_elements(list1,list2):
    big_list=list(zip(list1,list2))
    result=big_list[0][0]+big_list[0][1],big_list[1][0]+big_list[1][1],big_list[2][0]+big_list[2][1]
    result_list=list(result)
    print(result_list)
plus_elements(list1,list2)

