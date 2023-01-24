# Get the base 10 value of a letter number in hex
def hex_digit():
    pass


def color_hex_sort():
    color_hexes = []
    for a in range(0, 16):
        for b in range(0, 16):
            for c in range(0, 16):
                for d in range(0, 16):
                    for e in range(0, 16):
                        for f in range(0, 16):
                            digit_f = f * 2
                            digit_e = e * 3
                            digit_d = d * 5
                            digit_c = c * 7
                            digit_b = b * 11
                            digit_a = a * 13
                            print(f"{digit_a}{digit_b}{digit_c}{digit_d}{digit_e}{digit_f}")
                            color_hexes.append(digit_a + digit_b + digit_c + digit_d + digit_e + digit_f)

    with open("color_hexes.txt", "w", encoding="utf-8") as f:
        f.write(str(color_hexes))

if __name__ == "__main__":
    color_hex_sort()