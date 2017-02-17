SWIM
====

Scalable Weakly-consistent Infection style Process Group Membership Protocol

Abstract
--------

* Several distributed peer-to-peer applications require weakly-consistent knowledge of process group membership information at all participating processes.

* SWIM effort is motivated by the un-scalability of the traditional heart-beating protocols, which either impose network loads that grow quadratically with frequency w.r.t detecting process crashes.

* Design, Implementation and performance of SWIM sub-system on a large cluster of commodity PCs.

* Unlike traditional heart beating protocols, SWIM separates the failure detection and the membership update dissemination functionality of the membership protocol.

* Information about membership changes, such as process joins, drop outs and failures, is propagated via piggybacking on ping messages and acknowledgements.

* This results in fast infection style (also epidemic or gossip style) of dissemination.

* The rate of false failure detection in SWIM system is reduced by modifying the protocol to allow group members to suspect a process before declaring it as failed - this allows the system to discover and rectify false failure detections.

* Protocol guarantees deterministic time bound to detect failures.


1. Introduction
---------------

* Large scale peer-to-peer distributed process groups running over the Internet rely on a distributed membership maintenance sub-system.

* Examples of existing middleware systems that utilize a membership protocol include reliable multicast [3, 11], and epidemic-style  membership dissemination [4, 8, 13].

* These protocols in turn find use in applications such as distributed databases that need to reconcile recent disconnected updates [14].

* Publish-Subscribe systems and large scale peer to peer systems.

* The performance of emerging applications such as large-scale cooperative gaming, and other collaborative distributed applications, depends critically on the reliability and scalability of the membership maintenance protocol used within.

* Briefly, a membership protocol provides each process ("member") of the group with a locally-maintained list of other non-faulty processes of the group.

* Gossip based dissemination protocols would use the list to periodically pick target members for gossip.

* Virtually synchronous multi-cast protocols.

* Implement a membership sub-system that provides stable failure detection time, stable rate of false positives and low message load per group member, thus allowing distributed applications that use it to scale well.

* Sequencer process that checkpoints the membership list periodically.

* However, unlike the weakly consistent problem, strongly consistent specifications might have fundamental scalability limitations.

* heart-beating.

* SWIM imposes constant message load per group member.

* detects process failure in an expected constant time at some non-faulty process in the group.

* provides deterministic bound on the local time that a non-faulty proess takes to detect failure on another process.

* provides a


---

SWIM, a scalable weakly- consistent process group membership protocol. The SWIM project is motivated by the unscalability of heartbeat-based protocols, which are popular with distributed system de- signers today.





---
http://www.cs.cornell.edu/gupta/swim

https://www.cs.cornell.edu/~asdas/research/dsn02-swim.pdf



