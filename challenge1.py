
# 寫一個function來找出清單中的最大數
def find_max(a_list):
	max = 0
	for data in a_list:
		if data > max:
			max = data
	return max

# 解答----------------------------------------

def find_max_ans(a_list):
	if not a_list:  # 檢查a_list有沒有東西，如果有東西，這條就是True
		return 0
	max_num = a_list[0]:
	for num in a_list:
		if num > max_num:
			max_num = num
	return max_num
