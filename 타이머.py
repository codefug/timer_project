#시간 시작
starttime=time.time()
lasttime=starttime
lapnum=1
value=""

print("Press ENTER for each lap. \nType Q and press ENTER to stop")

while value.lower()!="q":
    
    value=input()
    laptime=round((time.time()-lasttime),2)
    totaltime=round((time.time()-starttime),2)
    print("Lap No."+str(lapnum))
    print("Total Time: "+str(totaltime))
    print("Lap Time: "+str(laptime))
            
    print("*"*20)
  
    # Updating the previous total time and lap number
    lasttime = time.time()
    lapnum += 1
  
print("Exercise complete!")