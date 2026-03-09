# Encryption – LFSR Encryption
This project was implemented for the course Encryption Theory.
The idea of the project is to implement a Stream Cipher using LFSR (Linear Feedback Shift Register) and then improve it using a nonlinear method (NLFSR) to increase security.

## Project Description
In this project, a keystream is generated using LFSR based on a random seed.  
The keystream is then used to encrypt the plaintext using the XOR operation.  
During decryption, the same seed is extracted and used again to generate the same keystream in order to recover the original message.

## Files
EmbeddingProcess.py: Contains the encryption process.
ExtractionProcess.py: Contains the decryption process.
interface.py: Simple interface to run the program.

## Baseline Version
The baseline system uses a simple LFSR to generate the keystream.  
The feedback function used is:
b6 = b6 XOR b1
This method is simple and fast but can be vulnerable if the keystream or seed is reused.

## Enhancement
To improve security, a nonlinear modification was added to the keystream generation process.  
Nonlinear operations such as AND, OR, and XOR were used to make the output less predictable.

## Notes
One important limitation in stream cipher systems is reusing the same seed.  
If the same keystream is used more than once, it may allow attackers to analyze the relationship between encrypted messages.
