
# Python module for copying objects
import copy


# Importing application internal classes
from grades import Grades
from grade_weights import GradeWeights

class GradeCalculator:
    """
    Calculates the overall course grade for ENPM611.
    """

    @staticmethod
    def calculate_remaining_required_for_a_grade(grades: Grades, weights:GradeWeights) -> float:
        """
        """
        goal_grade = 90
        current_grade = 0
        grade_map = Grades()

        if grades.quiz_1 is not None:
            current_grade += grades.quiz_1 * weights.quiz_1
            grade_map.quiz_1 = 1
        if grades.quiz_2 is not None:
            current_grade += grades.quiz_2 * weights.quiz_2
            grade_map.quiz_2 = 1
        if grades.midterm is not None:
            current_grade += grades.midterm * weights.midterm
            grade_map.midterm = 1
        if grades.project is not None:
            current_grade += grades.project * weights.project
            grade_map.project = 1
        if grades.final is not None:
            current_grade += grades.final * weights.final
            grade_map.final = 1

        if grade_map.quiz_1 is not None:
            goal_grade -= (weights.quiz_1 * 100)
        if grade_map.quiz_2 is not None:
            goal_grade -= (weights.quiz_2 * 100)
        if grade_map.midterm is not None:
            goal_grade -= (weights.midterm * 100)
        if grade_map.project is not None:
            goal_grade -= (weights.project * 100)
        if grade_map.final is not None:
            goal_grade -= (weights.final * 100)

        if goal_grade - current_grade < 0:
            return 0

        return goal_grade - current_grade

    @staticmethod
    def calculate_course_percentage(grades:Grades, weights:GradeWeights) -> float:
        """"
        Calculates the percentace of the overall course
        grade. If not all grades have been set yet, this
        function returns None.
        """
        if grades.quiz_1 is None or grades.quiz_2 is None or grades.midterm is None or grades.project is None or grades.final is None:
            print("Can't calculate final grade without all assignments graded")
            return None
        else:
            quizzes_part = ((grades.quiz_1 + grades.quiz_2) / 2) * weights.quizzes
            midterm_part = grades.midterm * weights.midterm
            project_part = grades.project * weights.project
            final_part = grades.final * weights.final
            course_grade = quizzes_part + midterm_part + project_part + final_part
            return course_grade
        
        
    @staticmethod
    def calculate_optimistic_course_percentage(grades:Grades, weights:GradeWeights) -> float:
        """
        Calculates the course percentage grade assuming that
        all assignments that have not been completed receive 100%. 
        """
        
        # Need to create a copy so that we don't overwrite
        # the values of the Grades object that was passed in
        optimistic_grades:Grades = copy.copy(grades)
        
        # Now we are setting all grades that have not been set
        # to the maximum percentage of 100%
        if optimistic_grades.quiz_1 is None:
            optimistic_grades.quiz_1 = 1
        if optimistic_grades.quiz_2 is None:
            optimistic_grades.quiz_2 = 1
        if optimistic_grades.midterm is None:
            optimistic_grades.midterm = 1
        if optimistic_grades.project is None:
            optimistic_grades.project = 1
        if optimistic_grades.final is None:
            optimistic_grades.final = 1
        
        # Let the basic calculation function take care of actually
        # calculating the percentage grade
        return GradeCalculator.calculate_course_percentage(optimistic_grades, weights)
        
    @staticmethod
    def calculate_letter_grade(percentage_grade:float) -> str:
        """
        Calculate the letter grade giving a percentage grade.
        The cutoffs for letter grades can be found in the introductory slides
        and in the syllabus.
        """
        
        # Avoid exception due to missing value
        if percentage_grade is None:
            return None
        
        # Return the letter that corresponds to
        # the percentage cutoff
        if percentage_grade >= 0.91:
            return 'A'
        elif percentage_grade >= 0.8:
            return 'B'
        elif percentage_grade >= 0.74:
            return 'C'
        elif percentage_grade >= 0.6:
            return 'D'
        else:
            return 'F'