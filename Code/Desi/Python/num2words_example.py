num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

def num2words():
    try:
      print num2words():
      except KeyError:
        try:
          print num2words[n-n%10] + num2words[n%10].lower()
            except KeyError:
                print 'Number out of range'

>>> n2w(0)
Zero
>>> n2w(13)
Thirteen        
>>> n2w(91)
Ninetyone
>>> n2w(21)
Twentyone
>>> n2w(33)
Thirtythree