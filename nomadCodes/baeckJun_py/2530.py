#인공지능시계
h,m,s = input().split()
enter = int(input())

#초
s1 = (int(s) + enter)%60

#분
m1 = int(m) + int((int(s) + enter)/60)
m2 = m1%60

#시
h1 = int(h) + int(m1/60)
h2 = h1%24

print(f"{h2} {m2} {s1}")