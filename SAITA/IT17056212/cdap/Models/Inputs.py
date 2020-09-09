class Input(object):
    myInput = None
    keywords = []
    name_para = None
    path_para = None
    error_msg = None
    error_code = None
    comp_type = None
    component = None
    category = None
    question1 = None
    question2 = None
    question3 = None
    question4 = None

    @classmethod
    def get_input(cls, new=False):
        if new or not cls.myInput:
            cls.myInput = Input()

        return cls.myInput

    @classmethod
    def get_category(cls):
        # print(cls.category)
        return cls.category

    @classmethod
    def set_category(cls, cat):
        cls.category = cat

    @classmethod
    def get_component(cls):
        # print(cls.component)
        return cls.component

    @classmethod
    def set_component(cls, comp):
        cls.component = comp

    @classmethod
    def get_input_array(cls):
        if cls.component == 'identifying':
            input_array = [[cls.error_msg, cls.error_code, cls.comp_type, 1]]
            return input_array
        if cls.component == 'categorizing':
            input_array = [[cls.question1, cls.question2, cls.question3, cls.question4, 'non-tech']]
            return input_array

    @classmethod
    def get_error_msg(cls):
        return cls.error_msg

    @classmethod
    def set_error_msg(cls, msg):
        cls.error_msg = msg.lower()

    @classmethod
    def get_error_code(cls):
        return cls.error_code

    @classmethod
    def set_error_code(cls, code):
        cls.error_code = code.lower()

    @classmethod
    def get_type(cls):
        return cls.comp_type

    @classmethod
    def set_type(cls, type):
        cls.comp_type = type.lower()

    @classmethod
    def get_question1(cls):
        return cls.question1

    @classmethod
    def set_question1(cls, question):
        cls.question1 = question

    @classmethod
    def get_question2(cls):
        return cls.question2

    @classmethod
    def set_question2(cls, question):
        cls.question2 = question

    @classmethod
    def get_question3(cls):
        return cls.question3

    @classmethod
    def set_question3(cls, question):
        cls.question3 = question

    @classmethod
    def get_question4(cls):
        return cls.question4

    @classmethod
    def set_question4(cls, question):
        cls.question4 = question

    @classmethod
    def get_keyword(cls):
        return cls.keywords

    @classmethod
    def set_keyword(cls, word):
        cls.keywords = word

    @classmethod
    def get_name_para(cls):
        return cls.name_para

    @classmethod
    def set_name_para(cls, name_para):
        cls.name_para = name_para

    @classmethod
    def get_path_para(cls):
        return cls.path_para

    @classmethod
    def set_path_para(cls, path_para):
        cls.path_para = path_para
