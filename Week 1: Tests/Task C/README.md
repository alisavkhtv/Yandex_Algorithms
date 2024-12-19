# A Letter on the Display

### Time constraints: 1 sec
### Memory constraints: 256 Mb

### Description:

You have gained access to one of the surveillance cameras in a highly secret organization. In the camera's field of view is a display board from which you continuously read information. Now you need to write a program that determines which letter is currently depicted on it based on the state of the display. The display consists of a square grid divided into n×n equal square LEDs. Each LED is either on or off. Let's introduce a coordinate system where the OX axis points to the right and the OY axis points upwards, with the side of each LED equal to 1.

The display can only show the following letters:
- I — A rectangle of lit LEDs
- O — A rectangle of lit LEDs with corners at (x_1, y_1) and (x_2, y_2), inside which there is a rectangle of turned-off LEDs with corners at (x_3, y_3) and (x_4, y_4). The boundaries of the turned-off rectangle should not touch the outer rectangle, meaning x_1 < x_3 < x_4 < x_2 and y_1 < y_3 < y_4 < y_2
- C — A rectangle of lit LEDs with corners at (x_1, y_1) and (x_2, y_2), inside which there is a rectangle of turned-off LEDs with corners at (x_3, y_3) and (x_4, y_4). The right boundary of the turned-off rectangle coincides with the right boundary of the outer rectangle, meaning x_1 < x_3 < x_4 = x_2 and y_1 < y_3 < y_4 < y_2
- L — A rectangle of lit LEDs with corners at (x_1, y_1) and (x_2, y_2), inside which there is a rectangle of turned-off LEDs with corners at (x_3, y_3) and (x_4, y_4). The upper right corners of the turned-off rectangle and the outer rectangle coincide, meaning x_1 < x_3 < x_4 = x_2 and y_1 < y_3 < y_4 = y_2
- H — A rectangle of lit LEDs with corners at (x_1, y_1) and (x_2, y_2), inside which are two rectangles of turned-off LEDs with corners at (x_3, y_3), (x_4, y_4) for the first one and (x_5, y_5), (x_6, y_6) for the second one. The turned-off rectangles must have equal width, be strictly one below the other, with one touching the top side and the other touching the bottom side of the outer rectangle: x_1 < x_3 = x_5 < x_4 = x_6 < x_2 and y_1 = y_3 < y_4 < y_5 < y_6 = y_2
- P — A rectangle of lit LEDs with corners at (x_1, y_1) and (x_2, y_2), inside which are two rectangles of turned-off LEDs with corners at (x_3, y_3), (x_4, y_4) for the first one and (x_5, y_5), (x_6, y_6) for the second one. The lower right corner of the first turned-off rectangle must coincide with the lower right corner of the outer rectangle while the other turned-off rectangle must be strictly above it without touching any boundaries; also, the left boundaries of both turned-off rectangles must coincide: x_1 < x_3 = x_5 < x_6 < x_4 = x_2
and y_1 = y_3 < y_4 < y_5 < y_6 < y_2.

Any other state of the display is considered to represent the letter X.

Based on the appearance of the display board, determine which letter is depicted on it.

### Input:
The first line of input contains a single number n (1 ≤ n ≤ 10) — the side length of the display. The following n lines contain strings of length n made up of characters “.” and “#” — strings representing the grid. “.” denotes an off LED while “#” denotes an on LED.

### Output:
The program should output a single character: if this table fits any description for letters I, O, C, L, H, P, then output that letter (all letters are in English). If this table does not fit any conditions for these letters, then output X.
