LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(plaintext, key):
    i, m = divmod(len(plaintext), len(key))
    repeated_key = key * i + key[:m]
    ciphertext = ""
    for c, r in zip(plaintext, repeated_key):
        ciphertext += shift_letter(c, LETTERS.index(r))
    return ciphertext


def shift_letter(letter, offset):
    pos = LETTERS.index(letter)
    new_pos = (pos + offset) % len(LETTERS)
    return LETTERS[new_pos]


def analyze_frequency(text):
    freq = {}
    for c in text:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return [
        (k, v / len(text))
        for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)
    ]


def get_keyword(ciphertext, key_len):
    frequencies = [analyze_frequency(ciphertext[i::key_len]) for i in range(key_len)]
    keyword = ""
    for freq in frequencies:
        keyword += shift_letter(freq[0][0], -LETTERS.index("E"))
    return keyword


if __name__ == "__main__":

    encrypted = "NSWXARWJGEXIJCZWUZLOAWFJFTUIMUVFEWHWPEEVVCYENYSGVVECSRZLGFDRZBPKWPMIYTFFGQDRJOKOTWWIWNVKUOBEXOLLZFDCOWZLJCXXQSZFITUIMUVFVLVEJDKZGSVWWYNANZKERERFKRLSOYEUTOWMYLVLVSUJNEHMGBFCEFKZGSVWWYZKCPRYPTYWHFHUQEELWGHSBXISAGWSPRVSVNHFNAJAPEDXWRUAHTHVANKSWHKSNSYSXSKEXIKKYVLGDCRFDSUIBLVUVSGMJTYWKFXWAOWDGHWINSYWOWQKSAPKYFLXENXKVMOIBOIWZOPTHEZKXWVMXLPVKTIINEELHFRQBALDMBHVOLVLVSUFEGISOHUMCRREYCUHBRVIWSQGEEJOQFGPANXLJOQHOEELGBFIHEEYVVFEJBVUCZFYHAKWFTRVOPVUKTLGWUKZQFVEJDLKGRWSLRFNGCUHESGJQJHEQTYGTGKMLOWLGLWWAVVFHCUEQTYGTGZLKSVKVMOIOAIWPCWWKDZNGFJIJTRUEIUEPERNGFDKALVLVSUJNEHMGBFMASTSPCQPUBVYNSDRADSQCBDPUZZFIOOENGVSOCXRPOWJGDUIOEELCHLZATVPVKLXDTYWCJDMHASANWWCKFDGFSURYODHWHLRCAEVECOPACKAQBVSBLRJISWITTTGTDRVWSLUJQDPYUCSVWRROAIWGOVMHYDSFSHBWMGDGGFEJBVVTOZRBRFECJDVEEKQQTVSQRTWUDUIOSIWRCUXENXJGZLKEOLKVSAXOSTAGBWMBITLGLWWWNUYGBHVWLWAEHLSJAEVVVHVAAIWFWIJARVFESVIOPVUKOOPUFFJISQINACXKQWMKNNAVVWLAPFKKHLSJOWZCBGMSIKZJPHGKMZFIARVACFEOCQLARSWTHVDEMZFJWVGHAJKKQLRPRFVWQWSNYTJADWSCRRHJMWITTTGFSVEJDJWEFHXSRZLKBJKEVVKVVHIJGCAUVOIPTVJHFHUQEEUAGHUQEEUGOVIPAFFTWVLZLWUOIJCLWSNMXAUVTYWOCVXYODEQBOIPTVJROLVOAJLJVHEJRVWTWQSJAKFFGWIOEEGHHHIZOILKVLEOTFSPRWLAMFKVQRQIOEVQIEPADCWVHHVOAJDNSHWOOFLVTIVNNEHRQFXDEKGRHZIHVVDGHWINSTGODUMOERTQIWSBTYWVCWEHUJSISWLATFHGWJLPLVLVSUWYODHTWVIWBFMVCIXDEKGVOOYOAXWNSWXARWJGEXIJCPSUOIYJCKAQBRJNAECEOQFAFZLVSGAALCTAGHZARRDTOQOBUEUVWRROWZLJHKIPWFHCFDQATVJECFLKBVLCFDRGFLFEHLSJBVAPUWLABVKVOQSPHVJTOQOBUEUVWRRSIKZPCDHFUJLCPOIBRVWROUEIEKWTOOWKFZLUHKIHEKLGFIVAQLWPQBHESKJKPXXEOEJGOVSJASDAKHPHTYWUOPIBUEUVWRRDAJTGSQYOEULQTLXPHVSOWQSWCZVHFHUQEEUAWQTNOKWKBVIMUVFESVEOPPMUWQKPHVNKQFMLHVJQFVSIEFLJSUGEPYWTPDWADFFCGWVWDUDKBJGDETCGFESWRULADLGWLCQWGHWWMEWOCQMYSLUJOVEOIELQSUVZRFHRWQKPHVKGQRRZRKGTSPIIBVJVVHXKPVAIVWGDAISEHHVOTYWWGHSBLVLVSUJNEHMGBFMASRFFTUIMUVFEMDRWLPKKGSPWYJSHIQHWMVFVOOVKLVAPQUCLTFYTOPWWNUKGJHVWLNGTRSYVZCWIOPIOIEUNIGMJGYSPUPEJSTJCPEPAAEVVVHXALVNKGLSJGREGGKSSWYWGZRJBOILWBHSJEFXVVHIWRCAGGWHASTJKDWMKNZFEZDWOITSNZLXARRLWFHSBAGHNMLRCTYWMBRAHEUYGCIIJGCAUVOIPTVJHFHUQEEUAHRWKLMAPUDGNYGLQUUEIIJXQIQHENVSRCHWBADGWGVXKRPLJSJSHDSMIKKINEKZGAHXDOUAUGXGYEJKHIOPUAGHNWHHPOUWEWSLARREGGVECEZFUHUYYTZFICQXDENZGFHEXOLLUCIEPRVSUIUIDIUVGBECYAGLCWQOEDUDGHWINFIWSIHRYIVKJOGEOTIGPUHJBETLQBWLADVKKUQSBSFEGYHCXORJFZDCKUKKVVHQKSKXTSTYANKDGHWINSRJGCQXDESGVHRQNONGHHKIXLZUMSQWZEIXGFWCLENJKHHVWNULJSKSIEIGYCIXDEUNQFDOOIDHNWIMADBWAPREND"
    decrypted = "LETTERFREQUENCIESLIKEWORDFREQUENCIESTENDTOVARYBOTHBYWRITERANDBYSUBJECTONECANNOTWRITEANESSAYABOUTXRAYSWITHOUTUSINGFREQUENTXSANDTHEESSAYWILLHAVEANIDIOSYNCRATICLETTERFREQUENCYIFTHEESSAYISABOUTTHEFREQUENTUSEOFXRAYSTOTREATZEBRASINQATARDIFFERENTAUTHORSHAVEHABITSWHICHCANBEREFLECTEDINTHEIRUSEOFLETTERSHEMINGWAYSWRITINGSTYLEFOREXAMPLEISVISIBLYDIFFERENTFROMFAULKNERSLETTERBIGRAMTRIGRAMWORDFREQUENCIESWORDLENGTHANDSENTENCELENGTHCANBECALCULATEDFORSPECIFICAUTHORSANDUSEDTOPROVEORDISPROVEAUTHORSHIPOFTEXTSEVENFORAUTHORSWHOSESTYLESARENOTSODIVERGENTACCURATEAVERAGELETTERFREQUENCIESCANONLYBEGLEANEDBYANALYZINGALARGEAMOUNTOFREPRESENTATIVETEXTWITHTHEAVAILABILITYOFMODERNCOMPUTINGANDCOLLECTIONSOFLARGETEXTCORPORASUCHCALCULATIONSAREEASILYMADEEXAMPLESCANBEDRAWNFROMAVARIETYOFSOURCESPRESSREPORTINGRELIGIOUSTEXTSSCIENTIFICTEXTSANDGENERALFICTIONANDTHEREAREDIFFERENCESESPECIALLYFORGENERALFICTIONWITHTHEPOSITIONOFHANDIWITHHBECOMINGMORECOMMONHERBERTSZIMINHISCLASSICINTRODUCTORYCRYPTOGRAPHYTEXTCODESANDSECRETWRITINGGIVESTHEENGLISHLETTERFREQUENCYSEQUENCEASETAONRISHDLFCMUGYPWBVKJXQZTHEMOSTCOMMONLETTERPAIRSASTHHEANREERINONATNDSTESENOFTEEDORTIHIASTOANDTHEMOSTCOMMONDOUBLEDLETTERSASLLEESSOOTTFFRRNNPPCCTHETOPTWELVELETTERSCOMPRISEABOUTOFTHETOTALUSAGETHETOPEIGHTLETTERSCOMPRISEABOUTOFTHETOTALUSAGELETTERFREQUENCYASAFUNCTIONOFRANKCANBEFITTEDWELLBYSEVERALRANKFUNCTIONSWITHTHETWOPARAMETERCOCHOBETARANKFUNCTIONBEINGTHEBESTANOTHERRANKFUNCTIONWITHNOADJUSTABLEFREEPARAMETERALSOFITSTHELETTERFREQUENCYDISTRIBUTIONREASONABLYWELLTHESAMEFUNCTIONHASBEENUSEDTOFITTHEAMINOACIDFREQUENCYINPROTEINSEQUENCESASPYUSINGTHEVICCIPHERORSOMEOTHERCIPHERBASEDONASTRADDLINGCHECKERBOARDTYPICALLYUSESAMNEMONICSUCHASASINTOERRDROPPINGTHESECONDRTOREMEMBERTHETOPEIGHTCHARACTERSTHEUSEOFLETTERFREQUENCIESANDFREQUENCYANALYSISPLAYSAFUNDAMENTALROLEINCRYPTOGRAMSANDSEVERALWORDPUZZLEGAMESINCLUDINGHANGMANSCRABBLEANDTHETELEVISIONGAMESHOWWHEELOFFORTUNEONEOFTHEEARLIESTDESCRIPTIONINCLASSICALLITERATUREOFAPPLYINGTHEKNOWLEDGEOFENGLISHLETTERFREQUENCYTOSOLVINGACRYPTOGRAMISFOUNDINEAPOESFAMOUSSTORYTHEGOLDBUGWHERETHEMETHODISSUCCESSFULLYAPPLIEDTODECIPHERAMESSAGEINSTRUCTINGONTHEWHEREABOUTSOFATREASUREHIDDENBYCAPTAINKIDDLETTERFREQUENCIESHADASTRONGEFFECTONTHEDESIGNOFSOMEKEYBOARDLAYOUTSTHEMOSTFREQUENTLETTERSAREONTHEBOTTOMROWOFTHEBLICKENSDERFERTYPEWRITERANDTHEHOMEROWOFTHEDVORAKSIMPLIFIEDKEYBOARD"
    key = "CODEWARS"
    mostCommonCharOverall = "E"

    print("Key Length: {}".format(len(key)))
    guessed_keyword = get_keyword(encrypted, len(key))
    print("Guessed key", guessed_keyword)
    print("Correct Key?", encrypt(decrypted, guessed_keyword) == encrypted)
    print("Decrypted: {}".format(encrypt(encrypted, key)))
