#!/usr/bin/env python
# -*-coding:utf-8-*-


def is_need_turn_round(current, current_direction, visited, m, n):
    """
    判断基于当前位置是否需要转向
    基于当前方向获得下一个 如果下一个是有效的则不需要转向 如果下一个是无效的则转向
    """
    choice = next_choice(current, current_direction)
    if is_valid_choice(choice, visited, m, n):
        return False
    else:
        return True


def next_choice(current, current_direction):
    """
    基于当前位置获取下一个 不一定是有效
    """
    a, b = current
    if current_direction == 'w':
        return (a - 1, b)
    elif current_direction == 's':
        return (a + 1, b)
    elif current_direction == 'a':
        return (a, b - 1)
    elif current_direction == 'd':
        return (a, b + 1)


def is_valid_choice(choice, visited, m, n):
    """
    判断给定的下一个选项是否是有效的
    """
    a, b = choice
    if a < 0 or a >= m:
        return False
    if b < 0 or b >= n:
        return False

    if choice in visited:
        return False

    return True


def turn_round(current_direction, ):
    if current_direction == 'd':
        return 's'
    elif current_direction == 's':
        return 'a'
    elif current_direction == 'w':
        return 'd'
    elif current_direction == 'a':
        return 'w'


def go(res, current, current_direction, rested, visited, m, n):
    """
    最小的一步 首先判断是否需要转向 如果需要 执行转向动作再行走

    """
    if is_need_turn_round(current, current_direction, visited, m, n):
        current_direction = turn_round(current_direction)

    choice = next_choice(current, current_direction)

    # 当前的已访问
    visited.add(current)
    rested.remove(current)

    print(choice)  # 下一个是有效的 先打印
    res.append(choice)
    current = choice  # 行走
    return res, current, current_direction, rested, visited


def spiralOrder(m, n):
    res = []
    current_direction = 'd'
    start_point = (0, 0)
    print(start_point)
    res.append(start_point)
    rested = [(row_number, column_number) for row_number in range(m) for
              column_number in range(n)]
    visited = set()
    current = start_point
    while rested:
        # 重复步数
        res, current, current_direction, rested, visited = go(res, current,
                                                              current_direction,
                                                              rested, visited,
                                                              m, n)
    print(res)


TEST1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
TEST2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


def spiral(M):
    m = len(M)
    n = len(M[0])
    res = []
    for a, b in spiralOrder(m, n):
        item = M[a][b]
        res.append(item)
    return res


assert spiral(TEST1) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral(TEST2) == [1, 2, 3, 4, 8, 8, 12, 11, 10, 9, 5, 5, 6, 7, 7, 6]

if __name__ == '__main__':
    spiralOrder(3, 3)
