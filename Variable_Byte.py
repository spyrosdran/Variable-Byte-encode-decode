"""
    If the binary number has less than 7 bits,
    then we add the right amount of zeros
    and return the VB.

    If we have more than 7 bits, then we add zeros at the end,
    so that the number of bits is a multiple of 7. Then we keep
    adding the bits to the VB. Due to the fact that the binary
    number is reversed, the first byte is going to be the last
    byte in the returned value and thus we add "1", so as to
    define that this is going to be the last byte. In every
    other case we add a zero after adding 7 bits to the VB. At
    last, we return the VB reversed, so that the user can read it
    again normally
"""


def vb_encode(num):
    num = int(num)
    # Turn the number into a binary, remove the 0b from the front and cast to string
    binary = str(bin(num)[2:])

    # Reversing the string, so that we can later add zeros at the end
    binary = binary[::-1]

    # Initializing the number of bits and the returned string containing the VB
    number_of_bits = len(binary)
    vb = ""

    if number_of_bits <= 7:
        # Defining the number of zeros we have to add
        number_of_zeros = 7 - number_of_bits
        zeros = ""

        for i in range(0, number_of_zeros):
            zeros += "0"

        vb = binary + zeros + "1"

    else:
        # Adding the right amount of zeros, so that the number of bits is a multiple of 7
        while number_of_bits % 7 != 0:
            binary += "0"
            number_of_bits += 1

        # We keep a counter, so that we know whenever we have to add to the VB "0" or "1"
        counter = 1
        for bit in binary:
            vb += bit
            if counter % 7 == 0:
                if counter == 7:
                    vb += "1"
                else:
                    vb += "0"
            counter += 1

    # Reverse the reversed binary sequence and return it
    return vb[::-1]


def vb_decode(vb):
    #Valid input check
    if len(vb) % 8 != 0:
        return "The parameter is not encoded in variable byte format"
    for bit in vb:
        if str(bit) != "1" and str(bit) != "0":
            return "The parameter is not encoded in variable byte format"

    string = ""

    # Removing every continuation bit from the sequence
    counter = 0
    for bit in vb:
        if counter % 8 == 0:
            counter += 1
            continue
        string += bit
        counter += 1

    # Casting the bit array to an integer. Every bit is exponentiated in base 2
    number = int(string, 2)

    return number


# Running the main program
if __name__ == "__main__":

    print("Please enter a non negative integer: ")
    num = input()

    # Valid input check
    while not num.isdigit():
        print("Please try again. Enter a non negative integer:")
        num = input()

    print("Encoding number: " + num)
    vb = vb_encode(num)
    print("Encoded number: " + vb)

    print("--------------")

    print("Decoding number: " + vb)
    num = vb_decode(vb)
    print("Number retrieved after decoding: " + str(num))
