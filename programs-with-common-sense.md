---
description: >-
  http://www-formal.stanford.edu/jmc/mcc59.ps ,John McCarthy, Computer Science
  Department Stanford University
---

# Programs with Common Sense

This paper explores the possibility of the machine with common sense like we humans have. So what does that mean? A program/machine have a common sense whenever it can draw conclusion from given premises\(logical propositions\) and also improve it. Here we are talking about representing these premises in formal languages\[Logical languages\]. He gave this machine a simple name: **Advice Taker**

So this Advice taker should perform actions by merely taking instructions\[All formal expressed in logical form\]. This program will have all the consequences of the choice it makes as previous knowledge. So that it learns from the past. Here are the few guidelines he presented for a learning system:

* All behaviors must be representable in the system
* Changes in behavior must be expressible in a simple way
* All aspects of behavior except the most routine must be improvable. In particular, the improving mechanism should be improvable.

Programs are generally told to work by giving imperative instruction as in Turing Machine. Author argues that like human, machines should be able to take action and generate conclusion from a declarative instruction like some form of universal logic truth. It should be able to manipulate these premises to arrive in conclusion.

Let's explore a example in a very simple manner. Say i want to go to Walmart. Here, we have to instruct the Machine "Advice taker" in logical expressions. The rules need to be in predicate logic.  The first thing will be to give it several facts/premises. 

* Am i at home?
* Am i at Walmart?
* Am i travelling?

Similarly we need to provide some rules.

* Is it Far?
* Is it Walkable?
* Is it Driveable?

Now we give it if this then this type statements. 

* If walkable, walk
* If far, drive...

So you get the idea. It's all about logical deductions. You give it series of facts, rules and if then instead of manually providing it directions. Then, the program will calculate the final result. The genius here was we will not be manually programming it to go to Walmart and then again program it to go to Midtown. All these logical facts, rules will take care of that.







