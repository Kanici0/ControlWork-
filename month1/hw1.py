Monday =  float ( input('введите трату за понедельник'))
Tuesday = float (input('введите трату за вторник'))
Wednesday = float (input('введите трату за среду'))
Thursday = float (input('введите трату за четветк'))
Friday =float (input('введите трату за патницу'))
Saturday = float (input('введите трату за суботу'))
Sunday = float (input('введите трату за воскресение'))


total_expense =  int(Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday)
b = round(total_expense/ 7 )


print("расход за неделю :",total_expense)
print("средний расход :",b)


