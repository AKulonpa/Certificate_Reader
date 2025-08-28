The goal of this project was to develop a program that can automatically read and evaluate job certificates in order to support internship decisions, general vs. professional internship. The program is able to process different file formats such as PDF, TXT, Word, and JPG, even when the text is unstructured or unclear.

The implemented solution works as follows:

1.The input file (certificate) is read and converted into text using appropriate methods.

2.The extracted text is sent to OpenAI’s API for analysis.

3.The AI answers specific questions, such as employee’s duties, work period, company, estimated ECTS credits, and whether the work is related to the persons studies.

4.The structured output is returned to the user.
