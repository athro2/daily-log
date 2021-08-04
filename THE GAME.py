people1 = "짱구"
people2 = "철수"
answer1 = 5
answer2 = 7
win = answer1 > answer2

print("길을 가던 " + people1 + "와 " + people2 + "는 사나이의 자존심을 걸고 숫자놀이를 하기로 하였다")
print("숫자놀이란 더 큰 숫자를 내는 사람이 이기는 경기였다")
print("" + people1 + "는 " + str(answer1) + "을 냈고 " + people2 + "는 " + str(answer2) + "을 냈다")
print("Q: " + people1 + "는 " + people2 + "를 이겼다. 사실일까? A: " + str(win))

#해당 코드는 다음과 같이 변경이 가능하지만 ,는 띄어쓰기 처리된다.
#print("길을 가던 ", people1, "와 ", people2, "는 사나이의 자존심을 걸고 숫자놀이를 하기로 하였다")
#print("숫자놀이란 더 큰 숫자를 내는 사람이 이기는 경기였다")
#print("", people1 + "는 ", answer1, "을 냈고 ", people2, "는 ", answer2, "을 냈다")
#print("Q: ", people1, "는 ", people2, "를 이겼다. 사실일까?: A: " + str(win))
