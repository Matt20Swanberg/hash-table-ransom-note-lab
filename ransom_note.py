"""
Ransom Note Construction Using Hash Tables

This module determines whether a ransom note can be constructed
using the characters available in a magazine.

A dictionary (hash table) tracks character frequencies, allowing
efficient lookups and ensuring each character is used only once.
"""

def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determine whether a ransom note can be constructed from a magazine.

    Args:
        ransomNote (str): The string containing the required characters.
        magazine (str): The string containing the available characters.

    Returns:
        bool: True if the ransom note can be constructed, False otherwise.

    Time Complexity:
        O(m + n), where m is the length of magazine and n is the
        length of ransomNote. Each string is traversed at most once.

    Space Complexity:
        O(k), where k is the number of unique characters in magazine.
        The dictionary stores one entry per unique character.
    """

    # Initialize a dictionary to track available character frequencies
    letter_counts = {}

    # Count each character in the magazine
    for char in magazine:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    # Check whether each required character is available
    for char in ransomNote:
        # Return False if the character is missing or exhausted
        if char not in letter_counts or letter_counts[char] == 0:
            return False

        # Consume one occurrence of the character
        letter_counts[char] -= 1

    # All required characters were available
    return True
