# NIM Game - The Last One Loses

> This repository is just for education purpose

### Description

You are given an m number of buckets, with each bucket x[i] containing n balls.

You and a computer take alternative turns removing balls from the buckets. In each turn, a player may remove any number of balls from a specific bucket, but only from one bucket (ie: you may remove one or all balls from a bucket, but you can never take balls from 2 different buckets in a single turn). The objective of the game is to force the other player to take the last ball.

Write a Python script that takes an input array x of length m. Each element x[i] contains an integer representing the number of balls in the corresponding bucket. The algorithm should output the index of the bucket and the number of balls that the player should remove to guarantee a win. If no such move exists, the algorithm should return (0, 0). If there are multiple solutions, return the smallest index and the smallest number of balls that should be removed.

### Example 1
Input:
```
[2, 3]
```
Output:
```
(1, 1)
```
By removing 1 ball from the second bucket, the next player is left in a state of [2, 2]. The only options are to remove either 1 ball or 2 balls from either one of the rows. The first player can then remove 2 balls or 1 ball from the remaining row and force the opponent to take the last ball.

### Example 2
Input:
```
[2, 2]
```
Output:
```
(0, 0)
```
Similar to the reasoning above, if you start in the [2, 2] state, you are left with no valid moves that guarantee a win.

### Example 3:
Input:
```
[3, 4, 5, 6]
```
Output:
```
(1, 4)
```
This example has 3 possible solutions: (1, 4), (2, 4), (3, 4). The output should be the smallest value, so remove 4 balls from second bucket (1, 4) is returned.

### Constraints
m, n ∈ [1, 1000000]
