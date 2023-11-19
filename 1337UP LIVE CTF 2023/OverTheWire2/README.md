# Over the Wire (part 2)

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2023](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2134)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Warmup |
|  **Solves** |  166  |
|  **Difficulty** |  Easy |
| **Files** |  [otw_pt2.pcap](<otw_pt2.pcapng>)  |

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/d8b946f1-8228-497c-bb2a-b6e6a49473d7)

# Solution

We get an pcap file as attachment. Lets open it in wireshark and check the protocol hierarchy:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/37f3c064-6416-43cb-8281-a8fad885a0d9)


There is a lot of different protocols captured in this capture. One interesting one is SMTP(Simple Mail Transfer Protocol). <br/>
Lets filter on smtp and follow the traffic:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/a176ffbd-ac32-45a5-ba06-c308a21c59e8)


It's some communication between 0xM4hm0ud and Cryptocat. It's talking about hiding future secret messages. In stream 114 we can find this message:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/f14f321c-59c9-4647-9989-860d8fbab26b)


We can see some image sent as base64. When saving the base64 as an image we can see that it's just an picture of a cat. As in the message before they probaly used some steg technique to hide messages.
When we run `exiftool` we can see this:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/f5dc3cdb-bae5-4a9c-a6c4-ecc08c131c8f)


but this not the flag. Lets check the other packets. In stream 150 we can see another image. This one is a png file. We can use `zsteg` on png images.
When we run zsteg we can see the flag(flag is hidden in lsb):

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/b87a9ad6-0d58-4ce4-9629-aeea4619a8eb)

