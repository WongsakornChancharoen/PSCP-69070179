# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3386
```

OJ submission ID, if submitted:

```text
652001
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
ให้หาว่าในกลุ่ม a มีรหัสนักศึกษาที่มีอยู่ในกลุ่ม b กี่คน (อยู่ 2 กลุ่ม)
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
รับค่า n, m
a, b = set เก็บรหัสนักศึกษา
วนลูป n ครั้ง
    เพิ่มรหัสนักศึกษาเข้า set a
วนลูป m ครั้ง
    เพิ่มรหัสนักศึกษาเข้า set b
นำ set a มาใช้ intersection_update กับ b
ถ้าใน a มีสมาชิกอยู่
    วนลูปใน a แล้วปริ้นทีละรหัส
ถ้าไม่ให้ปริ้น Nope
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
10
10
56070147
59070002
58070161
59070044
59070019
59070116
58070040
59070032
58070009
59070048
59070135
59070063
59070146
59070149
59070141
59070103
59070110
59070008
59070158
59070188
```

Expected output:

```text
Nope
```

Actual output:

```text
Nope
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
15
12
59070158
59070074
59070173
59070012
59070191
59070078
59070167
59070127
59070116
59070105
59070155
58070153
59070182
59070047
59070061
59070185
59070148
59070065
58070015
59070173
59070070
59070012
58070161
59070116
59070170
58070108
59070049
```

Expected output:

```text
59070173
59070116
59070012
```

Actual output:

```text
59070173
59070116
59070012
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
ถ้ากลุ่ม b ไม่มีสมาชิกจะไม่มีการเทียบ
```

Input:

```text
1
0
5607170
5607179
5607196
```

Expected output:

```text
Nope
```

Actual output:

```text
Nope
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
