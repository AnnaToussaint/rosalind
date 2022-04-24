#!/usr/bin/env python3
str = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'

d = {}
# Split input into list of strings
split_input = str.split(' ')
# Iterate over the list
for word in split_input:
    # If word already in dict increment its counter
    if word in d:
        d[word] += 1
    # Else it's the first time we have
    # seen it to set it's counter to 1
    else:
        d[word] = 1

# Finally print the counts of each word
for k,v in d.items():
    print(k,v)
