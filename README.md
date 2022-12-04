# Natural Language Learning by Bots using Audio Text based limited Dataset for Tulu
## Our project aims to solve the following problems:

1. Creating a basic form of the three-source model.
   This involves a text-based I/O method. Usable audio sources are extremely rare to find for limited data languages. The frontend is simple to use, as the main users      will not be CSE experts but rather experts in the involved language, in this case Tulu. The model uses a modified HMM to update and return sentence structure weights.

2. Forming a database of Tulu words in Kannada script.
   We collect four details about around 500 words and sentences: the word in English, the word in Tulu (in Kannada script), the POS of the word, and the gender of the      word. This is done keeping in mind that Kannada, like most Indian languages, has a fixed per-letter pronunciation. We use SpeechRecognition module's Kannada setting      to recognize Tulu words when in the Translate By Audio section, which recognizes Tulu words even if they are not present in Kannada. 
##To run the program:
1. Install the required dependencies
2. Run frontend.py
