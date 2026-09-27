# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3360
```

OJ submission ID, if submitted:

```text
647923
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
1-3 hours
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
หาพื้นที่ของขนมปังชิ้นที่ใหญ่ที่ได้สุดและใหญ่ที่สุดเป็นอันดับ 2
จากการหั่นด้วยมีดในแนวตั้งและแนวนอน
ตามตำแหน่งและจำนวนที่ input ระบุ
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
รับค่าความกว้าง (w), ความสูง (h), จำนวนมีดแนวตั้ง (m), และจำนวนมีดแนวนอน (n)
รับค่าตำแหน่งมีดแนวตั้ง แล้วแปลงเป็น int เก็บใน list ชื่อ verts
รับค่าตำแหน่งมีดแนวนอน แล้วแปลงเป็น int เก็บใน list ชื่อ horiz
สร้าง list cut_verts และ cut_horiz เพื่อเก็บความกว้างและความสูงของขนมปังแต่ละชิ้นที่ถูกตัด
คำนวณความกว้างชิ้นแรกและชิ้นสุดท้ายจากการตัดแนวตั้งครั้งแรก
วนลูปเพื่อคำนวณปรับความกว้างของขนมปังที่ได้จากการตัดแนวตั้งที่เหลือ (m ชิ้น)
คำนวณความสูงชิ้นแรกและชิ้นสุดท้ายจากการตัดแนวขวางครั้งแรก
วนลูปเพื่อคำนวณปรับความสูงของขนมปังที่ได้จากการตัดแนวขวางที่เหลือ (n ชิ้น)
กำหนดตัวแปร large_pieces = [0, 0] เพื่อเก็บพื้นที่ขนาดใหญ่ที่สุดและใหญ่เป็นอันดับสอง
วนลูปคำนวณพื้นที่ขนมปังทุกชิ้น (size = x * y)
    ถ้า size > พื้นที่อันดับ 1 ให้ปรับพื้นที่อันดับ 1 ใหม่
    ถ้าไม่ และ size > พื้นที่อันดับ 2 ให้ปรับพื้นที่อันดับ 2 ใหม่
แสดงผลลัพธ์ พื้นที่ชิ้นที่ใหญ่ที่สุด และ ใหญ่เป็นอันดับสอง
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
เนื่องจากโค้ดไม่สามารถผ่าน testcase ทั้งหมดได้เลยทำการแก้โค้ด
รับค่า w, h, m, n
สร้าง list เก็บตำแหน่งมีดแนวตั้ง (verts) และแนวขวาง (horiz)
วนลูป m รอบ รับค่าตำแหน่งมีดแนวตั้ง แล้วใส่ใน verts
วนลูป n รอบ รับค่าตำแหน่งมีดแนวขวาง แล้วใส่ใน horiz
สร้างพิกัดมีดแนวตั้งทั้งหมด x = [0] + verts + [w]
หาความกว้างของแต่ละชิ้น (widths) โดยเอาพิกัดติดกันมาลบกัน
สร้างพิกัดมีดแนวขวางทั้งหมด y = [0] + horiz + [h]
หาความสูงของแต่ละชิ้น (heights) โดยเอาพิกัดติดกันมาลบกัน
เรียงลำดับ widths และ heights จากมากไปน้อย (reverse=True)
ชิ้นที่มีพื้นที่ใหญ่ที่สุด = widths[0] * heights[0]
ชิ้นที่มีพื้นที่ใหญ่เป็นอันดับสอง = ค่ามากสุดระหว่าง (widths[0] * heights[1]) กับ (widths[1] * heights[0])
แสดงผลลัพธ์ ชิ้นใหญ่ที่สุด และ ชิ้นใหญ่เป็นอันดับสอง
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
20 12 3 4
2 10 14
1 6 8 10
```

Expected output:

```text
40 30
```

Actual output:

```text
40 30
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
4 5 3 4
1 2 3
1 2 3 4
```

Expected output:

```text
1 1
```

Actual output:

```text
1 1
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
เช็กความถูกต้อง
```

Input:

```text
5 5 1 1
4 
4
```

Expected output:

```text
16 4
```

Actual output:

```text
16 4
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
