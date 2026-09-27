# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3115
```

OJ submission ID, if submitted:

```text
579748
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
โปรแกรมเช็กว่าจากร้านทั้งหมดที่ input ระบุไว้โดยเป็นช่วงเวลาเปิดร้านของแต่ละร้าน
ณ เวลาที่ input ระบุไว้เป็นนาทีในวันนั้น มีร้านเปิดอยู่กี่ร้าน
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
รับค่า num, check จากการ split input บรรทัดแรก
สร้าง list บันทึกช่วงเวลาเปิดร้านของแต่ละร้าน
วนลูป num ครั้ง
ในลูป ให้ split input และแปลงเป็น int แล้วเก็บไว้ใน list ที่สร้าง
รับค่าเวลาที่ต้องการจะเช็กโดยการ split input แล้วแปลงเป็น int ทั้งหมด
วนลูป โดย i เริ่มที่ 0 จบที่ check
สร้างตัวแปรเก็บจำนวนร้านที่เปิด ณ เวลา i
ในลูป ให้วนลูปใน list ที่บันทึกช่วงเวลาเปิดร้าน
    ในลูป list ให้เช็กว่า เวลา i อยู่ในช่วงเวลาที่ร้านเปิดหรือไม่
    ถ้าใช่ ให้ +1 จำนวนร้านที่เปิด
หลังจากจบลูป list ให้ปริ้นจำนวนร้านที่เปิดโดยไม่ขึ้นบรรทัดใหม่
วนลูปซ้ำจนกว่า i >= check
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
3 5
540 1020
600 660
1080 1200
600 659 660 900 1300
```

Expected output:

```text
2 2 1 1 0
```

Actual output:

```text
2 2 1 1 0
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
2 3
0 720
500 1000
100 700 800
```

Expected output:

```text
1 2 1
```

Actual output:

```text
1 2 1
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
ถ้าร้านเปิดและปิด ณ เวลาเดียวกัน = ร้านไม่เปิดเลย
```

Input:

```text
1 1
0 0
0
```

Expected output:

```text
0
```

Actual output:

```text
0
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
