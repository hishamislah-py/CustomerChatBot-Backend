# 4 Converting Hexadecimal Values to Bit Values

The Visa/Mastercard profile information may contain values in hexadecimal only. However, the table below may refer to particular bytes and bits.

To convert **8C01F21C1693** to bytes and bits, do the following:

1. Each byte is 2 hexadecimal digits.  therefore, â8Câ is the first byte, and â01â the second byte.
2. Each byte of 2 hexadecimal digits can be converted to 8 binary bits as follows:

   1. First hexadecimal digit = bits 8 to 5 of this byte
   2. Second hexadecimal digit = bits 4 to 1 of this byte
   3. Convert hexadecimal digits to 4 bits as follows:

      | Hexadecimal character | Binary bits equivalent | Decimal value |
      | --- | --- | --- |
      | 0 | 0000 | 0 |
      | 1 | 0001 | 1 |
      | 2 | 0010 | 2 |
      | 3 | 0011 | 3 |
      | 4 | 0100 | 4 |
      | 5 | 0101 | 5 |
      | 6 | 0110 | 6 |
      | 7 | 0111 | 7 |
      | 8 | 1000 | 8 |
      | 9 | 1001 | 9 |
      | A | 1010 | 10 |
      | B | 1011 | 11 |
      | C | 1100 | 12 |
      | D | 1101 | 13 |
      | E | 1110 | 14 |
      | F | 1111 | 15 |
   4. For example, â8Câ is in binary *b*10001100
   5. Therefore â8Câ is: bit8=1, bit7=0, bit6=0, bit5=0, bit4=1, bit3=1, bit2=0, bit1=0

3. For the example **8C01F21C1693**:

   | Byte | Hex value | Binary (bit8 (leftmost) to bit1 (rightmost) |
   | --- | --- | --- |
   | 1 | 8C | 10001100 |
   | 2 | 01 | 00000001 |
   | 3 | F2 | 11110010 |
   | 4 | 1C | 00011100 |
   | 5 | 16 | 00010110 |
   | 6 | 93 | 10010011 |

   For example: Byte 3 bit 8 =1, and Byte 5 bit1=0