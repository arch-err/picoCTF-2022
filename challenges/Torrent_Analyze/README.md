# Torrent_Analyze
*SOS, someone is torrenting on our network. One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like picoCTF{filename}. Captured traffic.*

## Solution
1. Realize that the hashes in the `bt-dht` packets are filenames
2. Export all packets with a hash, use vim some vim magic to transform the wireshark export to a list of unique hashes
3. Google the hashes, one hash (`e2467cbf021192c241367b892230dc1e05c0580e`) is the hash of the filename `ubuntu-19.10-desktop-amd64.iso`
4. Wrap the filename in `picoCTF{}`


## Flag
**Flag:** `picoCTF{ubuntu-19.10-desktop-amd64.iso}`
