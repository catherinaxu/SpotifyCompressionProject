def compress(lyrics_string):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in lyrics_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result


def main():
    # lyrics = "[Intro] Nobody pray for me It's been that day for me Way (Yeah, yeah!) [Verse 1] Ayy, I remember syrup sandwiches and crime allowances Finesse a nigga with some counterfeits, but now I'm countin' this Parmesan where my accountant lives, in fact I'm downin' this D'USSÉ with my boo bae tastes like Kool-Aid for the analysts Girl, I can buy yo' ass the world with my paystub Ooh, that pussy good, won't you sit it on my taste bloods? I get way too petty once you let me do the extras Pull up on your block, then break it down: we playin' Tetris A.M. to the P.M., P.M. to the A.M., funk Piss out your per diem, you just gotta hate 'em, funk If I quit your BM, I still ride Mercedes, funk If I quit this season, I still be the greatest, funk My left stroke just went viral Right stroke put lil' baby in a spiral Soprano C, we like to keep it on a high note It's levels to it, you and I know [Chorus] Bitch, be humble (Hol' up, bitch) Sit down (Hol' up, lil', hol' up, lil' bitch) Be humble (Hol' up, bitch) Sit down (Hol' up, sit down, lil', sit down, lil' bitch) Be humble (Hol' up, hol' up) Bitch, sit down (Hol' up, hol' up, lil' bitch) Be humble (Lil' bitch, hol' up, bitch) Sit down (Hol' up, hol' up, hol' up, hol' up) Be humble (Hol' up, hol' up) Sit down (Hol' up, hol' up, lil', hol' up, lil' bitch) Be humble (Hol' up, bitch) Sit down (Hol' up, sit down, lil', sit down, lil' bitch) Be humble (Hol' up, hol' up) Bitch, sit down (Hol' up, hol' up, lil' bitch) Be humble (Lil' bitch, hol' up, bitch) Sit down (Hol' up, hol' up, hol' up, hol' up) [Verse 2] Who dat nigga thinkin' that he frontin' on Man-Man? (Man-Man) Get the fuck off my stage, I'm the Sandman (Sandman) Get the fuck off my dick, that ain't right I make a play fucking up your whole life I'm so fuckin' sick and tired of the Photoshop Show me somethin' natural like afro on Richard Pryor Show me somethin' natural like ass with some stretch marks Still will take you down right on your mama's couch in Polo socks Ayy, this shit way too crazy, ayy, you do not amaze me, ayy I blew cool from AC, ayy, Obama just paged me, ayy I don't fabricate it, ayy, most of y'all be fakin', ayy I stay modest 'bout it, ayy, she elaborate it, ayy This that Grey Poupon, that Evian, that TED Talk, ayy Watch my soul speak, you let the meds talk, ayy If I kill a nigga, it won't be the alcohol, ayy I'm the realest nigga after all [Chorus] Bitch, be humble (Hol' up, bitch) Sit down (Hol' up, lil', hol' up, lil' bitch) Be humble (Hol' up, bitch) Sit down (Hol' up, sit down, lil', sit down, lil' bitch) Be humble (Hol' up, hol' up) Bitch, sit down (Hol' up, hol' up, lil' bitch) Be humble (Lil' bitch, hol' up, bitch) Sit down (Hol' up, hol' up, hol' up, hol' up) Be humble (Hol' up, hol' up) Sit down (Hol' up, hol' up, lil', hol' up, lil' bitch) Be humble (Hol' up, bitch) Sit down (Hol' up, sit down, lil', sit down, lil' bitch) Be humble (Hol' up, hol' up) Bitch, sit down (Hol' up, hol' up, lil' bitch) Be humble (Lil' bitch, hol' up, bitch) Sit down (Hol' up, hol' up, hol' up, hol' up)"
    lyrics = "Now watch me whip (kill it!) Now watch me nae nae (okay!) Now watch me whip whip Watch me nae nae (want me do it?) Now watch me whip (kill it!) Watch me nae nae (okay!) Now watch me whip whip Watch me nae nae (can you do it?) Now watch me Ooh watch me, watch me Ooh watch me, watch me Ooh watch me, watch me Ooh ooh ooh ooh Ooh watch me, watch me Ooh watch me, watch me Ooh watch me, watch me Ooh ooh ooh ooh Do the stanky leg, do the stanky leg Do the stanky leg, do the stanky leg Do the stanky leg, do the stanky leg Do the stanky leg, do the stanky leg Now break your legs Break your legs Tell 'em break your legs Break your legs Now break your legs Break your legs Now break your legs Break your legs Now watch me (bop bop bop bop bop bop bop bop) Now watch me (bop bop bop bop bop bop bop bop) Now watch me whip (kill it!) Now watch me nae nae (okay!) Now watch me whip whip Watch me nae nae (want me do it?) Now watch me whip (kill it!) Watch me nae nae (okay!) Now watch me whip whip Watch me nae nae (can you do it?) Now watch me Ooh watch me, watch me Ooh watch me, watch me Ooh watch me, watch me Ooh ooh ooh ooh Ooh watch me, watch me Ooh watch me, watch me Ooh watch me, watch me Ooh ooh ooh ooh Now watch me you Now watch superman Now watch me you Now watch superman Now watch me you Now watch superman Now watch me you Now watch superman Now watch me duff, duff, duff, duff, duff, duff, duff, duff (Hold on) Now watch me duff, duff, duff, duff, duff, duff, duff, duff, duff Now watch me (bop bop bop bop bop bop bop bop) Now watch me (bop bop bop bop bop bop bop bop) Now watch me whip (kill it!) Now watch me nae nae (okay!) Now watch me whip whip Watch me nae nae (want me do it?) Now watch me whip (kill it!) Watch me nae nae (okay!) Now watch me whip whip Watch me nae nae (Can you do it?) Now watch me Ooh watch me, watch me Ooh watch me, watch me Ooh watch me, watch me Ooh ooh ooh ooh Ooh watch me, watch me Ooh watch me, watch me Ooh watch me, watch me Ooh ooh ooh ooh".lower()
    compressed = compress(lyrics)
    print('original len={}, compressed_len={}, ratio={}'.format(len(lyrics), len(compressed), len(compressed) / len(lyrics)))


if __name__ == '__main__':
    main()