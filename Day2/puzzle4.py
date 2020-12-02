valid_passwd=0
with open("Input_policy_password.txt","r",encoding="utf8") as f:
    for line in f:
        lower=int(line.split()[0].split("-")[0])
        upper=int(line.split()[0].split("-")[1])
        var=line.split()[1].strip(":")
        passw=line.split()[2]
        if passw.find(var,lower-1)==lower-1 and passw.find(var,upper-1)==upper-1:
            continue
        elif passw.find(var,lower-1)==lower-1:
            valid_passwd+=1      
        elif passw.find(var,upper-1)==upper-1:
            valid_passwd+=1
print(valid_passwd)
