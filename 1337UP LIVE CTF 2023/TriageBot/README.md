# TriageBot

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2023](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2134)  |
|  **Author** |  0xM4hm0ud & CryptoCat |
|  **Category** |  Warmup |
|  **Solves** |  27  |
|  **Difficulty** |  Easy |

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/b393ed7d-f896-49fd-811c-52d676190ef0)

# Solution

The description talks about an new bot and also about an `beta` for full functionality.
Lets go to the discord server and talk with the bot.

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/abe315b1-7560-4ea7-bf2b-c1cf5469903e)

We have an few options we can send.
Those 3 arent helpful and is just sending the same message every time we call the option:

```
!anyupdate - Check for updates
!support - Ask for support
!bountyplz - Get a bounty
```

When we try the option `!triage` it responds with this:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/e03e04f1-81d5-4363-9cb4-fb792afdf8d5)

So we are not a beta tester. In the description it talks about a beta role. The bot is inside the Intigriti server and we can't assign a role ourselves. So we need to invite the bot to our own server.
For this we need an invite link. We need to generate the link. We can do it 2 ways. Search online for a random bot and copy the link or enable developer mode and go to the portal where you can generate links aswell(after creating a bot).
The link looks like this `https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=PERMISSION&scope=bot`. We need to find the client id and also set permission. We can use the permission from the bot you found or also check in developer portal for permission.
For the client id, you can copy the bot id when right clicking on the bot in the server(if you enabled developer mode). Another way is to use the carl bot:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/74a3a907-0afc-436b-ac34-c62e47c15e7b)

So now we can fill in the url and invite the bot to our server.
In our server we can add the beta role and talk with the bot.

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/efc31db0-e446-4e06-a3b8-c36a4024c1b1)

So we are talking with an AI. We can use [prompt injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/Archive/0_1_vulns/Prompt_Injection.html) to get the flag here. 
There are different ways to solve it. I used this payload to get the flag(after some tries it gives the flag):

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/6e25a4cc-ac55-4f24-9be8-d6d8c9c41978)

