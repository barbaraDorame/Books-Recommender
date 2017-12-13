import pickle
from gensim import corpora
from itertools import chain

with open('/home/barbara/Documents/NLP/books/library/topics.p',
          'rb') as hindle:
    ldamodel = pickle.load(hindle)
with open('/home/barbara/Documents/NLP/books/library/normlibrary.p',
          'rb') as handle:
    data = pickle.load(handle)
# Topicos
# 0 one, water, two, day, mile, us, river, indian, time, found, country,
# would, feet, upon, island = Expedition/Adventure/Tale

# 1 mr0.009, said0.008, would0.008, one0.007, man0.005, could0.005, time0.004
# much0.004, see0.004, little0.004, know0.004, lady0.004, say0.003, sir0.003
# think0.003, look, never, day, like, well, might, good, us, upon, even, friend
# hand, thought, love, must = Novel/Drama

# 2 mr0.022, said0.019, im0.008, go 0.006, one0.005, look0.005, dont0.005
# time0.004, ad0.004, got0.004, man0.004, like0.004, see0.004, get0.004
# come0.004, say0.004, two0.004, know0.003, back, wot, miss, take, think
# old, eye, content, well, went = Sailor tales

# 3 sir0.021, said0.007, knight0.007, upon0.007, tritram0.007, king0.006
# launcelot0.004, one0.004, lady0.004, great0.004, thou0.004, percive0.003
# footnot, come, thor, would, love, castle, thee, time, day = Cavalry

# 4 return0.010, variant0.006, dick0.006, upon0.004, poem0.004, cruso0.004
# heart0.003, "1836"0.003, edit0.003, joe0.003, marmaduk0.003, "1798"0.003
# wordsworth0.003, thi0.003 = Poems/Oldie

# 5 state0.010, would0.006, may0.006, govern0.005, unit0.005, power0.004
# upon0.004, great0.004, nation0.004, law0.003, time0.003, made0.003
# gener0.003, countri0.003, hous, without, year, people, present, new, could
# act, subject, public, lord, war, shall, interest, everi = Politics

# 6 one0.007, man0.006, life0.005, may0.004, great0.004, like0.004, would0.004
# time0.003, us0.003, work0.003, men0.003, nature0.003, say0.003, good, year
# mani, thing, upon, first, make, much, god, love, world, must, live, mind
# everi = Spiritual/Religion/Poems

# 7 one0.008, said0.007, mr0.005, would0.005, go0.005, man0.005, know0.005
# look0.004, like0.004, time0.004, well0.004, come0.004, little0.004
# could0.004, dont0.004, back, get, say, old, hand, way, thing, make, came
# think, upon, two, ask, good, eye, day, got, made, take, face, turn, boy, want
# seem, went, miss, right, never, first, us, joe, thought, even, away
# = The life of/Biography/Novel

# 8 may0.007, one0.006, use0.006, case0.005, water0.004, form0.004, part0.004
# two0.003, work0.003, inch0.003, foot0.003, large0.003, flower0.003
# body0.003, anim0.003, leav, must, upon, small, surface, place, bone, feet,
# 1, engin, time, also, point, disease, first, plant, air, side, become,
# end, cause, made, well, produce, thu, make, food, experi, effect, wall
# condit, result, pressure, take, vessel = Educational

# 9 shall0.021, lord0.018, unto0.017, thou0.016, god0.013, thi0.013, thee0.011
# said0.009, ye0.008, king0.007, man0.007, upon0.006, say0.006, day0.006
# hath0.006, peopl, israel = Medieval

# 10 &0.025, c0.024, one0.010, adj0.005, v0.005, n0.004, late0.003, take0.003
# make0.003, upon0.003, $0.002, fr0.002, time0.002, go0.002, new0.002, mr
# good, punchinello, play, come, paper, man, give, put, hand, us, like, day,
# set, york = Children books

# 11 german0.013, war0.011, army0.006, french0.005, germany0.005, british0.005
# one0.005, russian0.005, men0.005, offic0.004, would0.004, great0.004
# forc0.004, franc0.004, russia0.004 = WWII

# 12 said0.010, one0.008, would0.007, littl0.006, look0.006, could0.006
# like0.006, go0.005, come0.005, see0.005, know0.004, time0.004, came0.004
# man0.004, back0.004, day, old, hand, well, never, eye, say, face, think, good
# went, thing, thought, get, away, way, seem, mr, long, two, boy, make, must
# upon, take, first, tell, ask, much = Novel/Fiction

# 13 one0.006, great0.005, time0.004, would0.004, roman0.004, king0.003
# upon0.003, place0.003, citi0.003, even0.003, made0.003, church0.003
# peopl0.003, year0.003, men0.003, day, could, two, first, power, order,
# gener, mani, also, without, centuri, enemi, part, war, might
# = Literature/History

# 14 command0.005, men0.005, right0.004, &0.004, guard0.004, offic0.004
# man0.004, may0.004, et0.003, one0.003, fernando0.003, rhetor0.003, "1"0.003
# hym0.003, sergeant0.003, fire, good, left, line, hit = Renaissance/History

lista = [book['Text'] for book in data]
dictionary = corpora.Dictionary(lista)
bow = [dictionary.doc2bow(book) for book in lista]
topics = []
for book in bow:
    a = list(sorted(ldamodel[book], key=lambda x: x[1]))
    topics.append(a[-1][0] + 1)

for book in data:
    topic = topics.pop(0)
    if topic == 1:
        book['Topic'] = 'Expedition/Adventure/Tale'
    elif topic == 2:
        book['Topic'] = 'Novel/Drama'
    elif topic == 3:
        book['Topic'] = 'Sailor tales'
    elif topic == 4:
        book['Topic'] = 'Cavalry'
    elif topic == 5:
        book['Topic'] = 'Poems/Oldie'
    elif topic == 6:
        book['Topic'] = 'Politics'
    elif topic == 7:
        book['Topic'] = 'Spiritual/Religion/Poems'
    elif topic == 8:
        book['Topic'] = 'The life of/Biography/Novel'
    elif topic == 9:
        book['Topic'] = 'Educational'
    elif topic == 10:
        book['Topic'] = 'Medieval'
    elif topic == 11:
        book['Topic'] = 'Children books'
    elif topic == 12:
        book['Topic'] = 'WWII'
    elif topic == 13:
        book['Topic'] = 'Novel/Fiction'
    elif topic == 14:
        book['Topic'] = 'Literature/History'
    else:
        book['Topic'] = 'Renaissance/History'

with open('/home/barbara/Documents/NLP/books/library/feels_topicslibrary.p',
          'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
