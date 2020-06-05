def median(data):
    """데이터의 중앙값을 반환한다."""
    sorted_data = sorted(data)
    median_value = sorted_data[int(len(sorted_data) / 2)] #float대신 integer나 slice가 와야한다. 그래서 int형으로 형변환을 하였다.
    return median_value
    
print(median([10, 9, 4, 1, 5, 7]))