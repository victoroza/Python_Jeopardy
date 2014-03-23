filename = str(input("filename: "))
f = open(filename,'a')
topic = str(input("topic: "))
f.write(topic+"\n")
write = "not null"
while write:
  cash = str(input("cash: "))
  write = cash
  question = str(input("question: "))
  answer1 = str(input("answer1: "))
  answer2 = str(input("answer2: "))
  answer3 = str(input("answer3: ")) 
  answer4 = str(input("answer4: "))
  ans = str(input("correct answer: "))
  if write != "":
    f.write(cash+","+question+","+answer1+","+answer2+","+answer3+","+answer4+","+ans+"\n")
f.close()
