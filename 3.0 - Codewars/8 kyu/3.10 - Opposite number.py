#Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

""" def opposite(number):
  # your solution here """


"""     test.assert_equals(opposite(1),-1)
        test.assert_equals(opposite(25.6), -25.6)
        test.assert_equals(opposite(0), 0)
        test.assert_equals(opposite(1425.2222), -1425.2222)
        test.assert_equals(opposite(-3.1458), 3.1458)
        test.assert_equals(opposite(-95858588225),95858588225) """


def opposite(number):
  return number * -1
  #return -number         so it looks good but it's actually a bit slower, hmm

""" #fastest solution returned 94ms with parens around multiplication 87ms without for results
    return number - number * 2 

#middle solution returned 109ms time period for result
#    return number * -1
#slowest solution returned 150ms time period for result
#    return -number """


print(opposite(-1))
print(opposite(99999))
print(opposite(0))
