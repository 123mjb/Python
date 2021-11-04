places = {s00: "empty", s01: "empty", s02: "empty", s10: "empty", s11: "empty", s12: "empty", s20: "empty", s21: "empty", s22: "empty",}
places [s00] = "X"
places [s10] = "X"
places [s20] = "X"
if places [s00] == "X" and [s10] == "X" and [s20] == "X":
    print("Player has won")
# across the top