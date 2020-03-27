
def count_common_letters(results):
    letters = {}

    while True:
        word = yield
        word = word.lower()
        for c in word:
            if c.isalpha():
                if c not in letters:
                    letters[c] = 0
                letters[c] += 1

        counted = sorted(letters.items(), key=lambda kv: kv[1])
        counted = counted[::-1]

        results.clear()
        for item, val in counted:
            results[item] = val

names = ['Skimpole', 'Sloppy', 'Wopsle', 'Toodle', 'Squeers',
         'Honeythunder', 'Tulkinghorn', 'Bumble', 'Wegg',
         'Swiveller', 'Sweedlepipe', 'Jellyby', 'Smike', 'Heep',
         'Sowerberry', 'Pumblechook', 'Podsnap', 'Tox', 'Wackles',
         'Scrooge', 'Snodgrass', 'Winkle', 'Pickwick']

results = {}
counter = count_common_letters(results)
counter.send(None)  # prime the coroutine

for name in names:
    counter.send(name)  # send data to the coroutine

counter.close()  # manually end the coroutine

for letter, count in results.iteritems():
    print('{0} apppears {1} times.'.format(letter, count))
