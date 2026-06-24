choice = "y"

# Loop to allow another student's marks to be entered continuously
while choice.lower() == "y":

    # Prompt the user to enter marks for three quizzes and convert them to floats
    quiz_1 = float( input ( "Enter Quiz 1 mark: " ) )
    quiz_2 = float( input ( "Enter Quiz 2 mark: " ) )
    quiz_3 = float( input ( "Enter Quiz 3 mark: " ) )

    # Calculate the average mark and display it
    average = (quiz_1 + quiz_2 + quiz_3) / 3
    print(f"Average mark: {average:.2f}")

    # Determine and display whether the student passes or fails
    if average >= 50:
        print("Status: Pass")
    else:
        print("Status: Fail")

    # Ask the user if they want to process another student
    choice = input ( "Continue? Select Y/N: " )

print("Program Ended")



#Design the Algorithm
#START
#    Set choice to "y"
#    WHILE choice is equal to "y" OR "Y"
#        PROMPT and INPUT quiz_1
#        PROMPT and INPUT quiz_2
#        PROMPT and INPUT quiz_3
        
#        COMPUTE average = (quiz_1 + quiz_2 + quiz_3) / 3
#        OUTPUT average
        
#        IF average >= 50 THEN
#            OUTPUT "Pass"
#        ELSE
#            OUTPUT "Fail"
#        ENDIF
        
#        PROMPT and INPUT choice ("Continue? Select Y/N: ")
#    ENDWHILE
#    OUTPUT "Program Ended"
#END

#2.2. Identify the Algorithm Structure
#2.2.1. Sequence: The sequential steps of taking inputs, calculating the average, and displaying results one after the other.

#2.2.2. Selection: The if-else statement used to decide whether the student passes or fails based on the score.

#2.2.3. Iteration: The while loop that allows the user to repeat the process for multiple students until they choose to stop.