import evaluate

# Let's make our own dataset which is a combination of HumanEval as well as the other execution based benchmarks

# Let's use just one LLM (the one used by ChatGPT)

# THe prompts are in my email Jan 5th

correct_responses = [["""
words = []
splitted_word = ""
for char in s:
if char == " ":
if splitted_word != "":
words.append(splitted_word)
splitted_word = ""
elif char != ",":
splitted_word += char
if splitted_word != "":
words.append(splitted_word)
return words
"""], 

["""
if n < 2: return False
if n == 2: return True
if n%2 == 0: return False
return not any(n%k == 0 for k in range(3,int(n
**0.5)+1,2))
""", """
prime = True
if n == 1:
return False
for i in range(2, n):
if n % i == 0:
prime = False
return prime
""", """
if n == 2 or n == 3:
return True
if n < 2 or n % 2 == 0:
return False
if n < 9:
return True
if n % 3 == 0:
return False
r = int(n**0.5)
f = 5
while f <= r:
if n % f == 0:
return False
if n % (f+2) == 0:
return False
f += 6
return True
"""], 

["""
if k <= len(arr):
sum = 0
for i in range(k):
if len(str(arr[i])) <= 2:
sum += arr[i]
return sum
else:
return "Number of elements are less than k"
"""], 

["""
even_count = 0
odd_count = 0
for i in range(1, n+1):
if str(i) == str(i)[::-1]:
if i % 2 == 0:
even_count += 1
else:
odd_count += 1
return (even_count, odd_count)
""", """
even_pal = 0
odd_pal = 0
for x in range(1, n + 1):
if str(x) == str(x)[::-1]:
if x % 2 == 0:
even_pal += 1
else:
odd_pal += 1
return even_pal, odd_pal
""", """
even, odd = 0, 0
for i in range(1, n+1):
if str(i) == str(i)[::-1]:
if int(str(i)[::-1]) % 2 == 0:
even += 1
else:
odd += 1
return even, odd
"""], 

["""
return max(strings, key=len) if strings else None
""", """
lengths = [len(string) for string in strings]
if len(lengths) == 0:
return None
max_length = max(lengths)
max_indices = [i for i, v in enumerate(lengths) if
v == max_length]
if len(max_indices) == 1:
return strings[max_indices[0]]
else:
return strings[max_indices[0]]
""", """
if not strings:
return None
return max(strings, key=len)
"""], 

]

code_generated_responses = ["""
import re
def words_string(s):
    words = re.split(r'[,\s]+', s)
    
    words = [word for word in words if word]
    
    return words
""", 

"""
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
""", 

"""
def add_elements(arr, k):
    selected_elements = [x for x in arr[:k] if 0 < x < 100]
    
    result_sum = sum(selected_elements)
    
    return result_sum
""", 

"""
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
""", 

"""
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = max(strings, key=len)
    
    return longest_str
"""
]


"""
Metrics which are available in Hugging Face evaluate library and have also been mentioned in my literature research:
BLEU
METEOR
chrF
ROUGE
BERT Score
Exact Match
"""


bleu = evaluate.load("bleu")
meteor = evaluate.load("meteor")
chrf = evaluate.load("chrf")
rouge = evaluate.load("rouge")
exact_match = evaluate.load("exact_match")



bleu_results = bleu.compute(predictions=code_generated_responses, references=correct_responses)
print(bleu_results)

meteor_results = meteor.compute(predictions=code_generated_responses, references=correct_responses)
print(meteor_results)

# Because chrf requires the same number of references for each prediction
chrf_correct_responses = [response[0] for response in correct_responses]

chrf_results = chrf.compute(predictions=code_generated_responses, references=chrf_correct_responses)
print(chrf_results)

rouge_results = rouge.compute(predictions=code_generated_responses, references=correct_responses)
print(rouge_results)





# All code generated responses that I am using are functionally correct