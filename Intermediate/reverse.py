#Reverse each word of a string

def reverse(s):

    words = s.split(" ")
    new_list = [i[::-1] for i in words]

    r = " ".join(new_list)
    return r

str1 = "Hello, My name is abc"
print(reverse(str1))
