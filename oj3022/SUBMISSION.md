# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3022
```

OJ submission ID, if submitted:

```text
548834
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
0-15 minutes
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
รับ input 3 บรรทัด
ซึ่งจะเป็นค่าจำนวนจริง หน่วยอุณหภูมิเริ่มต้นและหน่วยอุณหภูมิที่ต้องการตามลำดับ
และหน่วยอุณหภูมิทั้งสองจาก input เป็นค่า string
ต้องแปลงหน่วยอุณหภูมิที่มีค่าตาม input บรรทัดแรก ไปเป็นอีกหน่วยที่มีค่าต่างกัน
โดยใช้สูตรตามที่คำอธิบายโจทย์ให้มา
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
Step 1: รับ Input 3 บรรทัด (ค่าอุณหภูมิ, หน่วยเริ่มต้น, หน่วยที่ต้องการ)
Step 2: สร้าง function แยกให้แต่ละอุณหภูมิ แต่ละ function จะรับค่าอุณหภูมิและหน่วยที่ต้องการ
    เช่น Celsius(n, newtemp) -> ถ้า newtemp == "F": ปริ้น ค่าอุณหภูมิในหน่วย F จากหน่วย C
        Kelvin(n, newtemp) -> ถ้า newtemp == "R": ปริ้น ค่าอุณหภูมิในหน่วย R จากหน่วย K
Step 3: เรียกใช้ function ตามหน่วยเริ่มต้น
    ถ้า หน่วยเริ่มต้น == "C": Celsius(ค่าอุณหภูมิ, หน่วยที่ต้องการ)
    หรือถ้า หน่วยเริ่มต้น == "R": Rankine(ค่าอุณหภูมิ, หน่วยที่ต้องการ)
    ต่อไปจนกว่าจะครบ
Step 4: ปริ้น output เป็นเลขทศนิยม 2 หน่วย
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
Step 1: รับ Input 3 บรรทัด (ค่าอุณหภูมิ, หน่วยเริ่มต้น, หน่วยที่ต้องการ)
Step 2: แปลงอุณหภูมิจากหน่วยเริ่มต้น เป็นหน่วย C
Step 3: แปลงอุณหภูมิหน่วย C เป็นอุณหภูมิในหน่วยที่ต้องการ
Step 4: ปริ้น output เป็นเลขทศนิยม 2 หน่วย
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
เพื่อทดสอบว่าถ้าแปลงจากหน่วย C เป็นหน่วย C เหมือนเดิมค่าจะเท่าเดิม
```

Input:

```text
69.6
C
C
```

Expected output:

```text
69.60
```

Actual output:

```text
69.60
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
เพื่อทดสอบว่าการแปลงหน่วยถูกต้อง
```

Input:

```text
0
C
F
```

Expected output:

```text
32.00
```

Actual output:

```text
32.00
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
เพื่อทดสอบว่าการแปลงหน่วยถูกต้อง
```

Input:

```text
42
R
K
```

Expected output:

```text
23.33
```

Actual output:

```text
23.33
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
