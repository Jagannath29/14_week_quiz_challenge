# function, lambda

def ger_high_avg_mark(std_mark):
    highest_avg_mark = max(std_mark, key=lambda x: sum(std_mark[x])/len(std_mark[x])) 
    return highest_avg_mark


mark = {
    'Jaguar': [20,30,40,50],
    'hen': [10,38,80,30],
    'cat': [55,60,20,90],
    'dog': [42,39,62,55]
}
print(ger_high_avg_mark(mark))
    