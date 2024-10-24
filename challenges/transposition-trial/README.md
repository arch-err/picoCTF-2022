# transposition-trial
*Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message. Download the corrupted message here.*

## Solution
1. Notice that every third character has been shifted two places forward
2. Construct a vim macro, ex. `llxhhPlll`, and run it
3. Realize that this breaks on the last step, so do that one manually :P


## Flag
**Flag:** `picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}`
