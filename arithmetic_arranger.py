import re
def arithmetic_arranger(problems, show=False):
  if (len(problems)>5):
    return "Error: Too many problems."
  reg1="^\s*\d+\s*\D\s*\d+"
  reg2="^\s*\d{5,}\s*\D\s*\d{5,}"
  reg3="^\s*\d+\s*[*\/]\s*\d+"
  b=[]
  for problem in problems:
    if not (bool(re.match(reg1,problem))): 
      return "Error: Numbers must only contain digits."
    if (bool(re.match(reg2,problem))):
      return "Error: Numbers cannot be more than four digits."
    if (bool(re.match(reg3,problem))):
      return "Error: Operator must be '+' or '-'."
    b.append(problem.split(" "))
  first=""
  second=""
  third=""
  last=""
  results=[]
  #print(b)
  for pr in b:
    l=max(len(pr[0]),len(pr[2]))+2
    #print (l)
    text="{:>"+str(l)+"}"
    first+=text.format(pr[0])+"    "
    text2="{:>"+str(l-1)+"}"
    second+=pr[1]+text2.format(pr[2])+"    "
    third+="-"*l+"    "
    if (pr[1]=="+"):
      results=int(pr[0])+int(pr[2])
    else:
      results=int(pr[0])-int(pr[2])
    last+=text.format(str(results))+"    "
    #if (ind==len(b)):
      #print
      
  ret=first[:len(first)-4]+"\n"+second[:len(second)-4]+"\n"+third[:len(third)-4]
  if (show):
    ret+="\n"+last[:len(last)-4]
  return ret