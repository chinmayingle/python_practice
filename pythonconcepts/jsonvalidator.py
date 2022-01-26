import re
data2='''
{
  "id": "test",
  "name": "name",
  "hmm": [1,23,4.2],
  "cool":{"":}
}
'''

#test case 1:Duplicate keys
# {
#   "id": "test",
#   "name": "name",
#   "hmm": [1,23,4.2],
#   "hmm" : "sss"
# }

# test case 2:formating not correct
# {
#   "id"= "test",
#   "name": "name",
#   "hmm": [1,23,4.2],
#   "hmm" : "sss"
# }

# test case 3:format not correct comma
# data2='''
# {
#   "id": "test",
#   "name": "name",
#   "hmm": [1,23,4.2],
# }
# '''


#for simple json to check duplicate keys 1st attempt
def isjsonvalid(string):
    # print(string)
    # pattern=re.compile(r)
    x= re.findall("\{([a-zA-Z0-9\"\:,\[\]\{\}\t\n\.\_\- ]*)\}",string)
    # print(x)
    storekeys=set()
    for i in x:
      # print
      temp=(i.strip(' \t\n\r').split(","))
      print(temp)
      for j in temp:
        # print(j)
        lenb4=len(storekeys)
        print(j.strip(' \t\n\r"').split(":"))
        storekeys.add(j.strip(' \t\n\r"').split(":")[0])
        if lenb4 == len(storekeys):
          # print("duplicate key")
          raise Exception("duplicate key")
      print(storekeys)

#considering " and ' as same currently
def valjson(string):
  #remove all the whitespaces
  string=string.replace(" ","")
  string=string.replace("\t","")
  string=string.replace("\n","")
  
  print(string)
  # tp =re.findall(re.compile(r'(\"[a-zA-Z0-9-_]*\"):(?:\"| |\t)((\"[a-zA-Z0-9]*\")|(?:[0-9]*[.])?[0-9]+)'),string)
  # print(tp)
  index=0
  stringlen=len(string)
  tempchar=""
  status="key"
  storekeys=set()

  while index<stringlen:
    # print(string[index])

    #key or value
    if string[index]=='"' or string[index]=="'":
      # print("innnn",1,status)
      tempchar+=string[index]
      index+=1
      while (string[index]!='"') and index< stringlen:
        # print("ajun")
        # print(string[index])
        tempchar+=string[index]
        # print("tempcar",tempchar)
        if index==stringlen-1:
          print("not valid")
          break
        # else:
          # print("hmm",tempchar)
          # tempchar=""
        index+=1
      tempchar+=string[index]
      # print("temp",tempchar)

      #checking duplicates for keys
      if status == "key":
        # print(storekeys)
        lenb4=len(storekeys)
        storekeys.add(tempchar)
        if lenb4 == len(storekeys) and status=="key":
          print("duplicate key")
          raise Exception("duplicate key")
      else:
        status="key"
      tempchar=""

    #: is followed by the value hence status as value to ignore it from duplicate key check
    elif string[index]==":":
      # print("innnn",":")
      status="Value"

    #code for json array need to add validation
    elif string[index]=="[":
      # print("innnn","[")
      tempchar+=string[index]
      index+=1
      while (string[index]!=']') and index< stringlen:
        # print("ajun")
        # print(string[index])
        tempchar+=string[index]
        # print("tempcar",tempchar)
        if index==stringlen-1:
          print("not valid")
          break
        # else:
          # print("hmm",tempchar)
          # tempchar=""
        index+=1
      tempchar+=string[index]
      # print("temp",tempchar)
      tempchar=""
      status="key"

    #value is json itself to take it and call this function again partially completed
    elif (string[index]=="{" and status=="Value"):
      # print("innnn",status,"{",string[index])
      # break

      tempchar+=string[index]
      index+=1
      while (string[index]!='}') and index< stringlen:
        # print("ajun",index)
        print(string[index])
        tempchar+=string[index]
        # print("tempcar",tempchar)
        if index==stringlen-1:
          print("not valid")
          break
        # else:
          # print("hmm",tempchar)
          # tempchar=""
        index+=1
      tempchar+=string[index]
      # print("temp{",tempchar)

      #recurvise calling to check the value which itself is a json
      if valjson(tempchar) == False:
        return False
      tempchar=""

    #last comma
    elif string[index]=="," and string[index]=="}":
      # print("----",status)
      return False

    #first char of json
    elif string[index]=="{" or string[index]==",":
      index+=1
      continue
    elif string[index]=="}":
      return True
    
    else:
      # print("lasttt")
      return False

    # elif string[index]=""
    index+=1

  return True




if __name__=='__main__':
    try:
      # isjsonvalid(data2)
      print(valjson(data2))
    except Exception as e:
      print(e)