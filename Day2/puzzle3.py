valid_passwd=0
with open("Input_policy_password.txt","r",encoding="utf8") as f:
    for line in f:
        lower=int(line.split()[0].split("-")[0])
        upper=int(line.split()[0].split("-")[1])
        var=line.split()[1].strip(":")
        passw=line.split()[2]
        if lower<=passw.count(var)<=upper:
            valid_passwd+=1
print(valid_passwd)
