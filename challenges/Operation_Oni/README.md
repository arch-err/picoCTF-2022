# Operation_Oni
*Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.*
*Additional details will be available after launching your challenge instance.*

## Solution
1. Use sleuth tools to find and extract `key_file`
2. `ssh -i key_file -p 58904 ctf-player@saturn.picoctf.net "cat flag.txt"`


## Flag
**Flag:** `picoCTF{k3y_5l3u7h_339601ed}`
