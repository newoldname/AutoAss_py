srt = open("ori.srt","r",encoding="utf-8")
mstime = open("mstime.txt","w",encoding="utf-8")
oriarr = srt.readlines()
print(oriarr)
for i in range(len(oriarr)):
     if oriarr[i][0] == "(":
         if oriarr[i-1].count("-->"):
            times = oriarr[i-1].split(":",3)
            times[3] = times[2]
            times[2] = times[2].split(",",1)[0]
            times[3] = times[3].split(" ",1)[0]
            times[3] = times[3].split(",",1)[1]
            for j in range(0,4):
                times[j] = int(times[j])
            sum = times[3] +times[2] * 1000 + times[1] * 60 * 1000 + times[0] * 60*60*1000
            line = str(sum) + "\n"
            mstime.write(line)

srt.close()
mstime.close()
