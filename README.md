# Save the Turkey 🦃

It's the night before Thanksgiving, and one brave turkey is trying to escape the farm before it ends up on someone's dinner table. **Your job: code a Python game where the room makes the decisions and luck decides what happens.**

If you don't have Python, click this link to an online compiler: https://www.programiz.com/python-programming/online-compiler/

## How the game works

- The turkey starts with **3 lives**
- The game has **5 scenes**, and each scene gives the room **2 choices**
- The room picks a choice, then the code uses **random chance** to decide if it works
- If the choice fails, the turkey **loses a life**
- If lives hit **0**, it's game over and the turkey becomes dinner 🍽️
- If the turkey makes it through all 5 scenes with **more than 0 lives**, the turkey is saved 🎉

## Your program should

1. Store the turkey's starting lives in a variable
2. Use the `scenes` list we give you (each scene has a description and 2 choices, and each choice has a chance of success)
3. Write a function that **shows how many lives** the turkey has left
4. Write a function that **prints the choices** and **asks the room to pick 1 or 2** (keep asking until the answer is valid)
5. Write a function that **plays one scene**: get the choice, roll a random number, and decide if the turkey succeeds or loses a life
6. **Loop through every scene**, and stop early if the turkey runs out of lives
7. At the end, print whether the turkey **escaped** or **became dinner**

## Hints

- `random.random()` gives you a random decimal between 0 and 1. If it's **less than** the choice's chance, the choice works.
- `enumerate()` lets you loop through a list and get a number for each item at the same time.
- Lists start counting at **0**, but people pick choices starting at **1**.

## Example output

```
🦃 SAVE THE TURKEY 🦃
Lives: ❤️ ❤️ ❤️ (3)

It's the night before Thanksgiving. You hear Farmer Fred sharpening the carving knife...
  1. Hide in the haystack
  2. Make a run for the barn door
What does the room decide? (1 or 2): 1
✅ Fred walks right past you. Smooth.
Lives: ❤️ ❤️ ❤️ (3)
```

## Bonus challenges

- Add your own scene to the story
- Give a scene a third choice
- Add a difficulty setting that changes the starting lives
