dic = {}
dic[1] = ["Joao", "222-222-2222", "@joaoo"]
dic[2] = ["Maria", "333-333-3333", "@maria"]
dic[3] = ["Mary", "444-444-4444", "@mary"]
dic[4] = ["Vini", "666-666-6666", "@vini"]
dic[5] = ["Aninha", "777-777-7777", "@aninhaaa"]
dic[6] = ["Vitor", "888-888-8888", "@vitor"]
dic[7] = ["Wagner", "999-999-9999", "@wagner"]
dic[8] = ["Regina", "111-111-1111", "@reginhinha"]

for key,value in dic.items():
    print(str(key)+": "+value[0]+", "+value[1]+" ("+value[2]+")")
