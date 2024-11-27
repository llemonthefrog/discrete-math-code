import codes

types_of_coding = {
                   "uni" : codes.uniform_code,
                   "ariph" : codes.ariph_code
                }


if __name__ == "__main__":
    print("insert type of operation:")
    for num, tp in enumerate(types_of_coding):
        print(f"{num}. {tp}")

    t: str = input()

    while(not (t in types_of_coding)):
        t: str = input("please insert correct type of operation: \n")
    
    msg: str = input("insert message:\n")

    result: str = types_of_coding[t](msg)
    print(f"result: {result}\nshr: {len(types_of_coding["uni"](msg))/len(result)}")