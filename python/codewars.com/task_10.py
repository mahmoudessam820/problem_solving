'''
    Simple Encryption #1 - Alternating Split

    - Implement a pseudo-encryption algorithm which given a string S and an integer N
    - concatenates all the odd-indexed characters of S with all the even-indexed characters of S
    - this process should be repeated N times.

    Examples:

    encrypt("012345", 1)  =>  "135024"
    encrypt("012345", 2)  =>  "135024"  ->  "304152"
    encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

    Together with the encryption function, you should also implement a decryption function which reverses the process.
    If the string S is an empty value or the integer N is not positive, return the first argument without changes.

    Task URL: https://www.codewars.com/kata/simple-encryption-number-1-alternating-split

'''


# def encrypt(text, n):
#     if not text:
#         return text
#     elif n < 0:
#         return text
#     else:
#         odd_index = ''
#         even_index = ''
#         count = 0
#         result = []
#         while True:
#             for i in range(0, len(text)):
#                 if i % 2:
#                     odd_index += text[i]
#                 else:
#                     even_index += text[i]
#             count += 1
#             if count <= n:
#                 result.append(odd_index + even_index)
#                 odd_index = ''
#                 even_index = ''
#             if count == n:
#                 break
#         return result


# print(encrypt('encrypt', 3))


def decrypt(encrypted_text: str, n: int):
    if not encrypted_text:
        return encrypted_text
    elif n < 0:
        return encrypted_text
    else:
        edcrypt_text = ''
        count = 0
        result = []

        for i in range(0, len(encrypted_text)):
            if i % 2:
                edcrypt_text += encrypted_text[i]
            else:
                edcrypt_text += encrypted_text[i]

    return edcrypt_text


print(decrypt('nrpecyt', 1))



def encrypt(text, n):
    pass