# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3110
```

OJ submission ID, if submitted:

```text
579751
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
ให้หาค่าธรรมเนียมการส่งพัสดุจากเส้นทางต่างที่ระบุจาก input
ถ้าเส้นทางที่ input ให้ไม่มีอยู่ในเส้นทางที่โจทย์กำหนดไว้จะได้ข้อความ "Error"
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
สร้าง dict ซ้อน dict โดยให้ชั้นแรกเป็นต้นทางและชั้นที่สองเป็นปลายทาง
โดย dict ชั้นที่สองให้เก็บค่าธรรมเนียมเริ่มต้นกับค่าธรรมเนียมน้ำหนัก
รับ input จากนั้น split แล้วเก็บไว้ในตัวแปร start (ต้นทาง), และ dest (ปลายทาง)
รับค่าน้ำหนักพัสดุ
จากนั้นให้เช็กว่า start เป็น key ของ dict เส้นทางชั้นแรก และเมื่อใช้ key ต้นทางเข้าไปยัง
dict เส้นทางชั้นที่สองและ dest เป็น key ของ dict นั้น
ถ้าถูกต้อง (เส้นทางโจทย์ระบุไว้) ให้นำค่าที่ได้จากการเข้า dict เส้นทางสองชั้นนั้น
    มาคำนวณกับน้ำหนักของพัสดุแล้วปริ้น
ถ้าผิด (โจทย์ไม่ได้ระบุว่ามีเส้นทางดังกล่าว) ให้ปริ้น Error
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
BKK CNX
2
```

Expected output:

```text
70.00
```

Actual output:

```text
70.00
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
UBP PKT
3.33
```

Expected output:

```text
273.10
```

Actual output:

```text
273.10
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
ถ้าพัสดุไร้น้ำหนักก็ยังต้องจ่ายค่าธรรมเนียมเริ่มต้น
```

Input:

```text
BKK PKT
0
```

Expected output:

```text
25.00
```

Actual output:

```text
25.00
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
