def remove_just_one(redundant_list:list[int], remove_number:int) -> list[int]:
    not_removed = True
    ret = []
    for l in redundant_list:
        if l == remove_number and not_removed:
            not_removed = False
            continue
        ret.append(l)
    return ret

if __name__ == "__main__":
    redundant_list = [1,1,2,3,3,3,4]
    remove_number = 3
    print(remove_just_one(redundant_list, remove_number))