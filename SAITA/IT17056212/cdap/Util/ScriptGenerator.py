from Models.Inputs import Input
from Controllers.Query import Queries
import subprocess
import sys


class ScriptGenerator:
    inp = None
    newname_variable = None
    newpath_variable = None
    parameter_dict = {}

    def __init__(self):
        self.inp = Input.get_input()

    # Get solution sequence
    def getsolution_sequence(self, solutionid):
        solution_seq = Queries.get_technical_solution_sequence_by_solution_id(solutionid)
        return solution_seq[0][0]

    # Check parameter status of te solution
    def check_param_status(self, stepid):
        para_status = Queries.get_technical_solution_parameter_status_by_cid(stepid)
        return para_status

    # Execute solution sequence
    def process_sequence(self, solutionid):
        command_list = []
        shell_command = ""
        solution_seq = self.getsolution_sequence(solutionid)
        split_seq = solution_seq.split("-")

        for step in split_seq:
            para_stat = self.check_param_status(step)

            if para_stat[0][0].lower() == 'yes':
                v_name = self.set_parameters(step, solutionid)
                shell_command = self.write_command(step, v_name)
            else:
                v_name = "none"
                shell_command = self.write_command(step, v_name)
            command_list.append(shell_command)

        self.execute_command(command_list)
        self.execution_status()

    # Set parameters for the PowerShell commands
    def set_parameters(self, step, solutionid):
        variable_names = Queries.get_technical_solution_variables_by_cid(step)
        v_names = variable_names[0][0].split(",")

        for variable_name in v_names:
            if variable_name == 'namevariable':
                self.parameter_dict.update({'namevariable': self.inp.get_name_para()})
                print(self.parameter_dict)
            elif variable_name == 'pathvariable':
                self.parameter_dict.update({'pathvariable': ''})
            elif variable_name == 'warning':
                warn = Queries.get_technical_solution_warning_by_solution_id(solutionid)
                self.parameter_dict.update({'warning': warn[0][0]})

        return variable_name

    # Write the command sequence
    def write_command(self, step, variable_name):
        final_command = ""
        if variable_name != 'none':
            command = Queries.get_technical_solution_command_by_cid(step)
            param_value = self.parameter_dict.get(variable_name)
            final_command = command[0][0].replace(variable_name, param_value)

        else:
            command = Queries.get_technical_solution_command_by_cid(step)
            final_command = command[0][0]

        return final_command

    # Write and execute the command list using a PS1 file
    def execute_command(self, command_list):
        ex_stats = []
        shell_file = open("D:\\testShellScript.ps1", "w+")
        shell_file.write("Clear-Content d:\ExecutionStatus.txt")
        for line in command_list:
            stat = "\nWrite-output" + " $? >> d:\ExecutionStatus.txt"

            shell_file.write("\n" + line)
            shell_file.write("\n" + stat)

        p = subprocess.Popen(["powershell.exe",
                              "D:\\testShellScript.ps1"],
                             stdout=sys.stdout)

    # Get the execution status
    def execution_status(self):
        status_file = open("d:\ExecutionStatus.txt", "r")

        count = 0
        while True:
            count += 1

            # Get next line from file
            line = status_file.readline()

            # if line is empty
            # end of file is reached
            if not line:
                break
            print("Line{}: {}".format(count, line.strip()))

        status_file.close()
