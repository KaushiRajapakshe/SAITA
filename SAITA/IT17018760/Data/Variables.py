sql_server = "localhost"
sql_db = "saita_ser"
sql_uname = "root"
sql_password = ""
log_enable_all = True
log_enable_error = True
log_enable_warning = True
img_location = "../Icon/SAITA.png"
log_file = "../Data/System.log"
logo = "../Icon/logo.ico"
not_found_img="../Icon/imgnot.png"
logo_div = 0.3
title_bar_bg = "#3a3a3a"
window_bg = "#ffffff"
close_but_acc_bg = "#B10202"
mini_but_acc_bg = "#6F6F6F"
title_bar_but_txt_color = "#ffffff"
title_bar_txt = "SAITA - Corrupted Service Solving System"
title_bar_txt_color = "#ffffff"
full_window_color = "#ffffff"
head_window_color = "#ffffff"
body_window_color = "#ffffff"
cell_bg = "#3a3a3a"
cell_topic_txt_color = "#ffffff"
coll_count = 4
soft_img_dev = 1.2
soft_title_f_size_dev = 45
soft_ver_f_size_dev = 30
pad_val = 20

csvfilepath="../CSVFILES/"
executedLog="log_file.txt"
indexCSV="../SystemCSV/index.csv"
inputCSV="../SystemCSV/input.csv"
shutdownMSG=" Add-Type -AssemblyName PresentationCore,PresentationFramework; $msgBody = ""Your Windows will restart after 30 seconds.Save your works.""; [System.Windows.MessageBox]::Show($msgBody)"
restartCode="Add-Type -AssemblyName PresentationCore,PresentationFramework;$ButtonType = [System.Windows.MessageBoxButton]::YesNo;$MessageIcon = [System.Windows.MessageBoxImage]::Error;$MessageBody = 'Do you want to continue with the restart ?';$MessageTitle = 'SAITA Alert';$Result = [System.Windows.MessageBox]::Show($MessageBody,$MessageTitle,$ButtonType,$MessageIcon);if($Result -eq 'Yes'){Restart-Computer}"



#variables for the saytext class
start_text = "WelCome  You are navigating to solve the abandant service issue category."
end_text = "Have a nice day"
processing = "System is processing your entered value Please wait for a moment."
not_found_error="Your entered value cannot proceed    Check the correct value and try again"
file_exist="You have solved these kind of issues earlier  now system is checking your previous records and processing"
file_not_exist="This is the first time you have found this issue  please wait we are trying to give you the best solution"
generating_csv="system generating the solutions"
solution_executing="solutions are executing"
issue_solved="We want to know is your issue solved"
wrong_input="Please Send Correct Feedback. Is your issue solved in this moment  only yes or no"
if_yes_solved="Your issue solved thank you for join with saita system ask you to restart your windows"
system_terminate="Sorry  You cannot send these kind of values as an errors  System is terminating  Navigate SAITA system again  Thank you"



say_voice = 1
say_speed = 0.5

