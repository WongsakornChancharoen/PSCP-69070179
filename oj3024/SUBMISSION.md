# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3024
```

OJ submission ID, if submitted:

```text
550959
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
รับ input เป็นเลขจำนวนจริง 2 บรรทัด
โดยจะเป็นคะแนนโหวตทั้ง 3 รวมกัน และคะแนนโหวตสูงสุดตามลำดับ
ต้องนำข้อมูลที่ได้มาหาคะแนนโหวตต่ำสุดแล้วหาผลต่างกับคะแนนสูงสุด
ถ้ามากกว่า 2 ปริ้น "Surprising" หากไม่ ปริ้น "Not surprising"
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
Step 1: รับ Input เป็นจำนวนจริง 2 บรรทัด (คะแนนรวม, คะแนนสูงสุด)
Step 2: คะแนนต่ำสุด = คะแนนรวม - คะแนนสูงสุด * 3
Step 3: นำคะแนนสูงสุดลบกับคะแนนต่ำสุดที่ได้
Step 4: ถ้าผลต่างคะแนนมากกว่า 2 ปริ้น "Surprising" หากไม่ ปริ้น "Not surprising"
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
แผนคล้ายเดิมแต่มีการแก้ไขสูตรให้ถูกต้องกับเพิ่มขั้นตอน
Step 1: รับ Input เป็นจำนวนจริง 2 บรรทัด (คะแนนรวม, คะแนนสูงสุด)
Step 2: คะแนนต่ำสุด = คะแนนรวม - คะแนนสูงสุด * 2
Step 3: เนื่องจาก คะแนนสูงสุด * 2 จะมากกว่า คะแนนรวม ก็ต่อเมื่อคะแนนต่ำสุด = 0
    ดังนั้นถ้าคะแนนต่ำสุดน้อยกว่า 0 ให้ใส่คะแนนต่ำสุดเป็น 0
Step 4: นำคะแนนสูงสุดลบกับคะแนนต่ำสุดที่ได้
Step 5: ถ้าผลต่างคะแนนมากกว่า 2 ปริ้น "Surprising" หากไม่ ปริ้น "Not surprising"
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
เพื่อทดสอบว่าถ้าหากคะแนนสูงสุด * 2 มากกว่าคะแนนรวม (ต่ำสุด = 0)
ผลจะออกมาตรงไหม
```

Input:

```text
10
6
```

Expected output:

```text
Surprising
```

Actual output:

```text
Surprising
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
เพื่อทดสอบว่าผลจะออกมาเป็น Not surprising
```

Input:

```text
30
10
```

Expected output:

```text
Not surprising
```

Actual output:

```text
Not surprising
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
เพื่อทดสอบว่าผลจะเป็น Surprising
```

Input:

```text
27
10
```

Expected output:

```text
Surprising
```

Actual output:

```text
Surprising
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
