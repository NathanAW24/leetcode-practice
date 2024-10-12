# SOME CODING QUESTION

# Message parsing
Consider the transmission of messages over a network. The message is transferred character by character, each character having some index number.

Because of transmission delays, the characters along with their index numbers might not be reached in order to the receiver. You are given a list of pairs of index numbers and characters reached by the receiver. A valid message from index /to r is defined as follows:
• It is non-empty
• It is enclosed within two '* characters. i.e., at index 1-1 and index r+1, 1*1 character is available.
• Eg. "*hello*", here "hello" is a valid message. "*_hello*" is not a valid message, '_'denotes empty space.

You have to process the incoming characters and place the character at its index_number. As soon as some sequence of index turns into a valid message print the message.

# Note: 
It is possible that simultaneously two valid messages appear after putting some character at its index. In such cases, print the messages in the increasing order of their index number. It is also possible that some characters do not make any valid sequence.
Process the list in order and print the messages as soon as it becomes valid.

# Function description
Complete the function solve(). This function takes 2 parameters and returns an array of strings:
• N: Represents the length of Messages array
• Messages: Represents a 2D string array having N pair of index_number and character (both as strings)

# Input format for custom testing
# Note: 
Use this input format if you are testing against custom input or writing code in a language where we don't provide boilerplate code.
• The first line contains a single integer N.
• Next, N lines contain two space-separated strings, each denoting index_number and a character for that index.

# Output format
Print each valid message on a new line.

# Constraints
3 ≤ N ≤ 106
1 ≤ index_number ≤ 1018
Character at any index is either * or lowercase english letters
There exists atleast one valid message

# Sample

Input
```
6
693232583 *
1 *
2 a
693232585 *
3 *
693232584 W
```

Output
```
a
w
```

Boilerplate
```python
def solve (N, Messages)
    # Write your code here
    return [1,1]
    pass
N = int(input())
Messages = [input().split() for i in range(N)]
out_ = solve(N, Messages)
for i_out_ in out_: 
    print(i_out_)
```

Explanation
Given
- N= 6
- Messages = ["693232583, *1, '1, *1, "2, a", "693232585, *1, "3, *", "693232584, w"]

Approach
- Messages[0] puts '*' at index 693232583.
- Messages[1] puts '*' at index 1.
- Messages[2] puts 'a' at index 2.
- Messages[3] puts '*' at index 693232585.
- Messages[4] puts '*' at index 3. This makes the sequence from index_number 2 to 2 a valid message as it is enclosed within the character '* So, you output "a".
- Messages[5] puts character 'w' at index 693232584. This makes the sequence from index_number 693232584 to 693232584 a valid message as it is enclosed within the character '*'! So, you output 'w'.
- Final output = ["a", "w"].


Please do it in python