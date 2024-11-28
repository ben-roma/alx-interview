# 0x03. Log Parsing

This project focuses on developing a real-time log parsing script in Python. The script reads data from standard input (stdin), analyzes it, and computes metrics based on specific patterns and values.

## Learning Objectives

By the end of this project, you should be able to:

* Read data from standard input (stdin) in Python.
* Parse log entries to extract relevant information.
* Handle different data types and formats.
* Compute metrics based on the processed data.
* Implement signal handling to gracefully interrupt program execution.

## Project Structure

The project contains the following file:

* **0-stats.py:** A Python script that reads stdin line by line and computes metrics.

## Task

### 0. Log parsing

* Write a script that reads stdin line by line and computes metrics:
    * Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
    * After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
        * `Total file size: File size: <total size>` where `<total size>` is the sum of all previous `<file size>` (see input format above)
        * `Number of lines by status code:`
            * Possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
            * If a status code doesn’t appear or is not an integer, don’t print anything for this status code
            * Format: `<status code>: <number>`
            * Status codes should be printed in ascending order

## Technologies Used

* Python

## Resources

* [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
* [Python Signal Handling](https://docs.python.org/3/library/signal.html)
* [Python Regular Expressions](https://docs.python.org/3/library/re.html)
* [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
* [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)


This README provides a clear explanation of the log parsing project, its objectives, and the technologies used. It serves as a guide for understanding and implementing the Python script for real-time log analysis.