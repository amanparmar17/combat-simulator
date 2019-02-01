# Combat-Simulator

## What is a combat simulator?
A combat simulator is a platform where you pitch one army against other, and after various rounds, judged by certain criterions and rules, a winner emerges.

This project mainly focuses on the development of basic as well as advance combat simulator, using the power of **_Python_**.

At the start of the game, commander of each of the 2 armies, is given a **starting total of $10**. Units are purchased
and stored in their army. The commanders may spend as much or as little of their money as they desire. After the armies are assembled, the **units are then made to fight each other in the order they were purchased in**. Each unit in the **standard game costs $1**.


## Basic combat simulator

#### file name:

There are **three** types of units available, in the basic simulator:
* Archer
* Soldier 
* Knight

Each unit has a **weakness** and a **strength**.
Table below indicates who wins in any encounter.

| Type of Unit | Archer | Soldier | Knight | 
| ------------ |------- | ------- | ------ |
| Archer | Tie | Archer | Knight |
| Soldier | Archer | Tie | Soldier |
| Knight | Knight | Soldier | Tie |

After each fight, the winner is left on the battlefield to fight the next combatant. If both units
lose, then two new units are taken from the army and begin their fight.
