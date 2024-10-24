# Operation_Orchid
*Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.*

## Solution
1. Extract disk image
2. Use `fdisk`,  `fls`, and `icat` to analyze the disk and find the `.ash_history` and an encrypted flag-file
3. `openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567` (taken from the history-file) will decrypt the flag


## Flag
**Flag:** `picoCTF{h4un71ng_p457_0a710765}`
