def mutate_string(string, position, character):
    string = string[:position]+ character + string[position+1:]
    return string
string = input()
position = int(input())
character = input()
print(mutate_string(string, position, character))
