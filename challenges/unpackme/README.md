# unpackme
*Can you get the flag? Reverse engineer this binary.*

## Solution
1. `upx -d unpackme-upx -o unpacked`
2. Use gdb to disassemble into asm
3. We're comparing a number to a set value, so look for a `cmp` operation
4. find `0x0000000000401ec8 <+133>:	cmp    $0xb83cb,%eax`
5. Convert `0xb83cb` from hex to decimal (www.rapidtables.com/convert/number/hex-to-decimal.html?x=B83CB)
6. Run code, input `754635`, get flag


## Flag
**Flag:** `picoCTF{up><_m3_f7w_77ad107e}`
