# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3537
```

OJ submission ID, if submitted:

```text
669277
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
30-60 minutes
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
ให้รับข้อมูลผู้เล่นแต่ละคนเข้ามาก่อนเริ่มรอบ (มีบทบาท Crewmate กับ Impostor)
หลังจากเริ่มรอบแล้วจะมีการโหวตผู้เล่นออก ให้ปริ้นจำนวน Imposter ที่เหลืออยู่
แล้วแสดงว่าผู้เล่นคนไหนรอดและผู้เล่นคนไหนที่ถูกโหวตออก
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
players = dict ผู้เล่นทั้งหมดที่มีชีวิตรอด
dead = dict ผู้เล่นทั้งหมดที่ถูกโหวตออก
impostors = จำนวนผู้เล่นบทบาท Impostor ที่รอดอยู่
วนลูปจนกว่าจะเริ่มรอบ (input = "Start")
    ใช้ json โหลดข้อมูลที่ input ให้
    ถ้าข้อมูลบอกว่าผู้เล่นมีบทบาท "Impostor" ให้ impostors + 1
    เพิ่มข้อมูลผู้เล่นลงใน players
หลังจากเริ่มรอบ วนลูปจนกว่าจะจบรอบ (input = "End")
    ทำการ pop ข้อมูลของผู้เล่นที่มีชื่อตามที่ input ระบุ
    ถ้าบทบาท (ค่าที่ได้จากการ pop) เป็น "Impostor" ให้ impostors - 1
    ให้เพิ่ม key เป็นชื่อผู้เล่น และ value เป็นบทบาทของผู้เล่นลงใน dead
ทำการเรียง players และ dead ด้วย sorted (เรียงตามชื่อผู้เล่น)
ปริ้น f"{impostors} Impostor Remains"
ปริ้น "***Alive***"
ปริ้นรายชื่อผู้เล่นที่ยังมีชีวิตรอดอยู่
ปริ้น "***Dead***"
ปริ้นรายชื่อผู้เล่นที่ถูกโหวตออก
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
ไม่มีการเปลี่ยนแปลงเนื่องจากการโค้ดทำงานถูกต้องและสามารถผ่าน testcase ทั้งหมดได้
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
เพื่อเช็กได้ตรงกับ sample testcase หรือไม่
```

Input:

```text
{"Green" : "Crewmate"}
{"Cyan" : "Crewmate"}
{"Red" : "Crewmate"}
{"Pink" : "Crewmate"}
{"Lime" : "Impostor"}
{"Blue" : "Impostor"}
{"White" : "Crewmate"}
{"Orange" : "Crewmate"}
Start
Green
Cyan
White
End
```

Expected output:

```text
2 Impostor Remains
***Alive***
Blue : Impostor
Lime : Impostor
Orange : Crewmate
Pink : Crewmate
Red : Crewmate
***Dead***
Cyan : Crewmate
Green : Crewmate
White : Crewmate
```

Actual output:

```text
2 Impostor Remains
***Alive***
Blue : Impostor
Lime : Impostor
Orange : Crewmate
Pink : Crewmate
Red : Crewmate
***Dead***
Cyan : Crewmate
Green : Crewmate
White : Crewmate
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
เพื่อเช็กได้ตรงกับ sample testcase หรือไม่
```

Input:

```text
{"Aqua" : "Crewmate"}
{"Suisei" : "Impostor"}
{"Fubuki" : "Crewmate"}
{"Matsuri" : "Impostor"}
{"Impostor" : "Crewmate"}
{"Pekora" : "Impostor"}
{"Korone" : "Crewmate"}
{"Rushia" : "Crewmate"}
{"Kusa" : "Crewmate"}
{"Yagoo" : "Crewmate"}
{"Marine" : "Crewmate"}
{"Pinkguy" : "Crewmate"}
{"Crewmate" : "Impostor"}
{"Watame" : "Crewmate"}
Start
Aqua
Suisei
Fubuki
Matsuri
Crewmate
Pekora
End
```

Expected output:

```text
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Watame : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Impostor
Fubuki : Crewmate
Matsuri : Impostor
Pekora : Impostor
Suisei : Impostor
```

Actual output:

```text
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Watame : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Impostor
Fubuki : Crewmate
Matsuri : Impostor
Pekora : Impostor
Suisei : Impostor
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
ถ้าหากไม่ได้โหวตใครออกจะไม่มีผู้เล่นคนไหนตาย
```

Input:

```text
{"Thatguy" : "Crewmate"}
{"I" : "Crewmate"}
{"You" : "Crewmate"}
{"Who" : "Impostor"}
{"Thisguy" : "Crewmate"}
{"Him" : "Crewmate"}
{"Her" : "Impostor"}
Start
End
```

Expected output:

```text
2 Impostor Remains
***Alive***
Her : Impostor
Him : Crewmate
I : Crewmate
Thatguy : Crewmate
Thisguy : Crewmate
Who : Impostor
You : Crewmate
***Dead***
```

Actual output:

```text
2 Impostor Remains
***Alive***
Her : Impostor
Him : Crewmate
I : Crewmate
Thatguy : Crewmate
Thisguy : Crewmate
Who : Impostor
You : Crewmate
***Dead***
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
No
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text
None
```

What did they help with?

```text
None
```

What did you still do by yourself?

```text
Everything
```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
