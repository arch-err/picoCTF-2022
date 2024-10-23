# Sleuthkit_Intro
*Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.*

## Solution
1. `sudo fdisk -lu disk.img`
2. Identify start byte, `2048` in this case
3. `sudo losetup -o $((512*2048)) /dev/loop0 ./disk.img`
4. `sudo mount /dev/loop0  ./mnt`
5. Discover a linux fs and...
6. Reread the fucking challenge description and do what it says...


## Flag
**Flag:** `picoCTF{mm15_f7w!}`
