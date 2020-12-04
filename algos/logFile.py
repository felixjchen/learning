from pprint import pprint
logs = ["dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"]

logs2 = ["l5sh 6 3869 08 1295", "16o 94884717383724 9", "43 490972281212 3 51", "9 ehyjki ngcoobi mi", "2epy 85881033085988", "7z fqkbxxqfks f y dg", "9h4p 5 791738 954209", "p i hz uubk id s m l", "wd lfqgmu pvklkdp u", "m4jl 225084707500464",
         "6np2 bqrrqt q vtap h", "e mpgfn bfkylg zewmg", "ttzoz 035658365825 9", "k5pkn 88312912782538", "ry9 8231674347096 00", "w 831 74626 07 353 9", "bxao armngjllmvqwn q", "0uoj 9 8896814034171", "0 81650258784962331", "t3df gjjn nxbrryos b"]


def sortLogs(logs):
    def logOrder(log):
        identifier, line = log.split(" ", 1)

        return (0, line, identifier) if line[0].isalpha() else (1,)

    return sorted(logs, key=logOrder)


pprint((logs2))
pprint(sortLogs(logs2))
