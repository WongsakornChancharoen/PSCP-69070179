# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3036
```

OJ submission ID, if submitted:

```text
562650
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
รับ input เป็นเลขจำนวนเต็มซึ่งเป็นเลขห้องในปราสาท โดยปราสาทแต่ละชั้นจะมีห้อง
2 * (ชั้น - 1) + 1 นับจากบนลงล่าง แล้ว output ต้องเป็นจำนวนห้องที่ต้องผ่านจนกว่าจะถึงห้องหมายเลข 1
และต้องเป็นทางที่สั้นที่สุด
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
Step 1: รับ Input เป็นจำนวนเต็ม
Step 2: ใช้สูตรหาชั้นที่ห้องหมายเลขจาก input
Step 3: หาห้องที่เลขต่ำสุดภายในชั้นนั้น
Step 4: นำมาลบกันแล้วหาทางที่สั้นที่สุดจากห้องตำแหน่งนั้น
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
เปลี่ยนมาใช้ loop แทนเพราะเป็นวิธีที่ง่ายและทำความเข้าใจได้ดีกว่า
Step 1: รับ Input เป็นจำนวนเต็ม
Step 2: สร้างตัวแปรบันทึกเลขชั้น, เลขห้องต่ำสุดและสูงสุดไว้
Step 3: ใช้ while loop ที่วนจนกว่าเลขห้องสูงสุดจะเยอะกว่าเลขห้องจาก input
Step 4: ใน loop ให้บวกเพิ่มเลขห้องต่ำสุดและสูงสุดด้วยสูตร
    2 * (ชั้น - 1) + 1 และ 2 * ชั้น + 1 ตามลำดับ
Step 5: หลังจากจบ loop ให้สร้างตัวแปรเก็บห้องที่ต้องเดินทางผ่าน
Step 6: ถ้าห้องมากกว่า 1 แล้ว
    ตำแหน่งห้องภายในชั้น = เลขห้องจาก input - เลขห้องในชั้นที่น้อยที่สุด
    ถ้าตำแหน่งห้องเป็นเลขคู่ ให้ จำนวนห้องที่ต้องผ่าน = (ชั้น - 1) * 2 เนื่องจาก
        ตำแหน่งห้องเลขคู่จะเป็นสามเหลี่ยมที่ชี้ขึ้นข้างบน
        สามารถไปได้แค่ห้องซ้าย/ขวา ไม่งั้นจะเป็นการย้อนกลับ
    ถ้าเป็นเลขคี่ ให้ จำนวนห้องที่ต้องผ่าน = (ชั้น - 1) * 2 - 1 เนื่องจาก
        ตำแหน่งห้องเลขคี่จะเป็นสามเหลี่ยมที่ชี้ลงข้างล่าง
        สามารถเดินตรงไปยังชั้นต่อไปได้เลย
Step 7: ปริ้นจำนวนห้องที่ต้องผ่าน
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
เพื่อทดสอบว่าคำตอบเหมือน testcase ใน ijudge หรือไม่
```

Input:

```text
21
```

Expected output:

```text
8
```

Actual output:

```text
8
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
เพื่อทดสอบว่าคำตอบเหมือน testcase ใน ijudge หรือไม่
```

Input:

```text
11
```

Expected output:

```text
5
```

Actual output:

```text
5
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
เพื่อทดสอบว่าถ้าหาก input เป็น 1 output จะต้องเป็น 0
เนื่องจากไม่จำเป็นต้องเดินผ่านห้องใดแล้ว
```

Input:

```text
1
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
