'''
lab13_exercises.py

You will write a class called MathQuiz.  It will contain five (5) methods
and simulate a student taking a basic math quiz.

The __init__ method will have three parameters: self, the student name, and a file name.
 Assign the names to instance variables and create four more:
    a score set to 0,
    a boolean for whether the test is graded,
    a list for the questions,
    and a list for the student responses.
 It should also read in the quiz text file and load each line into the questions instance variable.

The __repr__ method should print out the student name, followed by a line of dashes,
 whether or not the quiz is graded, their score, and their percentage.
 It should look something like this:

Name:  	  Nathan
================
Graded:     True
Score:       4/5
Percentage:  80%

or

Name:	  Nathan
================
Graded:    False

The user_submission method will take one parameter: self.
 It will print the student name and then print each problem
 from the questions list and "add the user's answer the responses list."

The check_answer method takes three parameters: self, a string question, and an string answer.
 It must compare the question to the answer, performing the correct operation,
 and returns true if the answer matches and false if it does not.
 Eg:    student.check_answer('2 + 2', '4') --> True
        student.check_answer("4 - 2", "1") --> False

The grade_quiz() method takes one parameter: self.
 It uses check_answer to compare the questions list and the response list.
 For each correct answer, add one to the score

In the main, create two instances of the MathQuiz class and call user_submission on both.
Then print each instance to see the results.
'''






class MathQuiz:
    def __init__(self, name, fname):
        self.name = name
        self.score = 0
        self.graded = False
        self.questions = []
        self.responses = []

        for line in open(fname, 'r'):
            self.questions.append(line.strip())


    def __repr__(self):
        content = '\nName:'.ljust(5) + self.name.rjust(11) + '\n'
        content += '=' * 16 + '\n'
        content += 'Graded:'.ljust(11) + str(self.graded).rjust(5) + '\n'

        if  self.graded == True:
            content += 'Score:'.ljust(12) + str(self.score).rjust(2) + '/5\n'
            content += 'Percentage:'.ljust(12) + (str(self.score * 20) + '%').rjust(4) + '\n'

        return content

    def user_submission(self):
        print(self)

        for problem in self.questions:
            user_respose = input(problem + ' = ')
            self.responses.append(user_respose)






    def check_answer(self, question, answer):
        sign = qustion.split()[1]

        if sign == '+':
            result = qustion.split()[0] + qustion.split()[1]
        elif sign == '-':
            result = qustion.split()[0] - qustion.split()[1]
        elif sign == '*':
            result = qustion.split()[0] * qustion.split()[1]
        elif sign == '/':
            result = qustion.split()[0] / qustion.split()[1]


        return result == int(answer)




    def grade_quiz(self):
        for j in range(len(self.questions)):
            if self.check_answer(self.questions[j], self.responses[j]):
                self.score += 1

        self.graded = True



def main():
    nick = MathQuiz('nick', 'quiz.txt')
    benson = MathQuiz('benson', 'quiz.txt')

    nick.user_submission()
    benson.user_submission()

    nick.grade_quiz()
    benson.grade_quiz()

    print(nick)
    print(benson)


if __name__ == "__main__":
    main()
