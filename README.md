# nginx_loganalysis
Analyzing an nginx log file using python and streamlit.

**Project description:**
1. In this project, we are analyzing a nginx log file using python and displaying the content in a webpage by utilizing Streamlit and other python packages.
2. The webpage consists of three section and they are:
3. 1. Log table - which is used to display the log data in an organized tabular form.
   2. Side bar  - Which is used to filter the data from the log table by the response code value.
   3. Pie chart - Which is used the display the activity count of the ip addresses.

**Installation process:**
1. Download the csv file from the main or use your own file and open it in any environment that supports python.
2. Download the "loganalysis_streamlit.py" and open it.
3. Download streamlit using:
 1. pip install streamlit (make sure that pip is already installed)
4. Download pandas using:
 1. pip install pandas 
5. Download plotly using:
 1. pip install plotly
7. If you are using a different a file, go replace it in the line #23.
8. Adjust your column and row vaules accordingly and execute the file.
 
**Benefits**
1. Going through a log file in it's raw form is a long task.
2. Using this program, user can view the data in a more oragainzed form, which is easier to go through.
3. User can filter the specific data that is needed, this feature saves a lot of time.
4. Displaying the log data in this interactive form also helps the people to understand things easier.

**Output screenshot:**

   ![Alt text](/NGINX_loganalysis/output.png?raw=true "Output")

**Documentation**
These are some websites that helped me write this program:
1. https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
2. https://www.computerhope.com/htmcolor.htm
3. https://www.youtube.com/playlist?list=PLM8lYG2MzHmRpyrk9_j9FW0HiMwD9jSl5
4. https://www.youtube.com/watch?v=9gm03GMgXbE&ab_channel=ShaunitaNicole
5. https://plotly.com/python/table/

I hope you find these information helpful, thank you very much.
