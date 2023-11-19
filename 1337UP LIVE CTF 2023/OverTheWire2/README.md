# Over the Wire (part 2)

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2023](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2134)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Warmup |
|  **Solves** |  166  |
|  **Difficulty** |  Easy |
| **Files** |  [otw_pt2.pcap](<otw_pt2.pcapng>)  |

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/c528a8b1-e7e8-4284-88c1-fd127096ba12)

# Solution

We get an pcap file as source. Lets open it in wireshark and check the protocol hierarchy:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/c4f657c1-6b03-4ab5-87c0-ef51e9f38d73)

There is a lot of different protocols captured in this capture. One interesting one is SMTP(Simple Mail Transfer Protocol). <br/>
Lets filter on smtp and follow the traffic:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/121b5a56-0ad9-4623-9f22-af0bad0544a1)

It's some communication between 0xM4hm0ud and Cryptocat. It's talking about hiding future secret messages. In stream 114 we can find this message:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/80900788-36bd-404a-8730-4ed14f377065)

We can see some image sent as base64. When saving the base64 as an image we can see that it's just an picture of a cat. As in the message before they probaly used some steg technique to hide messages.
When we run `exiftool` we can see this:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/d2bbaa58-0aca-419e-915a-5c1a1c215ac5)

but this not the flag. Lets check the other packets. In stream 150 we can see another image. This one is a png file. We can use `zsteg` on png images.
When we run zsteg we can see the flag(flag is hidden in lsb):

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/e3bd7cae-cb1b-4706-832b-6c6467cf01c8)
