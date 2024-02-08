import os
import sys
import hashlib

supported = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]


def encode(func_name: str, content: bytes):
    if func_name in supported:
        return eval(f"hashlib.{func_name}(content).hexdigest()")
    else:
        return "Unsupported..."


def main():
    global given
    compare_mode = False

    code, file_name = sys.argv[1], sys.argv[2]
    if len(sys.argv) == 4:
        given = sys.argv[3]
        compare_mode = True

    content = open(file_name, 'rb').read()
    encode_text = encode(code, content)
    if not compare_mode:
        print(encode_text)
    else:
        print("Verifitcation Passed!" if (encode_text == given) else f"Verification failed...\n{given} : the code you gave\n{encode_text} : the real code to the file")


if __name__ == "__main__":
    main()
    for i in range(5, 0, -1):
        print(f"Close in {i}s...", end='\r')
        time.sleep(1)
