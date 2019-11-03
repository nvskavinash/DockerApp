# DockerApp
This project is for finding number of words in all the text files present in a folder <br>
Once the word count of all the files is shown the file with highest number of words is displayed<br>
Then all the above mentioned data along with machines IP Address and our name will be written into a filename called result.txt<br>
After which the contents from result.txt will be read and displayed in the console<br>
The input folder will be mapped to /home/data in the container using the command: docker run -v /mylaptop/dir:/home/data<br>
