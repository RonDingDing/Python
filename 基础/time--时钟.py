import time
while True:
        t = time.localtime()
        print("\r现在时刻: %d 年 %d 月 %d日 %d 时 %d 分 %d 秒 星期 %d" \
              % (t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec,t.tm_wday+1)
              ,end='')    
        time.sleep(1)
        print("\n")
 
