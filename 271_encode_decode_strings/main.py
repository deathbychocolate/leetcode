class Solution:

    @staticmethod
    def encode(strs: list[str]) -> str:
        return "".join([str(len(token)) + ":" + token for token in strs])

    @staticmethod
    def decode(strs: str) -> list[str]:
        num: str = ""
        i: int = 0
        token: str = ""
        result: list[str] = []
        read_prefix = True
        for c in list(strs):
            if i == 0 and c.isdigit():
                num += c
                continue
            if read_prefix and c == ":":
                i = int(num)
                read_prefix = False
                if i == 0:
                    # handle empty token (e.g. "0:")
                    result.append("")
                    num = ""
                    read_prefix = True
                continue
            if i > 0:
                token += c
                i -= 1
            if i == 0 and len(token) > 0:
                result.append(token)
                token = ""
                num = ""
                read_prefix = True


        return result


def main() -> None:
    r1 = ["hello"] == Solution.decode(Solution.encode(strs=["hello"]))
    r2 = ["world"] == Solution.decode(Solution.encode(strs=["world"]))
    r3 = ["a", "b"] == Solution.decode(Solution.encode(strs=["a", "b"]))
    r4 = ["123"] == Solution.decode(Solution.encode(strs=["123"]))
    r5 = ["!@#"] == Solution.decode(Solution.encode(strs=["!@#"]))
    r6 = [""] == Solution.decode(Solution.encode(strs=[""]))
    r7 = [] == Solution.decode(Solution.encode(strs=[]))
    r8 = ["test", "case"] == Solution.decode(Solution.encode(strs=["test", "case"]))
    r9 = ["longer", "string", "here"] == Solution.decode(Solution.encode(strs=["longer", "string", "here"]))
    r10 = ["a", "b", "c", "d"] == Solution.decode(Solution.encode(strs=["a", "b", "c", "d"]))
    r11 = ["single"] == Solution.decode(Solution.encode(strs=["single"]))
    r12 = ["multiple", "words", "in", "list"] == Solution.decode(Solution.encode(strs=["multiple", "words", "in", "list"]))
    r13 = ["1", "2", "3"] == Solution.decode(Solution.encode(strs=["1", "2", "3"]))
    r14 = ["@", "#", "$"] == Solution.decode(Solution.encode(strs=["@", "#", "$"]))
    r15 = ["a/b", "c/d"] == Solution.decode(Solution.encode(strs=["a/b", "c/d"]))
    r16 = ["a\\b", "c\\d"] == Solution.decode(Solution.encode(strs=["a\\b", "c\\d"]))
    r17 = ["a\nb", "c\nd"] == Solution.decode(Solution.encode(strs=["a\nb", "c\nd"]))
    r18 = ["a\tb", "c\td"] == Solution.decode(Solution.encode(strs=["a\tb", "c\td"]))
    r19 = ['a"b', 'c"d'] == Solution.decode(Solution.encode(strs=['a"b', 'c"d']))
    r20 = ["a'b", "c'd"] == Solution.decode(Solution.encode(strs=["a'b", "c'd"]))
    r21 = ["😊"] == Solution.decode(Solution.encode(strs=["😊"]))
    r22 = ["🚀", "🌟"] == Solution.decode(Solution.encode(strs=["🚀", "🌟"]))
    r23 = ["こんにちは"] == Solution.decode(Solution.encode(strs=["こんにちは"]))
    r24 = ["안녕하세요"] == Solution.decode(Solution.encode(strs=["안녕하세요"]))
    r25 = ["你好"] == Solution.decode(Solution.encode(strs=["你好"]))
    r26 = ["a" * 100] == Solution.decode(Solution.encode(strs=["a" * 100]))
    r27 = ["a" * 199] == Solution.decode(Solution.encode(strs=["a" * 199]))
    r28 = ["a", "b" * 198] == Solution.decode(Solution.encode(strs=["a", "b" * 198]))
    r29 = ["a\n" * 99] == Solution.decode(Solution.encode(strs=["a\n" * 99]))
    r30 = ["a\t" * 99] == Solution.decode(Solution.encode(strs=["a\t" * 99]))
    r31 = ["a\\" * 99] == Solution.decode(Solution.encode(strs=["a\\" * 99]))
    r32 = ["a/b" * 99] == Solution.decode(Solution.encode(strs=["a/b" * 99]))
    r33 = ["a:b" * 99] == Solution.decode(Solution.encode(strs=["a:b" * 99]))
    r34 = ["a,b" * 99] == Solution.decode(Solution.encode(strs=["a,b" * 99]))
    r35 = ["a;b" * 99] == Solution.decode(Solution.encode(strs=["a;b" * 99]))
    r36 = ["a[b]*99"] == Solution.decode(Solution.encode(strs=["a[b]*99"]))
    r37 = ["a{b}*99"] == Solution.decode(Solution.encode(strs=["a{b}*99"]))
    r38 = ["a(b)*99"] == Solution.decode(Solution.encode(strs=["a(b)*99"]))
    r39 = ["a<b>*99"] == Solution.decode(Solution.encode(strs=["a<b>*99"]))
    r40 = ["a>b" * 99] == Solution.decode(Solution.encode(strs=["a>b" * 99]))
    r41 = ["a=b" * 99] == Solution.decode(Solution.encode(strs=["a=b" * 99]))
    r42 = ["a+b" * 99] == Solution.decode(Solution.encode(strs=["a+b" * 99]))
    r43 = ["a-b" * 99] == Solution.decode(Solution.encode(strs=["a-b" * 99]))
    r44 = ["a*b" * 99] == Solution.decode(Solution.encode(strs=["a*b" * 99]))
    r45 = ["a^b" * 99] == Solution.decode(Solution.encode(strs=["a^b" * 99]))
    r46 = ["a&b" * 99] == Solution.decode(Solution.encode(strs=["a&b" * 99]))
    r47 = ["a|b" * 99] == Solution.decode(Solution.encode(strs=["a|b" * 99]))
    r48 = ["a~b" * 99] == Solution.decode(Solution.encode(strs=["a~b" * 99]))
    r49 = ["a`b" * 99] == Solution.decode(Solution.encode(strs=["a`b" * 99]))
    r50 = ["a!b" * 99] == Solution.decode(Solution.encode(strs=["a!b" * 99]))
    r51 = ["a@b" * 99] == Solution.decode(Solution.encode(strs=["a@b" * 99]))
    r52 = ["a#b" * 99] == Solution.decode(Solution.encode(strs=["a#b" * 99]))
    r53 = ["a$b" * 99] == Solution.decode(Solution.encode(strs=["a$b" * 99]))
    r54 = ["a%b" * 99] == Solution.decode(Solution.encode(strs=["a%b" * 99]))
    r55 = ["a\\nb" * 99] == Solution.decode(Solution.encode(strs=["a\\nb" * 99]))
    r56 = ["a\\tb" * 99] == Solution.decode(Solution.encode(strs=["a\\tb" * 99]))
    r57 = ["a\\\\b" * 99] == Solution.decode(Solution.encode(strs=["a\\\\b" * 99]))
    r58 = ['a\\"b' * 99] == Solution.decode(Solution.encode(strs=['a\\"b' * 99]))
    r59 = ["a\\'b" * 99] == Solution.decode(Solution.encode(strs=["a\\'b" * 99]))
    r60 = ["a\\/b" * 99] == Solution.decode(Solution.encode(strs=["a\\/b" * 99]))
    r61 = ["a\\b" * 99] == Solution.decode(Solution.encode(strs=["a\\b" * 99]))
    r62 = ["a\u0000b"] == Solution.decode(Solution.encode(strs=["a\u0000b"]))
    r63 = ["a\u0001b"] == Solution.decode(Solution.encode(strs=["a\u0001b"]))
    r64 = ["a\u001fb"] == Solution.decode(Solution.encode(strs=["a\u001fb"]))
    r65 = ["a\u007fb"] == Solution.decode(Solution.encode(strs=["a\u007fb"]))
    r66 = ["a\u0080b"] == Solution.decode(Solution.encode(strs=["a\u0080b"]))
    r67 = ["a\u07ffb"] == Solution.decode(Solution.encode(strs=["a\u07ffb"]))
    r68 = ["a\uffffb"] == Solution.decode(Solution.encode(strs=["a\uffffb"]))
    r69 = ["a\U0001f600b"] == Solution.decode(Solution.encode(strs=["a\U0001f600b"]))
    r70 = ["a\U0010ffffb"] == Solution.decode(Solution.encode(strs=["a\U0010ffffb"]))
    r71 = ["a\u20acb"] == Solution.decode(Solution.encode(strs=["a\u20acb"]))
    r72 = ["a\u2603b"] == Solution.decode(Solution.encode(strs=["a\u2603b"]))
    r73 = ["a\u2665b"] == Solution.decode(Solution.encode(strs=["a\u2665b"]))
    r74 = ["neet", "code", "love", "you"] == Solution.decode(Solution.encode(strs=["neet", "code", "love", "you"]))
    r75 = ["we", "say", ":", "yes"] == Solution.decode(Solution.encode(strs=["we", "say", ":", "yes"]))
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)
    print(r8)
    print(r9)
    print(r10)
    print(r11)
    print(r12)
    print(r13)
    print(r14)
    print(r15)
    print(r16)
    print(r17)
    print(r18)
    print(r19)
    print(r20)
    print(r21)
    print(r22)
    print(r23)
    print(r24)
    print(r25)
    print(r26)
    print(r27)
    print(r28)
    print(r29)
    print(r30)
    print(r31)
    print(r32)
    print(r33)
    print(r34)
    print(r35)
    print(r36)
    print(r37)
    print(r38)
    print(r39)
    print(r40)
    print(r41)
    print(r42)
    print(r43)
    print(r44)
    print(r45)
    print(r46)
    print(r47)
    print(r48)
    print(r49)
    print(r50)
    print(r51)
    print(r52)
    print(r53)
    print(r54)
    print(r55)
    print(r56)
    print(r57)
    print(r58)
    print(r59)
    print(r60)
    print(r61)
    print(r62)
    print(r63)
    print(r64)
    print(r65)
    print(r66)
    print(r67)
    print(r68)
    print(r69)
    print(r70)
    print(r71)
    print(r72)
    print(r73)
    print(r74)
    print(r75)


if __name__ == "__main__":
    main()
