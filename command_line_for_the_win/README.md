# CMD Challenge Project

This README documents the steps taken to complete the CMD Challenge project, which requires participants to demonstrate command-line skills and SFTP usage to transfer files.

## Table of Contents
- [Objective](#objective)
- [Steps](#steps)
  - [Completing CMD Challenges](#completing-cmd-challenges)
  - [Taking Screenshots](#taking-screenshots)
  - [Using SFTP to Transfer Files](#using-sftp-to-transfer-files)
  - [Verifying File Transfer](#verifying-file-transfer)
- [Tools Used](#tools-used)
- [Author](#author)

## Objective

The primary objective of this project is to complete specific challenges on CMD CHALLENGE, take screenshots of the completed challenges, and transfer them to a specified directory on a remote server using SFTP.

## Steps

### Completing CMD Challenges

1. Navigate to [CMD CHALLENGE website](https://www.cmdchallenge.com/).
2. Complete the required challenges as per the project guidelines.

### Taking Screenshots

1. After completing each challenge, capture a screenshot as evidence.
2. Save the screenshots with appropriate names, such as `0-first_9_tasks.jpg`, `1-next_9_tasks.jpg`, etc., for easy reference.

### Using SFTP to Transfer Files

1. Open a terminal or command prompt on your local machine.
2. Initiate an SFTP connection to the remote server:

    ```bash
    sftp username@remote_server_address
    ```

3. Navigate to the directory where you saved the screenshots:

    ```bash
    lcd path_to_screenshots_directory
    ```

4. Upload the screenshots to the server:

    ```bash
    put screenshot_name.extension
    ```

    Repeat this step for all screenshots.

5. If necessary, move the uploaded screenshots to the desired directory on the server:

    ```bash
    rename screenshot_name.extension target_directory/screenshot_name.extension
    ```

### Verifying File Transfer

1. After transferring, navigate to the target directory on the remote server:

    ```bash
    cd target_directory
    ```

2. List the contents to ensure all screenshots are present:

    ```bash
    ls
    ```

## Tools Used

- CMD CHALLENGE website
- SFTP (Secure File Transfer Protocol)
- Terminal or Command Prompt

## Author

[Gift Amachree]
