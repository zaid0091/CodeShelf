---
title: DNS Routing & Global Load Balancing
description: Master DNS architecture, Anycast routing, and Global Server Load Balancing (GSLB) to route users to the geographically closest data centers.
order: 9
tags: [architecture, dns, gslb, geo-routing, anycast, latency]
---

# Chapter 9: DNS Routing & Global Load Balancing

> **Deploy global applications, utilize Anycast DNS routing, and configure Global Server Load Balancing to minimize geographical latency.**

---

## Domain Name System (DNS) Basics

DNS is the phonebook of the Internet, translating human-readable domains (like `example.com`) into IP addresses (like `93.184.216.34`). When scaling globally, DNS is the first line of routing.

---

## Anycast Routing

Typically, IP routing is **Unicast**: one IP address points to one physical server. 

**Anycast** allows multiple servers located globally in different data centers to share the exact same IP address. The internet's routing protocol (BGP - Border Gateway Protocol) automatically routes the user's packets to the physically closest server announcing that IP address:

```text
User (US) -> [Anycast IP: 1.1.1.1] -> US Data Center
User (EU) -> [Anycast IP: 1.1.1.1] -> EU Data Center
```
*Anycast is heavily used by CDN providers (Cloudflare, Fastly) and global DNS providers (Cloudflare 1.1.1.1, Google 8.8.8.8) to reduce handshake latency.*

---

## Global Server Load Balancing (GSLB)

GSLB is the practice of distributing traffic across multiple geographically separated data centers. GSLB systems are typically implemented at the DNS level.

### GSLB Routing Strategies

1. **Geo-Location Routing**: Routes users based on their country or state (e.g. US users get US IPs, European users get European IPs). Good for legal compliance (GDPR data residency).
2. **Latency-Based Routing**: Measures round-trip time (RTT) from the user's region to various data centers, returning the IP of the lowest-latency location.
3. **Failover Routing (Active-Passive)**: Returns primary data center IPs. If health checks indicate the primary site is down, it switches DNS records to point to a secondary disaster recovery site.

---

## Best Practices & Pitfalls

| Best Practice | Common Pitfall |
|---------------|----------------|
| Set low TTL (Time To Live) values (e.g., 30–60 seconds) on dynamic failover DNS records so DNS changes propagate quickly during outages. | Setting TTLs too low on static records, which increases DNS resolution lookup overhead for users. |

---

## Interview Points

> **📌 Interview Point 1: Why is DNS-based failover slow compared to load balancer failover?**
> DNS records are heavily cached by intermediate ISPs, operating systems, and browsers. If a data center goes down and you update the DNS IP, some users will continue attempting to connect to the dead IP until their cached DNS entries expire (respecting the TTL).

---

## Exercises

### Exercise 1: Evaluate routing types ⭐
**Task:** If you need to ensure EU customer data is strictly stored and processed inside European Union networks, which GSLB strategy must you configure?

<details>
<summary>✅ Solution (click to reveal)</summary>
**Geo-Location Routing**. This guarantees that traffic originating from EU locations is routed strictly to EU servers.
</details>

---

## Next Chapter

Continue to [Caching Strategies & Eviction](./ch10-caching-strategies.md) to explore memory performance.
