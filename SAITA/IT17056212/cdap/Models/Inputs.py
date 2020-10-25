class Input(object):
    myInput = None
    keywords = []  # Non technical keywords for NLG
    name_para = None  # Name parameter
    path_para = None  # Path parameter
    error_msg = None  # Error message
    error_code = None  # Error code
    comp_type = None  # Component type
    component = None  # component
    category = None  # Category
    question1 = None  # Question 1
    question2 = None  # Question 2
    question3 = None  # Question 3
    question4 = None  # Question 4

    # Make the inputs class as a singleton
    @classmethod
    def get_input(cls, new=False):
        if new or not cls.myInput:
            cls.myInput = Input()

        return cls.myInput

    # Get category
    @classmethod
    def get_category(cls):
        # print(cls.category)
        return cls.category

    # Set category
    @classmethod
    def set_category(cls, cat):
        cls.category = cat

    # Get component
    @classmethod
    def get_component(cls):
        # print(cls.component)
        return cls.component

    # Set component
    @classmethod
    def set_component(cls, comp):
        cls.component = comp

    # Get input array
    @classmethod
    def get_input_array(cls):
        if cls.component == 'identifying':
            input_array = [[cls.error_msg, cls.error_code, cls.comp_type, 1]]
            return input_array
        if cls.component == 'categorizing':
            input_array = [[cls.question1, cls.question2, cls.question3, cls.question4, 'non-tech']]
            return input_array

    # Get error message
    @classmethod
    def get_error_msg(cls):
        return cls.error_msg

    # Set error message
    @classmethod
    def set_error_msg(cls, msg):
        cls.error_msg = msg.lower()

    # Get error code
    @classmethod
    def get_error_code(cls):
        return cls.error_code

    # Set error code
    @classmethod
    def set_error_code(cls, code):
        cls.error_code = code.lower()

    # Get error type
    @classmethod
    def get_type(cls):
        return cls.comp_type

    # Set error type
    @classmethod
    def set_type(cls, type):
        cls.comp_type = type.lower()

    # Get question 1
    @classmethod
    def get_question1(cls):
        return cls.question1

    # Set question 1
    @classmethod
    def set_question1(cls, question):
        cls.question1 = question

    # Get question 2
    @classmethod
    def get_question2(cls):
        return cls.question2

    # Set question 2
    @classmethod
    def set_question2(cls, question):
        cls.question2 = question

    # Get question 3
    @classmethod
    def get_question3(cls):
        return cls.question3

    # Set question 3
    @classmethod
    def set_question3(cls, question):
        cls.question3 = question

    # Get question 4
    @classmethod
    def get_question4(cls):
        return cls.question4

    # Get question 4
    @classmethod
    def set_question4(cls, question):
        cls.question4 = question

    # Get keywords
    @classmethod
    def get_keyword(cls):
        return cls.keywords

    # Set keywords
    @classmethod
    def set_keyword(cls, word):
        cls.keywords = word

    # Get name parameter
    @classmethod
    def get_name_para(cls):
        return cls.name_para

    # Set name parameter
    @classmethod
    def set_name_para(cls, name_para):
        cls.name_para = name_para

    # Get path parameter
    @classmethod
    def get_path_para(cls):
        return cls.path_para

    # Set path parameter
    @classmethod
    def set_path_para(cls, path_para):
        cls.path_para = path_para
