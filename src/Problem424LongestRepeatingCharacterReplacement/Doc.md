# Thought Process
## First case, `"ABAB", k=2`
Don't forget to keep track of the longest_string

ABAB
^^
lr
hash = {A: 1, B: 1}, k_used = 1
max hash --> A or B same, the rest change to max hash

ABAB
^ ^
l r
hash = {A: 2, B: 1}, k_used = 1 + 0 = 1
max hash --> A, the rest change to max hash

ABAB
^  ^
l  r
hash = {A: 2, B: 2}, k_used = 1 + 1 = 2 >= 2
max hash --> A, the rest change to max hash
since k_used >= 2 --> move l --> revert k_used = 0

ABAB
 ^ ^
 l r
hash = {A: 1, B: 2}, k_used = 0 + 1 = 1
max hash --> B, the rest change to max hash

move r, but cannot so move l --> revert k_used = 0 (?)
ABAB
  ^^
  lr
hash = {A: 1, B: 1}, k_used = 1 + 0 = 1
max hash --> A or B same, the rest change to max hash

Return maximum string

BIG QUESTION: When do we move the `l` pointer? Do we need to move `r` left?

## Second case, `"AABABBA", k=1`

AABABBA
^^
lr
hash = {A:2}, k_used = 0
max hash --> A, no changes needed
max_length = 2

AABABBA
^ ^
l r
hash = {A:2, B:1}, k_used = 0 + 1 = 1 --> cara hitungnya bukan gini, tapi pake `total(hash) - hash[max_val]`
max hash --> A, change the rest to A
max_length = 3

AABABBA
^  ^
l  r
hash = {A:3, B:1}, k_used = 1 + 0 = 1
max hash --> A, change the rest to A
max length = 4

AABABBA
^   ^
l   r
hash = {A:3, B:2}, k_used = 1 + 1 = 2 > k --> need to change 2 B's to A's
max hash --> A, change the rest to A
move left

AABABBA
 ^  ^
 l  r
hash = {A:2, B:2}, k_used = 2 > k --> need to change 2 B's to A's
max hash --> A or B same, change the rest
move left

AABABBA
  ^ ^
  l r
hash = {A:1, B:2}, k_used = 1 == k --> need to change 1 A to B.
max hash --> B, change the rest
move right again

AABABBA
  ^  ^
  l  r
hash = {A:1, B:2}, k_used = 1 == k --> need to change 1 A to B.
max hash --> B, change the rest
move right again

AABABBA
  ^   ^
  l   r
hash = {A:2, B:3}, k_used = 2 > k --> need to change 2 A's to B's
max hash --> 
