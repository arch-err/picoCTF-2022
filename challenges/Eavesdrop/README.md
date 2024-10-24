# Eavesdrop
*Download this packet capture and find the flag.*

## Solution
1. Open in wireshark, follow TCP
2. Find the following command from some type of chat: `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`
3. Carve out encrypted file sent in pcap
4. Run command given and get flag


## Flag
**Flag:** `picoCTF{nc_73115_411_5786acc3}`
