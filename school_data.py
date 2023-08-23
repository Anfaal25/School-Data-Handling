# school_data.py
# A terminal-based application to process and plot data based on given user input and provided csv files.


import numpy as np
import matplotlib.pyplot as plt
import math


class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Import data here

school_name = ['Centennial High School','Robert Thirsk School',
            'Louise Dean School','Queen Elizabeth High School',
            'Forest Lawn High School','Crescent Heights High School',
            'Western Canada High School','Central Memorial High School',
            'James Fowler High School','Ernest Manning High School',
            'William Aberhart High School','National Sport School',
            'Henry Wise Wood High School','Bowness High School',
            'Lord Beaverbrook High School','Jack James High School',
            'Sir Winston Churchill High School','Dr. E. P. Scarlett High School',
            'John G Diefenbaker High School','Lester B. Pearson High School']

school_code = ['1224','1679','9626','9806',
            '9813','9815','9816','9823',
            '9825','9826','9829','9830',
            '9836','9847','9850','9856',
            '9857','9858','9860','9865']

school_d = dict(zip(school_name , school_code))


#  Create a dictionary for all school names and codes
#  Create a list of school codes to help with index look-up in arrays


# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    print('Array data for 2018 - 2019:')
    data_2018_2019 = np.genfromtxt('Schooldata_2018-2019.csv', delimiter = ',' , skip_header = True)
    print(data_2018_2019)
    print('')
    print('Array data for 2019 - 2020:')
    data_2019_2020 = np.genfromtxt('Schooldata_2019-2020.csv', delimiter = ',' , skip_header = True)
    print(data_2019_2020)
    print('')
    print('Array data for 2020 - 2021:')
    data_2020_2021 = np.genfromtxt('Schooldata_2020-2021.csv', delimiter = ',' , skip_header = True)
    print(data_2020_2021)
    print('')

    # Add request for user input here

    user_input = input('Please enter the high school name or code: ')                                # User input is requested here.
 
    while user_input not in school_name and user_input not in school_code:                           # While loop to ensure user inputs a valid school code / name.
            print('You must enter a valid school name or code.')
            user_input = input('Please enter the high school name or code: ')
  
    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class

    for x in school_code:                                                                           # This ensures that if the user inputs the school code, the school name and code will be printed. 
        if (x == user_input):
            position = school_code.index(user_input)
            school = School(school_name[position] , user_input)
            school.print_all_stats()

    for x in school_name:                                                                           # This ensures that if the user inputs the school name, the school name and code are printed. 
        if (x == user_input):
            school = School(user_input , school_d[user_input])
            school.print_all_stats()

    # Add data processing and plotting here

    for x in school_code:                                                                           # Following are the operations carried out when the user inputs a school code and it is valid. 
        if x == user_input:
                row_of_x = school_code.index(user_input)                                            # Gets the row index of the code in the array.
                gr_10_19_20 = int(data_2019_2020[row_of_x][1])                                      # The grade 10 value during 2019-2020.
                gr_10_18_19 = int(data_2018_2019[row_of_x][1])                                      # The grade 10 value during 2018-2019.
                gr_10_20_21 = int(data_2020_2021[row_of_x][1])                                      # The grade 10 value during 2020 - 2021.
                mean_gr_10 = (gr_10_18_19 + gr_10_19_20 + gr_10_20_21)/ 3                           # Mean enrollment for grade 10 calculation.
                print('Mean enrollment for Grade 10:', (math.floor(mean_gr_10)))

                row_of_x = school_code.index(user_input)                                            # Gets the row index of the code in the array.
                gr_11_19_20 = int(data_2019_2020[row_of_x][2])                                      # The grade 11 value during 2019-2020.
                gr_11_18_19 = int(data_2018_2019[row_of_x][2])                                      # The grade 11 value during 2019-2020.
                gr_11_20_21 = int(data_2020_2021[row_of_x][2])                                      # The grade 11 value during 2019-2020.
                mean_gr_11 = (gr_11_18_19 + gr_11_19_20 + gr_11_20_21)/ 3                           # Mean enrollment for grade 11 calculation.
                print('Mean enrollment for Grade 11:', math.floor(mean_gr_11))

                row_of_x = school_code.index(user_input)                                            # Gets the row index of the code in the array.
                gr_12_19_20 = int(data_2019_2020[row_of_x][3])                                      # The grade 12 value during 2019-2020.
                gr_12_18_19 = int(data_2018_2019[row_of_x][3])                                      # The grade 12 value during 2019-2020.
                gr_12_20_21 = int(data_2020_2021[row_of_x][3])                                      # The grade 12 value during 2019-2020.
                mean_gr_12 = (gr_12_18_19 + gr_12_19_20 + gr_12_20_21)/ 3                           # Mean enrollment for grade 12 calculation.
                print('Mean enrollment for Grade 12:', math.floor(mean_gr_12))


                row_of_x = school_code.index(user_input)                                            # Gets the row index of the school code in the array.
                yr_12_19_20 = np.sum(data_2019_2020[row_of_x][3])                                   # Gets value of grade 12 students in 2019 - 2020.
                yr_12_18_19 = np.sum(data_2018_2019[row_of_x][3])                                   # Gets value of grade 12 students in 2018 - 2019.
                yr_12_20_21 = np.sum(data_2020_2021[row_of_x][3])                                   # Gets value of grade 12 students in 2020 - 2021
                total_graduated = yr_12_18_19 + yr_12_19_20 + yr_12_20_21                          # Total number of students who graduated.
                print('Total number of students who graduated in the past three years:' , math.floor(total_graduated))

                break 
    
    for x in school_name:                                                                           # This ensures that if the user inputs the school name, the school name and code are printed. 
        if (x == user_input):
                school_cd = school_d[user_input]                                                    # Gets the school code from the school dictionary. 
                row_of_x = school_code.index(school_cd)                                             # Code performs the same as above. This is only done when the user inputs the school name and not the school code. 
                gr_10_19_20 = int(data_2019_2020[row_of_x][1]) 
                gr_10_18_19 = int(data_2018_2019[row_of_x][1])
                gr_10_20_21 = int(data_2020_2021[row_of_x][1])
                mean_gr_10 = (gr_10_18_19 + gr_10_19_20 + gr_10_20_21)/ 3
                print('Mean enrollment for Grade 10:', (math.floor(mean_gr_10)))

                row_of_x = school_code.index(school_cd)
                gr_11_19_20 = int(data_2019_2020[row_of_x][2]) 
                gr_11_18_19 = int(data_2018_2019[row_of_x][2])
                gr_11_20_21 = int(data_2020_2021[row_of_x][2])
                mean_gr_11 = (gr_11_18_19 + gr_11_19_20 + gr_11_20_21)/ 3
                print('Mean enrollment for Grade 11:', math.floor(mean_gr_11))

                row_of_x = school_code.index(school_cd)
                gr_12_19_20 = int(data_2019_2020[row_of_x][3]) 
                gr_12_18_19 = int(data_2018_2019[row_of_x][3])
                gr_12_20_21 = int(data_2020_2021[row_of_x][3])
                mean_gr_12 = (gr_12_18_19 + gr_12_19_20 + gr_12_20_21)/ 3
                print('Mean enrollment for Grade 12:', math.floor(mean_gr_12))


                row_of_x = school_code.index(school_cd)
                yr_12_19_20 = np.sum(data_2019_2020[row_of_x][3]) 
                yr_12_18_19 = np.sum(data_2018_2019[row_of_x][3])
                yr_12_20_21 = np.sum(data_2020_2021[row_of_x][3])
                total_enrollment = yr_12_18_19 + yr_12_19_20 + yr_12_20_21
                print('Total number of students who graduated in the past three years:' , math.floor(total_enrollment))

                break       
    
    


    
    x_vals = [10,11,12]                                                                                         # X values for the graph.
    y_vals_3 = [(data_2020_2021[row_of_x][1]),(data_2020_2021[row_of_x][2]),(data_2020_2021[row_of_x][3])]      # Y values for the 2021 Enrollment.
    plt.scatter(x_vals,y_vals_3)                                                                                # Ensure only markers are plotted with no lines.
    plt.plot(x_vals , y_vals_3 , 'b.' , markersize = 11.5 , label = '2021 Enrollment')                          # Plots blue markers along with the appropriate label,  which is according to the format requested. 


    x_vals = [10,11,12]                                                                                         # X values for the graph.
    y_vals_2 = [(data_2019_2020[row_of_x][1]),(data_2019_2020[row_of_x][2]),(data_2019_2020[row_of_x][3])]      # Y values for the 2020 Enrollment.
    plt.scatter(x_vals,y_vals_2)                                                                                # Ensure only markers are plotted with no lines.
    plt.plot(x_vals , y_vals_2 , 'g.', markersize = 11.5 , label = '2020 Enrollment')                           # Plots green markers along with the appropriate label,  which is according to the format requested. 


    x_vals = [10,11,12]                                                                                         # X values for the graph. 
    y_vals_1 = [(data_2018_2019[row_of_x][1]),(data_2018_2019[row_of_x][2]),(data_2018_2019[row_of_x][3])]      # Y values for the 2019 Enrollment.
    plt.scatter(x_vals,y_vals_1)                                                                                # Ensure only markers are plotted with no lines. 
    plt.plot(x_vals , y_vals_1,'r.', markersize = 11.5 , label = '2019 Enrollment')                             # Plots red markers along with the appropriate label,  which is according to the format requested. 


   


    x_ticks = np.arange(10,13,1)                                                                                # Arranges the intervals so that only three X values are shown on the graph.  
    plt.xticks(x_ticks)
    plt.xlabel('Grade Level')                                                                                   # Sets a label for the X axis. 
    plt.ylabel('Number of Students')                                                                            # Sets a label for the Y axis. 
    plt.title('Grade Enrollment by Year')                                                                       # Sets a title for the entire graph. 
    plt.legend(shadow = True , loc = 'upper left')                                                              # Sets the location of the legend to the top left of the graph so as to not interfere with the plots and also follow the format requested. 
    plt.show()



     
    
    x_vals_sub = [2019 , 2020 , 2021]                                                                            # X axis values.     
    x_ticks_sub = np.arange(2019,2022,1)


    plt.subplot(3,1,1)                                                                                           # Position of the first Subplot. 
    plt.xticks(x_ticks_sub) 
    plt.title('Enrollment by grade')                                                                             # Title of all the subplots.
    plt.ylabel('Number of Students')                                                                             # Y axis label.
    y_vals_sub_10 = [data_2018_2019[row_of_x][1] , data_2019_2020[row_of_x][1] , data_2020_2021[row_of_x][1]]    # Y values for the first subplot.
    plt.plot( x_vals_sub,  y_vals_sub_10 , 'y--', label = 'Grade 10')                                            # Parameters added to meet the format requested.
    plt.legend(shadow = True , loc = 'upper right')                                                              # Position of the legend according to the format requested.
    
    plt.subplot(3,1,2)                                                                                           # Position of the second Subplot.
    plt.xticks(x_ticks_sub)
    plt.ylabel('Number of Students')                                                                             # Y axis label.
    y_vals_sub_11 = [data_2018_2019[row_of_x][2] , data_2019_2020[row_of_x][2] , data_2020_2021[row_of_x][2]]    # Y values for the first subplot.
    plt.plot(x_vals_sub,  y_vals_sub_11 , 'm--', label = 'Grade 11')                                             # Parameters added to meet the format requested.
    plt.legend(shadow = True , loc = 'upper right')                                                              # Position of the legend according to the format requested.

    plt,plt.subplot(3,1,3)                                                                                       # Position of the third Subplot.
    plt.xticks(x_ticks_sub)
    plt.xlabel('Enrollment Year')                                                                                # X label for all the subplots.
    plt.ylabel('Number of Students')                                                                             # Y axis label.
    y_vals_sub_12 = [data_2018_2019[row_of_x][3] , data_2019_2020[row_of_x][3] , data_2020_2021[row_of_x][3]]    # Y values for the first subplot.
    plt.plot(x_vals_sub,  y_vals_sub_12 , 'c--', label = 'Grade 12')                                             # Parameters added to meet the format requested.
    plt.legend(shadow = True , loc = 'upper right')                                                              # Position of the legend according to the format requested.

    plt.show()
    



if __name__ == '__main__':
    main()

