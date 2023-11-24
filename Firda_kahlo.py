from email.mime import audio


paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']
dates = [1939, 1933, 1946, 1940]

paintings = list(zip(paintings,dates))

paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer',1946))
paintings.append(('Me and My Doll',1937))

audio_tour_number = []
num = 0
for i in range(len(paintings)):
    num += 1
    audio_tour_number.append(num)

master_list = list(zip(paintings,audio_tour_number))
print(master_list)