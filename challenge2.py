
# 寫一個function來印出誰的成績是第二高，如果超過一個人分數都是第二高，請把人名一行一行印出來
# function的參數 : students = [['Jerrt', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 94], ['Harsh', 90]]

def second_highest(students):
	if len(students) < 2:
		return 'no runner up'
	else:
		max = students[0][1]
		for student in students:
			if student[1] > max:
				max = student[1]
		runner_up_grade = 0
		for student in students:
			if student[1] < max:
				if student[1] > runner_up_grade:
					runner_up_grade = student[1]
					runner_up = student[0]
				elif student[1] == runner_up_grade:
					runner_up = runner_up + '\n' + student[0]
					runner_up_grade = student[1]
	return runner_up

runner_up = second_highest([ ['Tom', 90], ['Jerrt', 88], ['Justin', 84], ['Akriti', 94], ['Harsh', 90]])
print(runner_up)

# 解答----------------------------------------

def second_highest_ans(students):
    grades = [s[1] for s in students] # 只把成績拿出來
    grades = sorted(grades, reverse=True)
    second = grades[1] # grades[0]是最高，grades[1]是第二高
    
    # 再下來找誰是這個分數
    # 底下這句話的意思是拿到 所有分數跟第二高一樣的人的"人名"也就是s[0]的部分
    # 記得嗎 參數的這個students清單裡面的東西，s[0]是人名，s[1]是分數
    second_high_students = [s[0] for s in students if s[1] == second]
    for student in second_high_students:
        print(student)

students = [ ['Tom', 90], ['Jerrt', 88], ['Justin', 84], ['Akriti', 94], ['Harsh', 90]]
print( second_highest_ans(students) )
