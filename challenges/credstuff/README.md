# credstuff
*We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it? Download the leak here. The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.*

## Solution
1. Follow instructions; Figure out which line in usernames.txt `cultiris` is on, then get that line from passwords.txt
2. `https://cyberchef.org/#recipe=ROT13(true,true,false,13)&input=Y3ZwYlBHU3tQN2UxU181NEkzNV83MVozfQo`


## Flag
**Flag:** `picoCTF{C7r1F_54V35_71M3}`
