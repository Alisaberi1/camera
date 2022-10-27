


x_first,y_first=map(int,input().split())
x_second,y_second=map(int,input().split())
x_third,y_third=map(int,input().split())
k_first_to_third=(y_third+y_first)-y_second

x_forth = x_second if x_first==x_third else (x_first+x_third)-x_second
y_forth=y_second if y_first==y_third else (k_first_to_third)
print(x_forth, y_forth)
