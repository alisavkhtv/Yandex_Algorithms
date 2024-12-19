# Air Conditioner (design of tests)

### Description:
At the competition, participants were presented with the following task: In the office where programmer Peter works, a new type of air conditioner has been installed. This air conditioner is characterized by its simplicity in operation. It has only two controllable parameters: the desired temperature and the operating mode.
The air conditioner can operate in the following four modes:
- "freeze" — cooling. In this mode, the air conditioner can only decrease the temperature. If the room temperature is already not higher than the desired temperature, it turns off.
- "heat" — heating. In this mode, the air conditioner can only increase the temperature. If the room temperature is already not lower than the desired temperature, it turns off.
- "auto" — automatic mode. In this mode, the air conditioner can both increase and decrease the room temperature to reach the desired level.
- "fan" — ventilation. In this mode, the air conditioner only circulates air and does not change the room temperature.

The air conditioner is powerful enough that when set to the correct operating mode, it will bring the room temperature to the desired level within one hour.
You are required to write a program that determines what the room temperature will be in one hour based on the given room temperature t_room, the desired temperature t_cond set on the air conditioner, and its operating mode. You need to develop a set of test cases (input data only) for this task that thoroughly checks participants' solutions.

### Output:
You should submit a text file, not a program.

In the first line of the file, write the number N (1 ≤ N ≤ 20) — the number of tests you have developed. In the following N lines, write one test case per line. Each test case should consist of two numbers t_room and t_cond (−50 ≤ t_room, t_cond ≤ 50) and an operating mode (one of the words freeze, heat, auto, fan).
