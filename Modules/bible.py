# Deprecated
"""Handles verses of the Bible. (why am I doing this)"""
from random import randint
class Bible:
  def __init__(self):
    self.books = {
      1 : 'Genesis',
      2 : 'Exodus',
      3 : 'Leviticus',
      4 : 'Numbers',
      5 : 'Deuteronomy',
      6 : 'Joshua',
      7 : 'Judges',
      8 : 'Ruth',
      9 : '1 Samuel',
      10 : '2 Samuel',
      11 : '1 Kings',
      12 : '2 Kings',
      13 : '1 Chronicles',
      14 : '2 Chronicles',
      15 : 'Ezra',
      16 : 'Nehemiah',
      17 : 'Esther',
      18 : 'Job',
      19 : 'Psalms',
      20 : 'Proverbs',
      21 : 'Ecclesiastes',
      22 : 'Song of Solomon',
      23 : 'Isaiah',
      24 : 'Jeremiah',
      25 : 'Lamentations',
      26 : 'Ezekiel',
      27 : 'Daniel',
      28 : 'Hosea',
      29 : 'Joel',
      30 : 'Amos',
      31 : 'Obadiah',
      32 : 'Jonah',
      33 : 'Micah',
      34 : 'Nahum',
      35 : 'Habakkuk',
      36 : 'Zephaniah',
      37 : 'Haggai',
      38 : 'Zechariah',
      39 : 'Malachi',
      40 : 'Matthew',
      41 : 'Mark',
      42 : 'Luke',
      43 : 'John',
      44 : 'Acts',
      45 : 'Romans',
      46 : '1 Corinthians',
      47 : '2 Corinthians',
      48 : 'Galatians',
      49 : 'Ephesians',
      50 : 'Philippians',
      51 : 'Colossians',
      52 : '1 Thessalonians',
      53 : '2 Thessalonians',
      54 : '1 Timothy',
      55 : '2 Timothy',
      56 : 'Titus',
      57 : 'Philemon',
      58 : 'Hebrews',
      59 : 'James',
      60 : '1 Peter',
      61 : '2 Peter',
      62 : '1 John',
      63 : '2 John',
      64 : '3 John',
      65 : 'Jude',
      66 : 'Revelation'
    }
    
  def bible_random(self):
    """gets a random bible verse from t_kjv.csv"""
    with open("Modules/Text_Files/t_kjv.csv", "r") as file:
      lines = file.readlines()
      amount = len(lines)
      result = lines[(randint(1,amount))]
      result = result.split(",")
      # ignore index 0. use the books dictionary for the string
      print(result)
      book = self.books.get(int(result[1]))
      verse = f"{book} {result[2]}:{result[3]} "
      verse += ','.join(result[4:])
      return verse
      
        