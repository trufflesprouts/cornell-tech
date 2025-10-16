\ Model assignment7
\ LP format - for model browsing. Use MPS format to capture full model detail.
\ Signature: 0xfe1120661f43bda8
Minimize
  x_01 + 2 x_02 + x_12 + 5 x_13 + 2 x_14 + 2 x_23 + x_24 + 4 x_25 + 3 x_34
   + 6 x_35 + 8 x_36 + 3 x_45 + 7 x_46 + 5 x_56 + 2 x_57 + 6 x_67
Subject To
 R0: x_01 + x_02 = 1
 R1: - x_01 + x_12 + x_13 + x_14 = 0
 R2: - x_02 - x_12 + x_23 + x_24 + x_25 = 0
 R3: - x_13 - x_23 + x_34 + x_35 + x_36 = 0
 R4: - x_14 - x_24 - x_34 + x_45 + x_46 = 0
 R5: - x_25 - x_35 - x_45 + x_56 + x_57 = 0
 R6: - x_36 - x_46 - x_56 + x_67 = 0
 R7: - x_57 - x_67 = -1
Bounds
End
