# Sleuthkit_Apprentice
*Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.*

## Solution
1. `sudo fdisk -lu disk.flag.img`
2. `fls -o 360448 disk.flag.img -r`
3. `icat -o 360448 disk.flag.img 2371`


## Flag
**Flag:** `picoCTF{by73_5urf3r_2f22df38}`
