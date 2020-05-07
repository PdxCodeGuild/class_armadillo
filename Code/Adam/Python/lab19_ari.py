"""
Lab 19: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) 
is a formula for computing the U.S. grade level for a given block of text. The general formula to compute 
the ARI is as follows:

4.71(character/words) + 0.5 (words/sentences) - 21.43

The score is computed by: 
multiplying the number of characters 
divided by the number of words by 4.71, 
adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result 
is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade 
level as scores of 14.

PEMDAS
#parenthesis first - / the number of characters


"""