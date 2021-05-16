# A program that takes a str "X-DSPAM-Confidence : 0.8475"
# and slices returning the last string from ":"  as a float.
string = "X- DSPAM-Confidence : 0.8475"
colon = string.find(":")
digit = string[colon + 1:]
digit = float(digit)
print(digit)