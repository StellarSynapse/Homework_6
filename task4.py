days = ["Monaday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

week = {}
week_={}
for num, day in enumerate(days):
    week.update({int(num)+1:day})

for num, day in enumerate(days):
    week_.update({day:int(num)+1})
print(week)
print(week_)
