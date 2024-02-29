# Chapter 1 Q&A

## pip install vs. import
**Q:** I don't really get the concept of the virtual environment. And
the difference between pip install and importing something

**A:**
- `pip` installs packages (these are basically libraries) onto the
  system. There are a lot of packages that don't come with python but
  that are useful to install. `pip` handles installing those packages
  and lets you update them easily. Once you've installed something
  with `pip`, you can use it in your python script with `import`.
- A virtual environment is a way to install specific packages for a
  given project, rather than installing them system-wide. That way,
  you can have one python project that uses e.g. flask version 1.5,
  and another project that uses flask 2.7.

## other ways of sending data across a network

**"Q":** it seems to imply there are many ways of sending data across
a network, which doesn't really confuse me so much as intrigue me.

**"A":** There are! For example, here are the address families defined
on my system. Note that we're only using AF_INET.

```c
/* from /include/sys/socket.h */
#define AF_UNSPEC       0               /* unspecified */
#define AF_UNIX         1               /* local to host (pipes) */
#if !defined(_POSIX_C_SOURCE) || defined(_DARWIN_C_SOURCE)
#define AF_LOCAL        AF_UNIX         /* backward compatibility */
#endif  /* (!_POSIX_C_SOURCE || _DARWIN_C_SOURCE) */
#define AF_INET         2               /* internetwork: UDP, TCP, etc. */
#if !defined(_POSIX_C_SOURCE) || defined(_DARWIN_C_SOURCE)
#define AF_IMPLINK      3               /* arpanet imp addresses */
#define AF_PUP          4               /* pup protocols: e.g. BSP */
#define AF_CHAOS        5               /* mit CHAOS protocols */
#define AF_NS           6               /* XEROX NS protocols */
#define AF_ISO          7               /* ISO protocols */
#define AF_OSI          AF_ISO
#define AF_ECMA         8               /* European computer manufacturers */
#define AF_DATAKIT      9               /* datakit protocols */
#define AF_CCITT        10              /* CCITT protocols, X.25 etc */
#define AF_SNA          11              /* IBM SNA */
#define AF_DECnet       12              /* DECnet */
#define AF_DLI          13              /* DEC Direct data link interface */
#define AF_LAT          14              /* LAT */
#define AF_HYLINK       15              /* NSC Hyperchannel */
#define AF_APPLETALK    16              /* Apple Talk */
#define AF_ROUTE        17              /* Internal Routing Protocol */
#define AF_LINK         18              /* Link layer interface */
#define pseudo_AF_XTP   19              /* eXpress Transfer Protocol (no AF) */
#define AF_COIP         20              /* connection-oriented IP, aka ST II */
#define AF_CNT          21              /* Computer Network Technology */
#define pseudo_AF_RTIP  22              /* Help Identify RTIP packets */
#define AF_IPX          23              /* Novell Internet Protocol */
#define AF_SIP          24              /* Simple Internet Protocol */
#define pseudo_AF_PIP   25              /* Help Identify PIP packets */
#define AF_NDRV         27              /* Network Driver 'raw' access */
#define AF_ISDN         28              /* Integrated Services Digital Network */
#define AF_E164         AF_ISDN         /* CCITT E.164 recommendation */
#define pseudo_AF_KEY   29              /* Internal key-management function */
#endif  /* (!_POSIX_C_SOURCE || _DARWIN_C_SOURCE) */
#define AF_INET6        30              /* IPv6 */
#if !defined(_POSIX_C_SOURCE) || defined(_DARWIN_C_SOURCE)
#define AF_NATM         31              /* native ATM access */
#define AF_SYSTEM       32              /* Kernel event messages */
#define AF_NETBIOS      33              /* NetBIOS */
#define AF_PPP          34              /* PPP communication protocol */
#define pseudo_AF_HDRCMPLT 35           /* Used by BPF to not rewrite headers
	                                 *  in interface output routine */
#define AF_RESERVED_36  36              /* Reserved for internal usage */
#define AF_IEEE80211    37              /* IEEE 802.11 protocol */
#define AF_UTUN         38
#define AF_VSOCK        40              /* VM Sockets */
#define AF_MAX          41
#endif  /* (!_POSIX_C_SOURCE || _DARWIN_C_SOURCE) */
```

I have no idea what almost any of these are, but they are ways to send
data across a network!

## why so few ipv4 addresses?

**Q:** This isn't really a question for you, but why did the people
making ipv4 choose the number of addresses that they did?

**A:** ~I don't have an answer but I'd never thought about this and I
think it's an interesting and worthwhile question. +2 bonus points on
the next assignment to anyone who finds the answer.~

**Bounty Claimed by _Simon Butler_!**

Quote attributed to Vint Cerf explaining the back-of-the-envolope math
they did to arrive at 32 bit IP addresses:

> As we were thinking about the Internet (thinking well, this is going
> to be some arbitrary number of networks all interconnected — we
> don't know how many and we don't know how they'll be connected), but
> national scale networks we thought "well, maybe there'll be two per
> country" (because it was expensive: at this point Ethernet had been
> invented but it wasn't proliferating everywhere, as it did do a few
> years later).

> Then we said "how many countries are there?" (two networks per
> country, how many networks?) and we didn't have Google to ask, so we
> guessed at 128 and that would be 2 times 128 is 256 networks (that's
> 8 bits) and then we said "how many computers will there be on each
> network?" and we said "how about 16 million?" (that's another 24
> bits) so we had a 32-bit address which allowed 4.3 billion
> terminations — which I thought in 1974/3 was enough to do the
> experiment!

https://networkengineering.stackexchange.com/a/7974

## what's up with encoding/decoding

**Q:** [paraphrased] encoding/decoding is kinda weird, huh?

**A:** Yeah. Note this is a python-specific thing, not a general
networking thing -- the thing you send over the network is _bytes_,
and while C strings are just a bunch of bytes, Python strings are not.
C++ strings aren't just a bunch of bytes, either -- they have other
header info. So in C++ to send a `std::string` named `cpp_str` you
would use `cpp_str.c_str()` to get a pointer to the bytes you want to
send.

In summary, the encoding/decoding is a Python artifact, not a
universal law of networking. But it is kind of nice that Python forces
you to think about your string encodings before sending them.
