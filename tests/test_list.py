#!/usr/bin/env python
# -*-coding:utf-8-*-

from pywander.list import del_list, double_iter, NearlyOrderedList


def test_del_list():
    assert del_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [2, 5, 9]) == [0, 1, 3, 4, 6, 7, 8]


def test_double_iter():
    lst = ['A', 'B', 'C', 'D']
    assert list(double_iter(lst)) == [('A', 'B'), ('A', 'C'), ('A', 'D'),
                                      ('B', 'C'),
                                      ('B', 'D'), ('C', 'D')]

    assert list(double_iter(lst, mode='product')) == [('A', 'A'), ('A', 'B'),
                                                      ('A', 'C'), ('A', 'D'),
                                                      ('B', 'A'), ('B', 'B'),
                                                      ('B', 'C'), ('B', 'D'),
                                                      ('C', 'A'), ('C', 'B'),
                                                      ('C', 'C'), ('C', 'D'),
                                                      ('D', 'A'), ('D', 'B'),
                                                      ('D', 'C'), ('D', 'D')]

    assert list(double_iter(lst, mode='permutations')) == [('A', 'B'),
                                                           ('A', 'C'),
                                                           ('A', 'D'),
                                                           ('B', 'A'),
                                                           ('B', 'C'),
                                                           ('B', 'D'),
                                                           ('C', 'A'),
                                                           ('C', 'B'),
                                                           ('C', 'D'),
                                                           ('D', 'A'),
                                                           ('D', 'B'),
                                                           ('D', 'C')]

    assert list(double_iter(lst, mode='combinations_with_replacement')) == [
        ('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'),
        ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]


def test_nearly_ordered_list():
    from dataclasses import dataclass
    test_data = [{'content': 'Aaberg', 'map': (7, 8)}, {'content': 'Aabye', 'map': (8, 9)},
                 {'content': 'Aadahi', 'map': (9, 10)}, {'content': 'Aagaard', 'map': (10, 11)},
                 {'content': 'Aaker', 'map': (11, 12)}, {'content': 'Aaliyah', 'map': (12, 13)},
                 {'content': 'Aall', 'map': (13, 14)}, {'content': 'Aalseth', 'map': (14, 15)},
                 {'content': 'Aalto', 'map': (15, 16)}, {'content': 'Aamodt', 'map': (16, 17)},
                 {'content': 'Aamoth', 'map': (17, 18)}, {'content': 'Aandahl', 'map': (18, 19)},
                 {'content': 'Aanenson', 'map': (19, 20)}, {'content': 'Aaneson', 'map': (20, 21)},
                 {'content': 'Aaran', 'map': (21, 22)}, {'content': 'Aaren', 'map': (22, 23)},
                 {'content': 'Aarik', 'map': (23, 24)}, {'content': 'Aaron', 'map': (24, 25)},
                 {'content': 'Aaronian', 'map': (25, 26)}, {'content': 'Aarons', 'map': (26, 27)},
                 {'content': 'Aaronson', 'map': (27, 28)}, {'content': 'Aarron', 'map': (28, 29)},
                 {'content': 'Aars', 'map': (29, 30)}, {'content': 'Aarsleff', 'map': (30, 31)},
                 {'content': 'Aarvold', 'map': (31, 32)}, {'content': 'Aasen', 'map': (32, 33)},
                 {'content': 'Aawick', 'map': (33, 34)}, {'content': 'Ab', 'map': (34, 35)},
                 {'content': 'Abaddon', 'map': (35, 36)}, {'content': 'Abadi', 'map': (36, 37)},
                 {'content': 'Abady', 'map': (37, 38)}, {'content': 'Abaegayle', 'map': (38, 39)},
                 {'content': 'Abagael', 'map': (39, 40)}, {'content': 'Abagail', 'map': (40, 41)},
                 {'content': 'Abagale', 'map': (41, 42)}, {'content': 'Abaigael', 'map': (42, 43)},
                 {'content': 'Abaigeal', 'map': (43, 44)}, {'content': 'Abalo', 'map': (44, 45)},
                 {'content': 'Abarbanel', 'map': (45, 46)}, {'content': 'Abare', 'map': (46, 47)},
                 {'content': 'Abastenia', 'map': (47, 48)}, {'content': 'Abate', 'map': (48, 49)},
                 {'content': 'Abayomi', 'map': (49, 50)}, {'content': 'Abbadessa', 'map': (50, 51)},
                 {'content': 'Abbado', 'map': (51, 52)}, {'content': 'Abban', 'map': (52, 53)},
                 {'content': 'Abbate', 'map': (53, 54)}, {'content': 'Abbe', 'map': (54, 55)},
                 {'content': 'Abbel', 'map': (55, 56)}, {'content': 'Abbelina', 'map': (56, 57)},
                 {'content': 'Abbell', 'map': (57, 58)}, {'content': 'Abbels', 'map': (58, 59)},
                 {'content': 'Abben', 'map': (59, 60)}, {'content': 'Abbenhaus', 'map': (60, 61)},
                 {'content': 'Abberley', 'map': (61, 62)}, {'content': 'Abbett', 'map': (62, 63)},
                 {'content': 'Abbey', 'map': (63, 64)}, {'content': 'Abbi', 'map': (64, 65)},
                 {'content': 'Abbiati', 'map': (65, 66)}, {'content': 'Abbie', 'map': (66, 67)},
                 {'content': 'Abbigael', 'map': (67, 68)}, {'content': 'Abbigail', 'map': (68, 69)},
                 {'content': 'Abbigale', 'map': (69, 70)}, {'content': 'Abbigayle', 'map': (70, 71)},
                 {'content': 'Abbink', 'map': (71, 72)}, {'content': 'Abbiss', 'map': (72, 73)},
                 {'content': 'Abbitt', 'map': (73, 74)}, {'content': 'Abbot', 'map': (74, 75)},
                 {'content': 'Abbotson', 'map': (75, 76)}, {'content': 'Abbott', 'map': (76, 77)},
                 {'content': 'Abboud', 'map': (77, 78)}, {'content': 'Abbrecht', 'map': (78, 79)},
                 {'content': 'Abbs', 'map': (79, 80)}, {'content': 'Abbuhl', 'map': (80, 81)},
                 {'content': 'Abby', 'map': (81, 82)}, {'content': 'Abbye', 'map': (82, 83)},
                 {'content': 'Abbygael', 'map': (83, 84)}, {'content': 'Abbygail', 'map': (84, 85)},
                 {'content': 'Abbygale', 'map': (85, 86)}, {'content': 'Abdalian', 'map': (86, 87)},
                 {'content': 'Abdian', 'map': (87, 88)}, {'content': 'Abdiel', 'map': (88, 89)},
                 {'content': 'Abdnor', 'map': (89, 90)}, {'content': 'Abdon', 'map': (90, 91)},
                 {'content': 'Abdy', 'map': (91, 92)}, {'content': 'Abe', 'map': (92, 93)},
                 {'content': 'Abebe', 'map': (93, 94)}, {'content': 'Abedabun', 'map': (94, 95)},
                 {'content': 'Abeel', 'map': (95, 96)}, {'content': 'Abegail', 'map': (96, 97)},
                 {'content': 'Abegayle', 'map': (97, 98)}, {'content': 'Abegg', 'map': (98, 99)},
                 {'content': 'Abegglen', 'map': (99, 100)}, {'content': 'Abel', 'map': (100, 101)},
                 {'content': 'Abelard', 'map': (101, 102)}, {'content': 'Abele', 'map': (102, 103)},
                 {'content': 'Abeles', 'map': (103, 104)}, {'content': 'Abelia', 'map': (104, 105)},
                 {'content': 'Abeliovich', 'map': (105, 106)}, {'content': 'Abell', 'map': (106, 107)}]

    @dataclass
    class WordEntry:
        content: str
        map: tuple

        def __lt__(self, other):
            return self.content.lower() < other.content.lower()

        def __eq__(self, other):
            return self.content.lower() == other.content.lower()

        def __repr__(self):
            return f"<WordEntry: {self.content} in map: {self.map}>"

    test_data = [WordEntry(item.get('content'), item.get('map')) for item in test_data]

    my_list = NearlyOrderedList(test_data)
    my_list.find_anomaly_intervals(init_size=20, min_size=5)

    # 制造错误数据
    test_data[2], test_data[5] = test_data[5], test_data[2]
    test_data[49], test_data[50] = test_data[50], test_data[49]
    test_data[50], test_data[51] = test_data[51], test_data[50]

    my_list = NearlyOrderedList(test_data)
    abnormal_data = my_list.find_anomaly_intervals(init_size=20, min_size=5)

    assert test_data[2] in abnormal_data
    assert test_data[5] in abnormal_data
    assert test_data[49] in abnormal_data
    assert test_data[50] in abnormal_data
    assert test_data[51] in abnormal_data


