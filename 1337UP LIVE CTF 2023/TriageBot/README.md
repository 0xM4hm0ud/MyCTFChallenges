# TriageBot

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2023](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2134)  |
|  **Author** |  0xM4hm0ud & CryptoCat |
|  **Category** |  Warmup |
|  **Solves** |  27  |
|  **Difficulty** |  Easy |

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/3efe6384-de20-4c61-8345-802beac65d4b)

# Solution

The description talks about an new bot and also about an `beta` for full functionality.
Lets go to the discord server and talk with the bot.

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/723c2aad-8d7d-4703-85a2-eaae61e6a69f)


We have an few options we can send.
Those 3 arent helpful and is just sending the same message every time we call the option:

```
!anyupdate - Check for updates
!support - Ask for support
!bountyplz - Get a bounty
```

When we try the option `!triage` it responds with this:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/74e7e335-c4d5-4219-aa53-ebb3d9b4a6be)

So we are not a beta tester. In the description it talks about a beta role. The bot is inside the Intigriti server and we can't assign a role ourselves. So we need to invite the bot to our own server.
For this we need an invite link. We need to generate the link. We can do it 2 ways. Search online for a random bot and copy the link or enable developer mode and go to the portal where you can generate links aswell(after creating a bot).
The link looks like this `https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=PERMISSION&scope=bot`. We need to find the client id and also set permission. We can use the permission from the bot you found or also check in developer portal for permission.
For the client id, you can copy the bot id when right clicking on the bot in the server(if you enabled developer mode). Another way is to use the carl bot:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/52c07c8f-6c1d-4e30-a289-410970309668)


So now we can fill in the url and invite the bot to our server.
In our server we can add the beta role and talk with the bot.

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/70d7406b-1127-42c8-b331-89960c7a54ca)


So we are talking with an AI. We can use [prompt injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/Archive/0_1_vulns/Prompt_Injection.html) to get the flag here. 
There are different ways to solve it. I used this payload to get the flag(after some tries it gives the flag):

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/cc377ef1-a1c1-4408-a728-e888bfc2257a)


