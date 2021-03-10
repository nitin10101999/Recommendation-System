# How to run:
>Command: python3 recommendationsystem.py

# Note:

## Before running the file-

### If you are running for first time
>Then goto line no 118 and choose your embedded vector size i.e. 64

>Then uncomment the code between line no (125 to 131) and rename the dictionary file as per your convenience

>run the code
  
### If you have already run the code for the same embedded vector size i.e. 64
>Then comment the code between line no (125 to 131) if not already commented 

>run the code.
  

I am providing above process to execute our code faster after running one time. Actually what am I doing is that I am storing the userId and hotelId features embedded vector to a dictionary and storing it to a file. For the first time in creating the dictionary it takes some time. then After other we just have to load the already created dictionary file and this would result in increase in run time.


#Info:
>fetchData.py => to fetch data from the txt file for the tripAdvisor dataset
