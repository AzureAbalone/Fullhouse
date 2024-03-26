from typing import List, Any, Generator

with open("Test\\test.txt", "r") as f, open("SDT.txt", "w") as g:
    comments: str = f.read()
    for temp in comments.split("\n"):
        if "0" in temp:
            for i in temp.split():
                if "0" in i:
                    index: str = i.index("0")
                    temp: List[str] = list(i[index : index + 9])
                    check: bool = next(
                        (True for j in range(97, 123) if chr(j) in temp),
                        any(chr(j) in temp for j in range(65, 91)),
                    )
                    if check:
                        break
                    else:
                        (
                            g.write(f"{''.join(temp+[i[index+9]])}\n")
                            if i[index + 9] in map(str, range(10))
                            else g.write(f"{''.join(temp)}\n")
                        )
