"""
Input:

    a string strng
    an array of strings arr
    Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):

    a boolean true if all rotations of strng are included in arr (C returns 1)
    false otherwise (C returns 0)

Note:
    Though not correct in a mathematical sense

    we will consider that there are no rotations of strng == ""
    and for any array arr: contain_all_rots("", arr) --> true
"""


def contain_all_rots(strng, arr):
    if strng == '':
        return True

    rots = [strng[i:] + strng[:i] for i in range(len(strng))]

    return all([rot in arr for rot in rots])


if __name__ == '__main__':
    print(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))
