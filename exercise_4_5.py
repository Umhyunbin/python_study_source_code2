number_1 = int(input())            # 사용자 입력 수 1,input해서 넣은 값이 텍스트로 number_1에 들어가기때문에 형 변환 필요.
number_2 = int(input())            # 사용자 입력 수 2,input해서 넣은 값이 텍스트로 number_2에 들어가기때문에 형 변환 필요.
result = number_1 + number_2  # 계산
print('결과: ' + str(result))      # 결과 출력,result가 이미 정수로 바뀌었기 때문에 결과라는 string과 연결되려면 형 변환 필요.