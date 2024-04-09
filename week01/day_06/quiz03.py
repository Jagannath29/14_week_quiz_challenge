# Method, string, translate, maketrans

text = 'good morning'
trans_text = text.maketrans('g', 'f')
print(text.translate(trans_text))


'''
    The output is: food morninf

    tips:
            maketrans() method creates a translation table that can be used with translate() method, 
'''